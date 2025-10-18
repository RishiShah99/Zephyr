from typing import Optional

from ui import speak


def get_daily_brief(city: Optional[str] = None, news_topic: str = "technology", max_news: int = 3) -> str:
    parts = []

    # Weather
    try:
        if city:
            from weather import get_weather
            parts.append(get_weather(city))
    except Exception as e:
        parts.append(f"Weather unavailable ({e})")

    # Calendar events
    try:
        from planner import see_future_events
        events = see_future_events()
        if events:
            parts.append("Upcoming events:\n" + events)
    except Exception as e:
        parts.append(f"Calendar unavailable ({e})")

    # News (RSS by default)
    try:
        from news_rss import get_news_rss
        parts.append(get_news_rss(news_topic, limit=max_news))
    except Exception:
        try:
            from news import get_top_news
            parts.append(get_top_news(news_topic))
        except Exception as e:
            parts.append(f"News unavailable ({e})")

    return "\n\n".join([p for p in parts if p])


def speak_daily_brief(city: Optional[str] = None, news_topic: str = "technology", max_news: int = 3) -> str:
    brief = get_daily_brief(city, news_topic, max_news)
    speak(brief)
    return brief
