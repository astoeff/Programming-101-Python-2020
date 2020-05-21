import requests
from bs4 import BeautifulSoup
import re
import string
from setup_database import setup_database
from gateway import UrlGateway
from datetime import datetime
from sqlalchemy.exc import OperationalError


def find_all_links_of_url_html_content(url):
    responce = requests.get(url)
    responce.encoding = 'utf-8'
    content = responce.content
    content_in_html = BeautifulSoup(content, 'html.parser')
    links = content_in_html.find_all('a')
    return links


def get_links_of_url(url, reg):
    links = find_all_links_of_url_html_content(url)
    for link in links:
        search_result = reg.search(str(link))
        if bool(search_result):
            link_addr = search_result.group(0).split('\"')[1].split('/')
            l = link_addr[0] + '//' + link_addr[2]
            link_without_www = re.sub('www.', '', l)
            gate = UrlGateway()
            gate.update_table_with_url_data(link_without_www)
            gate.close()

    gate = UrlGateway()
    gate.set_datetime_visited(url, datetime.now())
    gate.close()


if __name__ == '__main__':
    reg = re.compile("href=\"http[" + ''.join(string.printable) + "]*\.bg/")
    while True:
        try:
            setup_database()
            while True:
                gate = UrlGateway()
                url_content = gate.select_first_non_visited_and_not_processing().content
                gate.set_true_processing(url_content)
                try:
                    get_links_of_url(url_content, reg)
                    print('OK')
                except requests.exceptions.ConnectionError:
                    gate.set_datetime_visited(url_content, datetime.now())
                gate.close()
        except OperationalError:
            pass
