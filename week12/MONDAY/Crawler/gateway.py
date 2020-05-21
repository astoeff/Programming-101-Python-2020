from models import Url
from database import Database
from datetime import datetime
from sqlalchemy.exc import IntegrityError


class UrlGateway:
    def __init__(self):
        self.db = Database()

    def search_url_by_content(self, content):
        url = self.db.session.query(Url).\
            filter(Url.content == content).first()
        self.db.commit()
        return url

    def update_table_with_url_data(self, content):
        try:
            self.db.session.add(Url(content=content))
            self.db.commit()
        except IntegrityError:
            self.db.session.rollback()

    def set_datetime_visited(self, content, datetime_visited):
        self.db.session.query(Url).filter(Url.content == content).\
            update({Url.visited: datetime_visited, Url.processing: True})
        self.db.commit()

    def set_true_processing(self, content):
        self.db.session.query(Url).filter(Url.content == content).\
            update({Url.processing: True})
        self.db.commit()

    def select_visited(self):
        url = self.db.session.query(Url).filter(Url.visited.isnot(None)).first()
        self.db.commit()
        return url

    def select_first_non_visited_and_not_processing(self):
        url = self.db.session.query(Url).filter(Url.visited.is_(None), Url.processing.is_(False)).first()
        self.db.commit()
        return url

    def close(self):
        self.db.close()


if __name__ == '__main__':
    g = UrlGateway()
    # g.update_table_with_url_data('https://facebook.com')
    # g.set_datetime_visited('https://facebook.com', datetime.now())
    print(g.select_visited().content)
