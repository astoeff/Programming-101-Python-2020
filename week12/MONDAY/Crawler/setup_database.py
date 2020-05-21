from gateway import UrlGateway
from constants import ROOT_URL


def setup_database():
    gateway = UrlGateway()
    gateway.db.create()
    gateway.update_table_with_url_data(ROOT_URL)
    gateway.db.commit()
    gateway.close()


if __name__ == '__main__':
    setup_database()
