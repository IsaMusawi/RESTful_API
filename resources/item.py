from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

from models.item import ItemModel


class ItemGET(Resource):
    # Initial Parsing for price data
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help="This field cannot be left blank"
    )
    parser.add_argument('store_id',
        type=int,
        required=True,
        help="This field cannot be left blank"
    )
      
    @jwt_required()
    def get(self, name):
        item = ItemModel.findByname(name)
        if item:
            return item.json()
        else:
            return {"message": "Item not found"}, 404

    @jwt_required()
    def delete(self, name):
        item = ItemModel.findByname(name)
        if item:
            item.deleteFromDb()            
            return {'message': "An item with name '{}' has been deleted.".format(name)}, 200
        return {'message': "An item not found"}, 404


class ItemPOST(Resource):
    # Initial Parsing for price data
    parser = reqparse.RequestParser()
    parser.add_argument('name',
        type=str,
        required=True,
        help="This field cannot be left blank"
    )
    parser.add_argument('price',
        type=float,
        required=True,
        help="This field cannot be left blank"
    )
    parser.add_argument('store_id',
        type=int,
        required=True,
        help="This field cannot be left blank"
    )

    @jwt_required()
    def post(self):
        data = ItemPOST.parser.parse_args()      
        if ItemModel.findByname(data['name']):
            return{"message": "An item with name '{}' already exists.".format(data['name'])}, 400            
        
        item = ItemModel(**data)
        
        try:
            item.saveToDb()
        except:
            return {"message": "Error when input data"}, 500
        return item.json(), 201 #201 is status code

    @jwt_required()
    def put(self):
        data = ItemPOST.parser.parse_args()
        item = ItemModel.findByname(data['name'])

        if item is None:
            item = ItemModel(**data)
        else:
            item.price = data['price']
            item.store_id = data['store_id']
        
        item.saveToDb()
        return item.json()


class ItemList(Resource):
    @jwt_required()
    def get(self):
        return {"item": list(map(lambda x: x.json(), ItemModel.getAll()))}
        #return {"items": [item.json() for item in ItemModel.getAll()]}
