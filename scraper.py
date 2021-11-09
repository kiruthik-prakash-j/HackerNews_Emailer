import requests  # http requests
from bs4 import BeautifulSoup  # web scraping


def extract_news(url):
    """
    Gets the url of the Hacker News Website
    Extracts the news using Beautiful Soup and
    Returns the news content as a string
    """
    print('Extracting Hacker News Stories...')
    news_content = ''
    news_content += ("<b>HN Top Stories:</b> \n" + '<br>' + '-' * 50 + '<br>')
    response = requests.get(url)
    response_content = response.content
    soup = BeautifulSoup(response_content, 'html.parser')
    for i, tag in enumerate(soup.find_all('td', attrs={'class': 'title', 'valign': ''})):
        news_content += ((str(i + 1) + '::' + tag.text + "\n" + '<br>') if tag.text != 'More' else '')
    return news_content
