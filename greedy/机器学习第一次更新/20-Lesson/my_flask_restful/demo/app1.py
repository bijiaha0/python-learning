__author__ = "zhou"
__date__ = "2019-06-11 20:35"
#
# from flask import Flask
# import flask_restful as restful
#
#
# app = Flask(__name__)
# api = restful.Api(app)
#
# class HelloWorld(restful.Resource):
#     def get(self):
#         return {'hello': 'world'}
#
# api.add_resource(HelloWorld, '/')
#
# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

todos = {
    "todo1": "今天去打球"
}

class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}

class Todo1(Resource):
    def get(self):
        return {"do_something":"唱歌"}

class Todo2(Resource):
    def get(self):
        return {"task":"攻占日本岛"}, 200

api.add_resource(TodoSimple, '/<string:todo_id>')
api.add_resource(Todo1, '/1', '/1/')
api.add_resource(Todo2, '/2')

if __name__ == '__main__':
    app.run(debug=True)

