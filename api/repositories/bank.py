from api.repositories.abs.abs_mongo import AbstractRepository
from api.domain.users import User


class BankRepository(AbstractRepository):

    def is_empty(self) -> bool:
        return not bool(self.collection.find_one({}))
