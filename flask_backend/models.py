from sqlalchemy import (
    create_engine,
    ForeignKey,
    Column,
    String,
    Integer,
    CHAR,
    BOOLEAN,
    DateTime,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import datetime
from rich.traceback import install

install()

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    name = Column("name", String)

    def __init__(self, user_id, name):
        self.id = user_id
        self.name = name

    def __repr__(self):
        return f"({self.name})"


class Todo(Base):
    __tablename__ = "todos"

    todo_id = Column(Integer, primary_key=True)
    todo_text = Column(String)
    todo_date = Column(DateTime, default=datetime.datetime.now)

    def __init__(
        self,
        # todo_id,
        todo_text,
    ):
        # self.todo_id = todo_id
        self.todo_text = todo_text
        # self.date = todo_date

    def __repr__(self):
        return f"({self.todo_text})"


engine = create_engine("sqlite:///database.db", pool_pre_ping=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()
