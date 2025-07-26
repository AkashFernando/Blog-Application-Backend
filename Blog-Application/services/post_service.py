from ..repositories.post_repository import PostRepository

class PostService:
    def get_all_posts(self):
        return PostRepository.get_all()

    def get_post_by_id(self, post_id):
        return PostRepository.get_by_id(post_id)

    def create_post(self, title, content):
        return PostRepository.create(title, content)

    def update_post(self, post_id, title, content):
        return PostRepository.update(post_id, title, content)

    def delete_post(self, post_id):
        return PostRepository.delete(post_id)
