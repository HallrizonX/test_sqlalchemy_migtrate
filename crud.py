import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import DATABASE_URI
from models import Base, Book

engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

def recreate_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    #Base.metadata.create_all(engine)
    #recreate_database()

    book = Book(
        title='Deep Learning',
        author='Ian Goodfellow',
        pages=775,
        published=datetime.datetime(2016, 11, 18)
    )
    session.add(book)
    session.commit()

    print(session.query(Book).all())