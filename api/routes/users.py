from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer

from api.routes.dependencies import get_user_service, get_auth_service
from api.domain.users import User
from api.services.auth import AuthService
from api.services.users import UserService

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


@router.get("/users")
def get_all_users(user_service: UserService = Depends(get_user_service)):
    return user_service.get_all_users()


@router.post("/user")
def create_user(
        user: User,
        auth_service: AuthService = Depends(get_auth_service),
        user_service: UserService = Depends(get_user_service),
):
    user.hashed_password = auth_service.hash_password(user.hashed_password)
    success = user_service.create_user(user)
    return {"Success": success}


@router.get("/user", response_model=User)
def get_user_by_id(
        token: str = Depends(oauth2_scheme),
        auth_service: AuthService = Depends(get_auth_service),
        user_service: UserService = Depends(get_user_service),
) -> User:
    user_id = auth_service.verify_token(token)
    return user_service.get_user_by_id(user_id)


@router.delete("/user")
def delete_user(
        token: str = Depends(oauth2_scheme),
        auth_service: AuthService = Depends(get_auth_service),
        user_service: UserService = Depends(get_user_service),
):
    user_id = auth_service.verify_token(token)
    success = user_service.delete_user(user_id)
    return {"Success": success}


__all__ = router,
