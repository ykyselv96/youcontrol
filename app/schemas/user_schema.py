import bcrypt
from pydantic import BaseModel, Field, ValidationError, validator, root_validator
from typing import Optional, Any

from fastapi import HTTPException, status

from utils.hash_password import hash_password


# from .password_validator import password_validator


class UserInDb(BaseModel):
    id: int
    username: str
    email: str
    password: str
    description: Optional[str]


class UsersResponse(BaseModel):
    id: int
    username: str
    email: str
    description: Optional[str]

    class Config:
        orm_mode = True

class SignInForm(BaseModel):
    email: str
    password: str


class SignupForm(BaseModel):
    username: str
    email: str
    password: str = Field(..., min_length=8)
    password_repeat: str = Field(..., min_length=8)
    description: Optional[str]

    @root_validator  # type: ignore
    def validate_password(cls, model_values: dict[Any, Any]) -> dict[Any, Any]:
        password = model_values.get('password', [])
        password_repeat = model_values.get('password_repeat', [])
        if password != password_repeat:
            raise HTTPException(
                detail="Passwords do not match",
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            )
        hashed_password = hash_password(password)
        model_values['password'] = hashed_password

        return model_values
