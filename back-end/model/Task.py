from datetime import datetime
import uuid

from database.db_setup import Tasks, sessionClass, Base, Projects,engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String, ForeignKey, DateTime,Boolean

class Task(Base):
    __tablename__ = 'Tasks'
    task_id = Column(String, primary_key=True)
    name = Column(String)
    desc = Column(String)
    role = Column(String)
    end_date = Column(DateTime)
    is_done = Column(Boolean)
    project_id = Column(String, ForeignKey(Projects.c.id))

    def __init__(self, name, desc,role,end_date,project_id):
        date_format = '%d.%m.%Y'
        self.task_id = str(uuid.uuid4())
        self.name = name
        self.desc = desc
        self.role = role
        self.end_date = datetime.strptime(end_date,date_format)
        self.is_done = False
        self.project_id = project_id

    def CreateTask(self):
        conn = engine.connect()
        statement = Tasks.insert().values(task_id = self.task_id,
                                          name = self.name,
                                          desc = self.desc,
                                          role = self.role,
                                          end_date = self.end_date,
                                          is_done = self.is_done,
                                          project_id = self.project_id)

        try:

            conn.execute(statement)
            conn.commit()
            return True
        except:
            return False
        finally:
            conn.close()


