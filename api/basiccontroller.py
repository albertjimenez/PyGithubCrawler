from flask_restful import Resource
from api.api_request_connector import APIRequestConnector

class BasicController(Resource):

    def __init__(self) -> None:
        super().__init__()
        self.api_request_connector = APIRequestConnector()

    def get(self):
        return {'hello': 'world'}
