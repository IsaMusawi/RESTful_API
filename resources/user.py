from flask_restful import Resource, reqparse
from models.user import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help="This field cannot be left blank"
    )
    parser.add_argument('password',
        type=str,
        required=True,
        help="This field cannot be left blank"
    )

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.findByUsername(data['username']):
            return{"message": "An user with username '{}' already exists.".format(data['username'])}, 400            
      
        #user = UserModel(data['username'], data['password']) -> same with below
        user = UserModel(**data)

        user.saveToDb()

        return {"message": "User created successfully"}, 200



