from flask import jsonify
import sqlalchemy
from database.db_setup import sessionClass, Users
from model.User import User


def getUser(user_id):
    session = sessionClass()
    res = session.query(Users).filter(Users.c.id == user_id)
    session.close()
    c = list(res)[0]
    if len(c) != 0:
        user_id = c[0]
        user = User(*c[1:])
        user.user_id = user_id
        return jsonify(user)
    return jsonify("User was not found")
