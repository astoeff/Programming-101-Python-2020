from sqlalchemy import (Column, Integer, String, DateTime, Boolean)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Url(Base):
    __tablename__ = 'url'
    id = Column(Integer, primary_key=True)
    content = Column(String, unique=True)
    visited = Column(DateTime, nullable=True)
    processing = Column(Boolean, default=False)

    def __str__(self):
        return f'{self.id} | {self.content} | {self.visited}'
