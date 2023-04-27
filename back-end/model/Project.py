import uuid
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
from database.db_setup import Projects, sessionClass, engine, WorkFor
from datetime import datetime

Base = declarative_base()


class Project(Base):

    __tablename__ = 'Projects'
    project_id = Column(String, primary_key=True)
    name = Column(String)
    desc = Column(String)
    start_date = Column(DateTime)
    end_date = Column(DateTime)

    def __init__(self, name,desc, start_date, end_date,creator):
        date_format = '%d.%m.%Y'
        self.project_id = str(uuid.uuid4())
        self.name = name
        self.desc = desc
        self.start_date = datetime.strptime(start_date, date_format)
        self.end_date = datetime.strptime(end_date, date_format)
        self.creator = creator

    def AddProject(self):
        conn = engine.connect()
        statement = Projects.insert().values(id=self.project_id,
                                             name=self.name,
                                             desc = self.desc,
                                             start_date=self.start_date,
                                             end_date=self.end_date,
                                             )
        statement2 = WorkFor.insert().values(user_id = self.creator,
                                             project_id = self.project_id,
                                             role = "creator")
        try:
            conn.execute(statement)
            conn.execute(statement2)
            conn.commit()
            return True
        except:
            return False
        finally:
            conn.close()
