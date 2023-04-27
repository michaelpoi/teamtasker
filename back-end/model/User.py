import uuid
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String
from database.db_setup import engine, Users, WorkFor,Base





class User(Base):
    __tablename__ = 'Users'
    user_id = Column(String, primary_key=True)
    email = Column(String)
    name = Column(String)
    login = Column(String)
    password = Column(String)

    def __init__(self, name, email, login, password):
        self.user_id = str(uuid.uuid4())
        self.name = str(name)
        self.email = str(email)
        self.login = str(login)
        self.password = str(password)

    def addUser(self):
        conn = engine.connect()
        statement = Users.insert().values(id=self.user_id,
                                          name=self.name,
                                          email=self.email,
                                          login=self.login,
                                          password=self.password)
        try:
            conn.execute(statement)
            conn.commit()
            return True
        except:
            print(type(self.password))
            return False
        finally:
            conn.close()
