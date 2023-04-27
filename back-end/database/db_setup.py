from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, DateTime, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
engine = create_engine('sqlite:///database/teamtasker.db')
meta = MetaData()
Users = Table('Users', meta,
              Column('id', String, primary_key=True),
              Column('name', String),
              Column('email', String),
              Column('login', String),
              Column('password', String))
Projects = Table('Projects', meta,
                 Column('id', String, primary_key=True),
                 Column('name', String),
                 Column('desc', String),
                 Column('start_date', DateTime),
                 Column('end_date', DateTime))
WorkFor = Table('Projects-Users', meta,
                Column('user_id', String, ForeignKey('Users.id')),
                Column('project_id', String, ForeignKey('Projects.id')),
                Column('role', String),
                PrimaryKeyConstraint('user_id', 'project_id'))
Tasks = Table('Tasks', meta,
              Column('task_id', String, primary_key=True),
              Column('name', String),
              Column('desc', String),
              Column('role', String),
              Column('project_id', ForeignKey('Projects.id')))
meta.create_all(engine)
sessionClass = sessionmaker(bind=engine)
Base = declarative_base()