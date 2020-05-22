from gateway import UrlGateway
import sys
import datetime


def get_statistics(start, end):
    gate = UrlGateway()
    data = gate.select_by_datetime(start, end)
    urls = [url.content for url in data]
    gate.close()
    return urls


if __name__ == '__main__':
    start = datetime.datetime.strptime(sys.argv[1] + ' ' + sys.argv[2], '%Y-%m-%d %X')
    end = datetime.datetime.strptime(sys.argv[3] + ' ' + sys.argv[4], '%Y-%m-%d %X')
    assert start < end
    urls = get_statistics(start, end)
    for url in urls:
        print(url)
