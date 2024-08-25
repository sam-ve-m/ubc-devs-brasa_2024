from abc import ABC
from typing import List

from pymongo import MongoClient


class AbstractRepository(ABC):

    def __init__(self, connection_string: str, database_name: str, collection_name: str):
        self.client = MongoClient(connection_string)
        self.db = self.client[database_name]
        self.collection = self.db[collection_name]

    def get_all(self) -> List[dict]:
        return list(self.get_many_by_filter({}))

    def get_many_by_filter(self, mongo_filter: dict) -> list:
        return list(self.collection.find(mongo_filter))

    def get_by_filter(self, mongo_filter: dict) -> dict:
        return self.collection.find_one(mongo_filter)

    def get_by_field(self, value, field="_id") -> dict:
        return self.get_by_filter({field: value})

    def create(self, user: dict) -> bool:
        result = self.collection.insert_one(user)
        return bool(self.get_by_field(result.inserted_id))

    def create_many(self, users_data: List[dict]) -> bool:
        result = self.collection.insert_many(users_data)
        return bool(result.inserted_ids)

    def update(self, user_id, user: dict) -> bool:
        self.collection.update_one({"_id": user_id}, {"$set": user})
        return bool(self.get_by_field(user_id))

    def delete(self, user_id) -> bool:
        result = self.collection.delete_one({"_id": user_id})
        return result.deleted_count > 0
