from flask import jsonify, request
from flask_restx import Resource, Namespace
from model.Project import Project
from model.Task import Task


ProjectAPI = Namespace('project', description='project management')

@ProjectAPI.route('/')
class GeneralProjOps(Resource):
    @ProjectAPI.doc(description = "Post a new project", params = {'name':'Project name',
                                                                  'desc': 'Project description',
                                                                  'start-date':'Start date',
                                                                  'end-date':'End date',
                                                                  'user_id':'Creator id'})
    def post(self):
        try:
            data = request.args
        except:
            data = request.get_json()
        name = data['name']
        desc = data['desc']
        start_date = data['start-date']
        end_date = data['end-date']
        creator = data['user_id']
        project = Project(name,desc,start_date,end_date, creator)
        if project.AddProject():
            return jsonify(project)
        else:
            return jsonify("Project can not be added")

@ProjectAPI.route('/<project_id>/tasks')
class TaskManagment(Resource):
    @ProjectAPI.doc(description = "Add new task", params = {'name':'Task name',
                                                            'desc':'Task description',
                                                            'role':'Users role'})
    def post(self,project_id):
        try:
            data = request.args
        except:
            data = request.get_json()

        name = data['name']
        desc = data['desc']
        role = data['role']
        task = Task(name,desc,role,project_id)
        task.CreateTask()
        keys = ['project_id', 'name', 'desc', 'role']
        return jsonify(task)


