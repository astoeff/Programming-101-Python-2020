from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base


class Database:
    def __init__(self):
        self.engine = create_engine(f"sqlite:///database.db")
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    # def add(self, row):
    #     if isinstance(row, list):
    #         self.session.add_all(row)
    #     else:
    #         self.session.add(row)
    #     self.commit()

    def commit(self):
        self.session.commit()

    def close(self):
        self.session.close()

    def create(self):
        Base.metadata.create_all(self.engine)