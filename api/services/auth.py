from datetime import datetime, timedelta

import argon2
from jose import jwt, JWTError
from fastapi import HTTPException, status
from argon2 import PasswordHasher
from typing import Optional

from api.services.users import UserService


class AuthService:
    def __init__(
            self,
            secret_key: str,
            algorithm: str,
            access_token_expire_minutes: int,
            user_service: UserService,
    ):
        self.secret_key = secret_key
        self.algorithm = algorithm
        self.access_token_expire_minutes = access_token_expire_minutes
        self.user_service = user_service
        self.ph = PasswordHasher()

    def authenticate_user(self, username: str, password: str) -> Optional[str]:
        user = self.user_service.get_user_by_email(username)

        if not user:
            return
        if not self.verify_password(password, user.hashed_password):
            return
        return self.create_access_token({"sub": user.user_id})

    def create_access_token(self, data: dict) -> str:
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(minutes=self.access_token_expire_minutes)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, self.secret_key, algorithm=self.algorithm)
        return encoded_jwt

    def verify_password(self, plain_password, hashed_password) -> bool:
        try:
            self.ph.verify(hashed_password, plain_password)
            return True
        except argon2.exceptions.VerifyMismatchError:
            return False

    def hash_password(self, password: str):
        return self.ph.hash(password)

    def verify_token(self, token: str) -> str:
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
            user_id: str = payload.get("sub")  # Assuming 'sub' claim holds user ID
            if user_id is None:
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication credentials")
            return user_id
        except JWTError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication credentials")
