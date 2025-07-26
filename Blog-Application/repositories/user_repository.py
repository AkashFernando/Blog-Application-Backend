from models.user_model import User
from database import db

class UserRepository:
    @staticmethod
    def get_all():
        return User.query.all()

    @staticmethod
    def get_by_id(user_id):
        return User.query.get(user_id)

    @staticmethod
    def create(username,email,password):
        user = User(username=username,email=email,password=password)
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def update(user_id,username,email,password):
        user = User.query.get(user_id)
        if user:
            user.username = username
            user.email = email
            user.password = password

            db.session.commit()
        return user

    @staticmethod
    def delete(user_id):
        user = User.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
        return user
