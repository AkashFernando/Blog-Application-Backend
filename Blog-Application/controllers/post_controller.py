from flask import request, jsonify
from ..services.post_service import PostService

post_service = PostService()

def register_post_routes(app):
    @app.route('/posts', methods=['GET'])
    def get_all_posts():
        posts = post_service.get_all_posts()
        return jsonify([post.to_dict() for post in posts]), 200

    @app.route('/posts/<int:post_id>', methods=['GET'])
    def get_post(post_id):
        post = post_service.get_post_by_id(post_id)
        if post:
            return jsonify(post.to_dict()), 200
        return jsonify({'message': 'Post not found'}), 404

    @app.route('/posts', methods=['POST'])
    def create_post():
        data = request.get_json()
        title = data.get('title')
        content = data.get('content')
        post = post_service.create_post(title, content)
        return jsonify(post.to_dict()), 201

    @app.route('/posts/<int:post_id>', methods=['PUT'])
    def update_post(post_id):
        data = request.get_json()
        title = data.get('title')
        content = data.get('content')
        post = post_service.update_post(post_id, title, content)
        if post:
            return jsonify(post.to_dict()), 200
        return jsonify({'message': 'Post not found'}), 404

    @app.route('/posts/<int:post_id>', methods=['DELETE'])
    def delete_post(post_id):
        post = post_service.delete_post(post_id)
        if post:
            return jsonify({'message': 'Post deleted'}), 200
        return jsonify({'message': 'Post not found'}), 404
