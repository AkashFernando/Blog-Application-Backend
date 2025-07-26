from ..models.post_model import Post
from ..database import db

class PostRepository:
    @staticmethod
    def get_all():
        return Post.query.all()

    @staticmethod
    def get_by_id(post_id):
        return Post.query.get(post_id)

    @staticmethod
    def create(title, content):
        post = Post(title=title, content=content)
        db.session.add(post)
        db.session.commit()
        return post

    @staticmethod
    def update(post_id, title, content):
        post = Post.query.get(post_id)
        if post:
            post.title = title
            post.content = content
            db.session.commit()
        return post

    @staticmethod
    def delete(post_id):
        post = Post.query.get(post_id)
        if post:
            db.session.delete(post)
            db.session.commit()
        return post
