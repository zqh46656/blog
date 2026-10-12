"""Combine Marmite's feeds into one site-wide article feed after building."""

import argparse
import json
from copy import deepcopy
from email.utils import parsedate_to_datetime
from pathlib import Path
import xml.etree.ElementTree as ET


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
        channel.append(item)
    if ordered:
        pub_date = channel.find("pubDate")
        if pub_date is None:
            pub_date = ET.SubElement(channel, "pubDate")
        pub_date.text = ordered[0].findtext("pubDate")
    ET.register_namespace("content", "http://purl.org/rss/1.0/modules/content/")
    tree.write(root / "index.rss", encoding="utf-8", xml_declaration=True)
    print(f"Built unified RSS feed: {len(ordered)} articles")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("site", type=Path)
    build_feed(parser.parse_args().site)
