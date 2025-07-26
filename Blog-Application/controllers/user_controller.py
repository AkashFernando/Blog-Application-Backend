from flask import request, jsonify
from services.user_service import UserService

user_service = UserService()

def register_user_routes(app):
    @app.route('/users', methods=['GET'])
    def get_all_users():
        users = user_service.get_all_users()
        return jsonify([user.to_dict() for user in users]), 200

    @app.route('/users/<int:user_id>', methods=['GET'])
    def get_user(user_id):
        user = user_service.get_user_by_id(user_id)
        if user:
            return jsonify(user.to_dict()), 200
        return jsonify({'message': 'User not found'}), 404

    @app.route('/users', methods=['POST'])
    def create_user():
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        user = user_service.create_user(username,email,password)
        return jsonify(user.to_dict()), 201

    @app.route('/users/<int:user_id>', methods=['PUT'])
    def update_user(user_id):
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        user = user_service.update_user(user_id, username,email,password)
        if user:
            return jsonify(user.to_dict()), 200
        return jsonify({'message': 'User not found'}), 404

    @app.route('/users/<int:user_id>', methods=['DELETE'])
    def delete_user(user_id):
        user = user_service.delete_user(user_id)
        if user:
            return jsonify({'message': 'User deleted'}), 200
        return jsonify({'message': 'User not found'}), 404
