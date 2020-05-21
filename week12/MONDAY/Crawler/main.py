import requests
from bs4 import BeautifulSoup
import re
import string
from setup_database import setup_database
from gateway import UrlGateway
from datetime import datetime

# responce = requests.get('https://register.start.bg/')
def func():
    setup_database()
    gate = UrlGateway()
    gate.update_table_with_url_data('https://www.start.bg/')
    responce = requests.get('https://www.start.bg/')
    responce.encoding = 'utf-8'
    content = responce.content
    soup = BeautifulSoup(content, 'html.parser')
    links = soup.find_all('a')
    count = 0
    # reg = "href=\"http[" + ''.join(string.printable) + "]*'.'bg[" + ''.join(string.printable) + "]*\""
    reg = re.compile("href=\"http[" + ''.join(string.printable) + "]*\.bg/")
    distinct_page_links = set([])
    for link in links:
        search_result = reg.search(str(link))
        if bool(search_result):
            link_addr = search_result.group(0).split('\"')[1].split('/')
            l = ''.join(link_addr[:3]) + '/'
            link_without_www = re.sub('www.', '', l)
            # distinct_page_links.add(re.sub('www.', '', l))
            gate.update_table_with_url_data(link_without_www)

    gate.set_datetime_visited('https://www.start.bg/', datetime.now())
    gate.close()
# count = 1
# for link in distinct_page_links:
#     print(f'{count}. {link}')
#     count += 1


if __name__ == '__main__':
    func()
    gate = UrlGateway()
    print(gate.select_first_non_visited().content)
