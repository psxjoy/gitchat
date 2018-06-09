from chapter7.crawl_info import get_info
from chapter7.send_mail import send_mail
if __name__ == '__main__':
    crawl_url = "http://news.163.com/"
    content = get_info(crawl_url)
    send_mail(content)