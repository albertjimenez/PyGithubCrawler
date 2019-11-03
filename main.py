from flask import Flask
from flask_restful import Api

from api.basiccontroller import BasicController
from api.extracontroller import ExtraController

app = Flask(__name__)
api = Api(app)

api.add_resource(BasicController, '/')
api.add_resource(ExtraController, '/extra')

# TODO diccionario con key clase - ruta

if __name__ == '__main__':
    app.run(debug=True)
