from sqlalchemy import select

from db.models import Company
from schemas.company_schema import CompanyCreationForm, CompaniesResponse


class CompanyCrud:
    def __init__(self, db):
        self.db = db

    async def post_company(self, payload: CompanyCreationForm) -> CompaniesResponse:

        obj_in = Company(**payload.dict())

        self.db.add(obj_in)

        await self.db.commit()
        return obj_in

    async def get_all(self) -> CompaniesResponse:
        db_result = await self.db.execute(select(Company))
        return db_result.scalars().all()
