from sqlalchemy import (Column, Integer, String, DateTime)
# from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

# from email.utils import parseaddr
# from re import compile, match

Base = declarative_base()


class Url(Base):
    __tablename__ = 'url'
    id = Column(Integer, primary_key=True)
    content = Column(String, unique=True)
    # email = Column(String, unique=True)
    # password = Column(String)
    # salt = Column(String)
    visited = Column(DateTime, nullable=True)

    def __str__(self):
        return f'{self.id} | {self.username} | {self.email} | {self.password}'
