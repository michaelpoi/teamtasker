from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///database/teamtasker.db')
meta = MetaData()
Users = Table('Users', meta,
              Column('id', String, primary_key=True),
              Column('name', String),
              Column('email', String),
              Column('login', String),
              Column('password', String))
meta.create_all(engine)
sessionClass = sessionmaker(bind=engine)