import urllib.parse
from typing import Any


def get_news_rss(topic: str, limit: int = 5) -> str:
    """Fetch top news headlines via Google News RSS for a given topic."""
    if not topic:
        return "Please provide a topic."
    q = urllib.parse.quote(topic)
    url = f"https://news.google.com/rss/search?q={q}&hl=en-US&gl=US&ceid=US:en"
    try:
        feedparser: Any = __import__('feedparser')  # dynamic import
    except Exception:
        return "RSS reader not installed. Try 'pip install feedparser'."
    feed = feedparser.parse(url)
    if not feed.entries:
        return "No news articles found."
    items = feed.entries[:max(1, limit)]
    lines = ["Here are the top news headlines:"]
    for e in items:
        title = getattr(e, "title", "(no title)")
        summary = getattr(e, "summary", "").strip()
        lines.append(f"- {title}\n  {summary}")
    return "\n".join(lines)
