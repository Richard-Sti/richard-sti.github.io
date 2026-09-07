"""Check the generated site's navigation, local assets, and basic accessibility."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.elements = []
        self.feed(path.read_text())

    def handle_starttag(self, tag, attrs):
        self.elements.append((tag, dict(attrs)))


root = Path(__file__).resolve().parents[1] / "_site"
expected = {"/", "/research", "/updates", "/blog", "/cv"}
pages = list(root.rglob("*.html"))
assert pages, "Run bundle exec jekyll build first"
for route in expected:
    target = root / (route.lstrip("/") + ".html" if route != "/" else "index.html")
    assert target.is_file(), f"Missing page: {route}"

for path in pages:
    page = Page(path)
    elements = page.elements
    if path == root / "cv.html":
        assert any(tag == "meta" and attrs.get("http-equiv") == "refresh"
                   and attrs.get("content") == "0; url=/images/CV.pdf"
                   for tag, attrs in elements), "The legacy CV route must open the PDF"
        assert (root / "images/CV.pdf").is_file()
        continue
    assert sum(tag == "main" for tag, _ in elements) == 1, path
    assert any(tag == "html" and attrs.get("lang") == "en-GB" for tag, attrs in elements), path
    viewports = [attrs["content"] for tag, attrs in elements
                 if tag == "meta" and attrs.get("name") == "viewport"]
    assert viewports == ["width=device-width, initial-scale=1"], path
    links = {attrs.get("href") for tag, attrs in elements if tag == "a"}
    assert (expected - {"/cv"}) | {"/images/CV.pdf"} <= links, f"Missing navigation on {path}"
    for tag, attrs in elements:
        if tag == "img":
            assert attrs.get("alt"), f"Missing image description: {path}"
        if tag == "iframe":
            assert attrs.get("title"), f"Missing frame title: {path}"
        assert "panel-cover" not in attrs.get("class", ""), path
        for attribute in ("href", "src"):
            url = urlsplit(attrs.get(attribute, ""))
            if url.scheme or url.netloc or not url.path:
                continue
            local = unquote(url.path)
            target = root / local.lstrip("/") if local.startswith("/") else path.parent / local
            candidates = [target, target / "index.html", Path(str(target) + ".html")]
            assert any(candidate.is_file() for candidate in candidates), f"Broken link: {path}: {local}"

print(f"Checked {len(pages)} pages: navigation, local links/assets, and basic accessibility passed.")
