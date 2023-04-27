import uuid

from database.db_setup import Tasks, sessionClass, Base, Projects
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String, ForeignKey

class Task(Base):
    __tablename__ = 'Tasks'
    task_id = Column(String, primary_key=True)
    name = Column(String)
    desc = Column(String)
    role = Column(String)
    project_id = Column(String, ForeignKey(Projects.c.id))

    def __init__(self, name, desc,role,project_id):
        self.task_id = str(uuid.uuid4())
        self.name = name
        self.desc = desc
        self.role = role
        self.project_id = project_id

    def CreateTask(self):
        session = sessionClass()
        try:
            session.add(self)
            session.commit()
            return True
        except:
            return False
        finally:
            session.close()


