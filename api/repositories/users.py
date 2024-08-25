from api.repositories.abs.abs_mongo import AbstractRepository
from api.domain.users import User


class UserRepository(AbstractRepository):

    def get_by_email(self, email: str) -> User:
        if user := self.get_by_field(email, "email"):
            user = User(**user)
            return user

    def get(self, user_id: str) -> User:
        if user := self.get_by_field(user_id):
            user = User(**user)
            return user
