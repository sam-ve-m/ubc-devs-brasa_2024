from decouple import config
from fastapi import Depends

from api.repositories.users import UserRepository
from api.services.auth import AuthService
from api.services.users import UserService
from api.repositories.bank import BankRepository
from api.repositories.mcc import MCCRepository
from api.repositories.sales import SalesRepository


def get_user_service() -> UserService:
    repository = UserRepository(
        connection_string=config("MONGO_USERS_CONNECTION_STRING"),
        database_name=config("MONGO_USERS_DATABASE"),
        collection_name=config("MONGO_USERS_COLLECTION")
    )
    service = UserService(repository)
    return service


def get_auth_service(user_service: UserService = Depends(get_user_service)) -> AuthService:
    service = AuthService(
        secret_key=config("AUTH_SECRET_KEY"),
        algorithm=config("AUTH_ALGORITHM"),
        access_token_expire_minutes=int(config("AUTH_ACCESS_TOKEN_EXPIRE_MINUTES")),
        user_service=user_service,
    )
    return service


def get_sales_repository() -> SalesRepository:
    repository = SalesRepository(
        connection_string=config("MONGO_SALES_CONNECTION_STRING"),
        database_name=config("MONGO_SALES_DATABASE"),
        collection_name=config("MONGO_SALES_COLLECTION")
    )
    return repository


def get_bank_repository() -> BankRepository:
    repository = BankRepository(
        connection_string=config("MONGO_BANK_CONNECTION_STRING"),
        database_name=config("MONGO_BANK_DATABASE"),
        collection_name=config("MONGO_BANK_COLLECTION")
    )
    return repository


def get_m_c_c_repository() -> MCCRepository:
    repository = MCCRepository(
        connection_string=config("MONGO_MCC_CONNECTION_STRING"),
        database_name=config("MONGO_MCC_DATABASE"),
        collection_name=config("MONGO_MCC_COLLECTION")
    )
    return repository
