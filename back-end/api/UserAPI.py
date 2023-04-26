from flask import jsonify, request
from flask_restx import Resource, Namespace
from model.User import User
from sqlalchemy import String
from sqlalchemy.orm import sessionmaker
from database.db_setup import engine, Users, sessionClass

UserAPI = Namespace('user', description='users management')


@UserAPI.route('/')
class GeneralUserOps(Resource):
    @UserAPI.doc(description="Register a new user", params={'name': 'Users name',
                                                            'email': 'Users email',
                                                            'login': 'Users login',
                                                            'password': 'Users password'})
    def post(self):
        try:
            name = request.args['name']
            email = request.args['email']  # add email verification
            login = request.args['login']  # check if it is free
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
    # @UserAPI.doc(description="Get user by login")
    # def get(self, login):
    #     session = sessionClass()
    #     res = session.query(Users).filter(Users.c.login == login)
    #     return jsonify(res)


@UserAPI.route('/<user_id>')
class SpecificUserOps(Resource):
    @UserAPI.doc(description="Getting user by id")
    def get(self, user_id):
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


# @UserAPI.route('/<login>')
# class Login(Resource):
#     @UserAPI.doc(description="Get user by login")
#     def get(self, login):
#         session = sessionClass()
#         res = session.query(Users).filter(Users.c.login == login)
#         response = jsonify(res)
#         # response.headers.add('Access-Control-Allow-Origin', 'http://localhost:3000')
#         # response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
#         # response.headers.add('Access-Control-Allow-Methods', 'GET, OPTIONS')
#         # response.headers.add('Access-Control-Allow-Credentials', 'true')
#         return response


@UserAPI.route('/signin')
class SignIn(Resource):
    @UserAPI.doc(description = "Users sign in", params = {'login': 'user login','password':'password'})
    def post(self):
        try:
            data = request.get_json()
            login_input = data['login']
            password_input = data['password']
        except:
            login_input = request.args['login']
            password_input = request.args['password']
        session = sessionClass()
        res = session.query(Users).filter(Users.c.login == login_input)[0]
        password = res[4]
        #return password
        if password == password_input:
            return jsonify(res[0])
        else:
            return jsonify({'authenticated':False})

