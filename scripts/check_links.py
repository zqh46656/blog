"""Check generated HTML links and assets, including the GitHub Pages base path."""

import argparse
import json
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.ids = set()
        self.links = []
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.ids.update(filter(None, [attrs.get("id")]))
        if tag == "a" and attrs.get("name"):
            self.ids.add(attrs["name"])
        attributes = ["href", "src", "poster"]
        if tag == "object":
            attributes.append("data")
        for attr in attributes:
            if attrs.get(attr):
                self.links.append(attrs[attr])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("site", type=Path)
    args = parser.parse_args()
    root = args.site.resolve()
    manifest = json.loads((root / "marmite.json").read_text())
    base = manifest["config"]["url"].rstrip("/") + "/"
    origin = urlsplit(base)
    # Declared categories with no articles intentionally have no generated page.
    populated_streams = {post["stream"] for post in manifest["posts"]}
    empty_stream_paths = {
        urlsplit(urljoin(base, f"{name}.html")).path
        for name in manifest["config"]["streams"]
        if name not in populated_streams
    }
    pages = {
        path: Page(path.read_text()) for path in root.rglob("*.html")
    }
    errors = set()
    empty_categories = set()
    checked = 0
    for source, page in pages.items():
        current = urljoin(base, source.relative_to(root).as_posix())
        for link in page.links:
            target_url = urlsplit(urljoin(current, link))
            if (target_url.scheme, target_url.netloc) != (origin.scheme, origin.netloc):
                continue
            checked += 1
            path = unquote(target_url.path)
            if not path.startswith(origin.path):
                errors.add(f"{source.name}: {link} escapes the site base path")
                continue
            target = (root / path[len(origin.path):]).resolve()
            if not target.is_relative_to(root):
                errors.add(f"{source.name}: {link} escapes the output directory")
                continue
            if target.is_dir():
                target /= "index.html"
            if not target.is_file():
                if path in empty_stream_paths and not target_url.fragment:
                    empty_categories.add(path)
                else:
                    errors.add(f"{source.name}: {link} points to a missing file")
            elif target_url.fragment and target in pages:
                if unquote(target_url.fragment) not in pages[target].ids:
                    errors.add(f"{source.name}: {link} points to a missing anchor")
    for error in sorted(errors):
        print(error, file=sys.stderr)
    for path in sorted(empty_categories):
        print(f"Allowed empty category: {path} (returns 404 until an article is published).")
    print(f"Checked {len(pages)} HTML pages and {checked} internal references; "
          f"{len(errors)} errors.")
    return bool(errors)


if __name__ == "__main__":
    sys.exit(main())
