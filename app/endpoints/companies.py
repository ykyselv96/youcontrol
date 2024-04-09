from typing import List

from fastapi import APIRouter, status, Depends

from core.connections import async_session
from crud.company_crud import CompanyCrud

from core.connections import get_session
from schemas.company_schema import CompanyCreationForm, CompaniesResponse

router = APIRouter(tags=["company crud"])



# TODO add typing and schemas

@router.post("/company/", status_code=status.HTTP_200_OK, response_model = CompaniesResponse)
async def add_new_company(payload: CompanyCreationForm, db=Depends(get_session)) -> CompaniesResponse:

    comp_crud = CompanyCrud(db=db)
    res = await comp_crud.post_company(payload=payload)
    return res



@router.get("/company/", status_code=status.HTTP_200_OK, response_model = List[CompaniesResponse])
async def get_all_users(db=Depends(get_session)) -> List[CompaniesResponse]:

    comp_crud = CompanyCrud(db=db)
    res = await comp_crud.get_all()

    return res














@router.get("/users/{user_id}", status_code=status.HTTP_200_OK)
async def get_user_by_id(user_id: int, db=Depends(get_session)):

    comp_crud = CompanyCrud(db=db)
    res = await comp_crud.get_user_by_id(user_id=user_id)
    return res


