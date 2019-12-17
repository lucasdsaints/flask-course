from flask_restful import Resource, reqparse

from models.user import UserModel

class UserRegister(Resource):
    parse = reqparse.RequestParser()
    parse.add_argument('username', type=str, required=True, help='This field cannot be blank.')
    parse.add_argument('password', type=str, required=True, help='This field cannot be blank.')
    
    def post(self):
        data = UserRegister.parse.parse_args()

        if UserModel.find_by_username(data['username']):
            return {'message': 'user already exists.'}, 400

        user = UserModel(**data)
        user.save_to_db()
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        # query_insert = 'INSERT INTO users VALUES (NULL, ?, ?)'
        # values = data['username'], data['password']
        # cursor.execute(query_insert, values)
        # connection.commit()
        # connection.close()
        
        return {'message': 'user created successfully'}, 201
