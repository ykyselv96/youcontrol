from typing import List

from db.models import User
from sqlalchemy import select, insert, update, delete
from fastapi import status, HTTPException, Request
from schemas.user_schema import UsersResponse, SignupForm


class UserCrud:
    def __init__(self, db):
        self.db = db

    async def if_user_in_db_by_username(self, username) -> UsersResponse:
        statement = select(User).where(User.username == username)
        result = await self.db.execute(statement=statement)
        user_in_db = result.scalars().first()

        if user_in_db:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail='There is already another user with this username',
            )

    async def if_user_in_db(self, payload: SignupForm) -> UsersResponse:

        await self.if_user_in_db_by_username(username=payload.username)

        statement = select(User).where(User.email == payload.email)
        result = await self.db.execute(statement=statement)
        user_in_db = result.scalars().first()

        if user_in_db:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail='There is already another user with this email',
            )


    async def add_new_user(self, payload: SignupForm) -> UsersResponse:

        await self.if_user_in_db(payload=payload)

        obj_in = User(**payload.dict(exclude={'password_repeat'}))

        self.db.add(obj_in)
        await self.db.commit()
        return UsersResponse.from_orm(obj_in)

    async def get_all(self) -> List[UsersResponse]:
        db_result = await self.db.execute(select(User))
        return db_result.scalars().all()

    async def get_user_by_id(self, user_id: int) -> UsersResponse:
        statement = select(User).where(User.id == user_id)
        db_result = await self.db.execute(statement)
        user = db_result.scalars().first()

        if not user:
            raise HTTPException(status_code=404, detail="User_not_found")

        return UsersResponse.from_orm(user)

    async def delete_user(self, user_id: int) -> UsersResponse:

        user_in_db = await self.get_user_by_id(user_id=user_id)
        statement = delete(User).where(User.id == user_id)
        await self.db.execute(statement=statement)
        await self.db.commit()
        return user_in_db
