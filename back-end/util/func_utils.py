from flask import jsonify
from database.db_setup import sessionClass
from model import User
def getUserByLogin(login):
    session = sessionClass()
    res = session.query(Users).filter(Users.c.login == login)
    response = jsonify(res)
    return response


getUserByLogin('michael')