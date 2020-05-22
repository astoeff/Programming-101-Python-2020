# import sqlalchemy
# from sqlalchemy.orm import sessionmaker
from models import Url
from gateway import UrlGateway
import random
import string
from setup_database import setup_database


if __name__ == '__main__':
    setup_database()
    while True:
        letters = string.ascii_lowercase
        for i in range(20):
            urls = []
            urls.append(''.join(random.choice(letters) for j in range(8)))

        gate = UrlGateway()
        for i in range(len(urls)):
            gate.update_table_with_url_data(urls[i])
        gate.close()