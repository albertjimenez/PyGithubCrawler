from flask_restful import Resource


class BasicController(Resource):
    def get(self):
        return {'hello': 'world'}
