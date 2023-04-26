from flask import jsonify, request
from flask_restx import Resource, Namespace
from model.Project import Project


ProjectAPI = Namespace('project', description='project management')

@ProjectAPI.route('/')
class GeneralProjOps(Resource):
    @ProjectAPI.doc(description = "Post a new project", params = {'name':'Project name',
                                                                  'start-date':'Start date',
                                                                  'end-date':'End date'})
    def post(self):
        try:
            data = request.args
        except:
            data = request.get_json()
        name = data['name']
        start_date = data['start-date']
        end_date = data['end-date']
        project = Project(name,start_date,end_date)
        if project.AddProject():
            return jsonify(project)
        else:
            return jsonify("Project can not be added")