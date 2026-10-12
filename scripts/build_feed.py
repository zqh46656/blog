"""Combine Marmite's feeds into one site-wide article feed after building."""

import argparse
import json
from copy import deepcopy
from email.utils import parsedate_to_datetime
from html import escape
from html.parser import HTMLParser
from pathlib import Path
import xml.etree.ElementTree as ET


class Summary(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []

    def handle_data(self, data):
        self.parts.append(data)

    def handle_starttag(self, tag, attrs):
        if tag in {"p", "br", "div", "li", "h1", "h2", "h3"}:
            self.parts.append(" ")


def build_feed(root):
    manifest = json.loads((root / "marmite.json").read_text())
    base = manifest["config"]["url"].rstrip("/")
    published = {
        f"{base}/{post['slug']}.html"
        for post in manifest["posts"]
        if post.get("date") and post.get("stream") != "draft"
    }
    tree = ET.parse(root / "index.rss")
    channel = tree.getroot().find("channel")
    items = {}
    years = {
        post["date"][:4] for post in manifest["posts"]
        if post.get("date") and post.get("stream") != "draft"
    }
    # Year feeds cover every category. Their latest 15 entries contain the
    # latest 15 site-wide articles; only use years in the current manifest.
    for year in sorted(years):
        path = root / f"archive-{year}.rss"
        for item in ET.parse(path).findall("./channel/item"):
            link = item.findtext("link")
            if link in published and link not in items:
                items[link] = deepcopy(item)
    ordered = sorted(
        items.values(),
        key=lambda item: (parsedate_to_datetime(item.findtext("pubDate")), item.findtext("link")),
        reverse=True,
    )[:15]
    if published and not ordered:
        raise ValueError("No published articles found in generated RSS feeds")
    for item in channel.findall("item"):
        channel.remove(item)
    for item in ordered:
        source = item.find("source")
        if source is not None:
            item.remove(source)
        author = item.find("author")
        if author is not None:
            ET.SubElement(item, "{http://purl.org/dc/elements/1.1/}creator").text = author.text
            item.remove(author)
        content = item.find("{http://purl.org/rss/1.0/modules/content/}encoded")
        summary = Summary()
        summary.feed(item.findtext("description") or (content.text if content is not None else "") or "")
        text = " ".join("".join(summary.parts).split())
        description = item.find("description")
        if description is None:
            description = ET.SubElement(item, "description")
        description.text = escape(text[:240] + ("…" if len(text) > 240 else ""))
        if content is not None:
            item.remove(content)
        channel.append(item)
    if ordered:
        pub_date = channel.find("pubDate")
        if pub_date is None:
            pub_date = ET.SubElement(channel, "pubDate")
        pub_date.text = ordered[0].findtext("pubDate")
    atom = "http://www.w3.org/2005/Atom"
    for link in channel.findall(f"{{{atom}}}link"):
        if link.get("rel") == "self":
            channel.remove(link)
    self_link = ET.Element(f"{{{atom}}}link", {
        "href": f"{base}/index.rss", "rel": "self", "type": "application/rss+xml",
    })
    channel.insert(0, self_link)
    ET.register_namespace("atom", atom)
    ET.register_namespace("dc", "http://purl.org/dc/elements/1.1/")
    tree.write(root / "index.rss", encoding="utf-8", xml_declaration=True)
    print(f"Built unified RSS feed: {len(ordered)} articles")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("site", type=Path)
    build_feed(parser.parse_args().site)
