import uuid
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
from database.db_setup import Projects, sessionClass, engine
from datetime import datetime

Base = declarative_base()


class Project(Base):

    __tablename__ = 'Projects'
    project_id = Column(String, primary_key=True)
    name = Column(String)
    start_date = Column(DateTime)
    end_date = Column(DateTime)

    def __init__(self, name, start_date, end_date):
        date_format = '%d.%m.%Y'
        self.project_id = str(uuid.uuid4())
        self.name = name
        self.start_date = datetime.strptime(start_date, date_format)
        self.end_date = datetime.strptime(end_date, date_format)

    def AddProject(self):
        conn = engine.connect()
        statement = Projects.insert().values(id=self.project_id,
                                             name=self.name,
                                             start_date=self.start_date,
                                             end_date=self.end_date,
                                             )
        try:
            conn.execute(statement)
            conn.commit()
            return True
        except:
            conn.execute(statement)
            return False
        finally:
            conn.close()
