from typing import List

from fastapi import APIRouter, status, Depends, HTTPException

from core.connections import async_session
from crud.user_crud import UserCrud

from core.connections import get_session

from schemas.user_schema import SignupForm, UsersResponse

router = APIRouter(tags=["user crud"])


@router.post("/user/", status_code=status.HTTP_200_OK, response_model=UsersResponse)
async def add_new_user(payload: SignupForm, db=Depends(get_session)) -> UsersResponse:

    user_crud = UserCrud(db=db)
    res = await user_crud.add_new_user(payload=payload)
    return res


@router.get("/user/", status_code=status.HTTP_200_OK, response_model=List[UsersResponse])
async def get_all_users(db=Depends(get_session)) -> List[UsersResponse]:

    user_crud = UserCrud(db=db)
    res = await user_crud.get_all()

    return res


@router.get("/users/{user_id}", status_code=status.HTTP_200_OK, response_model=UsersResponse)
async def get_user_by_id(user_id: int, db=Depends(get_session)) -> UsersResponse:
    user_crud = UserCrud(db=db)
    res = await user_crud.get_user_by_id(user_id=user_id)
    return res







# @router.put("/users/{user_id}", status_code=status.HTTP_200_OK, response_model=UsersResponse)
# async def update_user(payload: User_Update_request_model, user_id: int, db=Depends(get_session)) -> UsersResponse:
#
#     user_handler = UserCrud(db=db)
#
#     # if current_user.id == user_id:
#     res = await user_handler.put_user(payload=payload, user_id=user_id)
#
#     # else:
#     #     raise HTTPException(
#     #         status_code=status.HTTP_403_FORBIDDEN,
#     #         detail="You can't update another users",
#     #     )

    # return res



@router.delete("/users/{user_id}",  status_code=status.HTTP_200_OK, response_model=UsersResponse)
async def delete_user(user_id: int, db=Depends(get_session)) -> UsersResponse:

    user_crud = UserCrud(db=db)

    # if current_user.id == user_id:
    res = await user_crud.delete_user(user_id=user_id)

    # else:
    #     raise HTTPException(
    #         status_code=status.HTTP_403_FORBIDDEN,
    #         detail="You can't delete another users",
    #     )

    return res

