from newsapi import NewsApiClient
from api_keys import NEWS_API_KEY

newsapi = NewsApiClient(api_key=NEWS_API_KEY)


def get_top_news(topic):
    top_headlines = newsapi.get_top_headlines(q=topic)
    if 'articles' in top_headlines:
        news_summary = "Here are the top news headlines:\n"
        for article in top_headlines['articles'][:5]:  # Limit to top 5 articles
            title = article.get('title')
            description = article.get('description', 'No description available.')
            news_summary += f"Title: {title}\nDescription: {description}\n\n"
        return news_summary
    else:
        return "No news articles found."
    
def get_everything_news(topic):
    all_articles = newsapi.get_everything(q=topic)
    if 'articles' in all_articles:
        news_summary = "Here are the top news headlines:\n"
        for article in all_articles['articles'][:5]:  # Limit to top 5 articles
            title = article.get('title')
            description = article.get('description', 'No description available.')
            news_summary += f"Title: {title}\nDescription: {description}\n\n"
        return news_summary
    else:
        return "No news articles found."

# Test if client works
print(get_top_news("Microsoft"))