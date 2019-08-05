from sqlalchemy import create_engine, Table, Column, Integer, MetaData, ForeignKey, String

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql+psycopg2://postgres:postgres@127.0.0.1:6543/CUSTOMARY')
Session = sessionmaker(bind=engine)
session = Session()
# -----------------------------------------
Base = declarative_base()
meta = MetaData()


Account = Table(
    'account', meta,
    Column('id', Integer, primary_key=True),
    Column('login', String(40)),
    Column('passwd', String(40)),
)

if __name__ == "__main__":
    Account.create()
    #ed_user = User(name='ed', password='12345')
    #session.add(ed_user)
    #session.commit()
