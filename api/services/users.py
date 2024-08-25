from typing import List, Optional

from api.domain.users import User
from api.repositories.users import UserRepository


class UserService:

    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def get_all_users(self) -> List[dict]:
        return self.user_repository.get_all()

    def get_user_by_id(self, user_id: str) -> User:
        return self.user_repository.get(user_id)

    def create_user(self, user: User) -> bool:
        return self.user_repository.create(user.dict(by_alias=True))

    def delete_user(self, user_id: str) -> bool:
        return self.user_repository.delete(user_id)

    def get_user_by_email(self, email: str) -> Optional[User]:
        return self.user_repository.get_by_email(email)
