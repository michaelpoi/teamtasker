from flask import Flask
from flask_restx import Api
from flask_cors import CORS
from util.json_utils import AppJsonEncoder
from api.UserAPI import UserAPI
from api.ProjectAPI import ProjectAPI
from api import GroupAPI

TeamTasker = Flask(__name__)
CORS(TeamTasker,supports_credentials=True,origins='*',methods=['GET', 'POST', 'PUT', 'DELETE'], headers=['Content-Type', 'Authorization' ])

TeamTasker.json_encoder = AppJsonEncoder
TeamTaskerApi = Api(TeamTasker, version='1.0', title='TeamTasker',
                    contact_email="22IMC1028@fh-krems.ac.at",
                    description='TeamTasker')

TeamTaskerApi.add_namespace(UserAPI)
TeamTaskerApi.add_namespace(ProjectAPI)
# TeamTaskerApi.add_namespace(GroupAPI)
# TeamTaskerApi.add_namespace(TaskApi)

if __name__ == "__main__":
    TeamTasker.run(debug=True, port=5000)
