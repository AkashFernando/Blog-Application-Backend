from repositories.user_repository import UserRepository

class UserService:
    def get_all_users(self):
        return UserRepository.get_all()

    def get_user_by_id(self, user_id):
        return UserRepository.get_by_id(user_id)

    def create_user(self, username,email,password):
        return UserRepository.create(username,email,password)

    def update_user(self, user_id,username,email,password):
        return UserRepository.update(user_id,username,email,password)

    def delete_user(self, user_id):
        return UserRepository.delete(user_id)
