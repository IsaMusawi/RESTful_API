import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import ItemGET,ItemPOST, ItemList
from resources.store import Store, StoreList
import psycopg2
from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db') #'postgresql://postgres:vaizaado154@localhost/RESTUdemy'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'musawi'
api = Api(app)

@app.before_first_request
def createTables():
    db.create_all()

jwt = JWT(app, authenticate, identity) # /auth

api.add_resource(ItemGET, '/item/<string:name>')
api.add_resource(ItemPOST, '/item')
api.add_resource(ItemList, '/items')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)
