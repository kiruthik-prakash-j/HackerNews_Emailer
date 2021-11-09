import mail
import scraper


def format_content(news_content):
    content = ''
    content += news_content
    content += ('<br>----------------------<br>')
    content += ('<br<br>End of Message')
    return content


def main():
    news_content = scraper.extract_news('https://news.ycombinator.com/')
    content = format_content(news_content)
    mail.send_mail(content)

if __name__ == "__main__":
    main()