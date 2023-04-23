from flask import jsonify, request
from flask_restx import Resource,Namespace
from model.User import User
from sqlalchemy import String
from sqlalchemy.orm import sessionmaker
from database.db_setup import engine, Users,sessionClass
UserAPI = Namespace('user', description='users management')

@UserAPI.route('/')
class GeneralUserOps(Resource):
    @UserAPI.doc(description = "Register a new user",params={'name':'Users name',
                                                             'email': 'Users email',
                                                             'login': 'Users login',
                                                             'password' : 'Users password'})
    def post(self):
        try:
            name = request.args['name']
            email = request.args['email']   # add email verification
            login = request.args['login']   # check if it is free
            password = request.args['password']
        except:
            data = request.get_json()
            name = data['name']
            email = data['email']
            login = data['login']
            password = data['password']
        user = User(name, email, login, password)
        if user.addUser():
            return jsonify(user)
        else:
            return jsonify("User can not be added")

    @UserAPI.doc(description = "Get all users")
    def get(self):
        session = sessionClass()
        res = session.query(Users).all()
        return jsonify(res)


@UserAPI.route('/<user_id>')
class SpecificUserOps(Resource):
    @UserAPI.doc(description = "Getting user by id")
    def get(self, user_id):
        session = sessionClass()
        res = session.query(Users).filter(Users.c.id == user_id)
        c = list(res)
        if len(c) != 0:
            return jsonify(res)
        return jsonify("User was not found")





