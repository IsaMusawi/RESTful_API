from flask import jsonify
from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):
    def get(self, name):
        store = StoreModel.findByname(name)
        if store:
            result = store.json(), 201
        else:
            result = {"message": "Store not found"}, 404

        return result

    def post(self, name):
        if StoreModel.findByname(name):
            return {"message": "Store with name {} is exits".format(name)}

        store = StoreModel(name)
        store.saveToDb()
        return store.jsonpost()

    def delete(self, name):
        store = StoreModel.findByname(name)
        if store:
            store.deleteFromDb()
            result = {"message": "Store with name {} has been deleted".format(name)}, 201
        else:
            result = result = {"message": "Store not found"}, 404

        return result


class StoreList(Resource):
    def get(self):
        return {"stores": [store.json() for store in StoreModel.getAll()]}