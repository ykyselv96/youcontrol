from pydantic import BaseModel, ValidationError, validator, Field
from typing import Optional, List



class Company_in_db(BaseModel):
    id: int
    owner: int
    name: str
    description: str


class CompanyCreationForm(BaseModel):
    name: str = Field(..., min_length=1)
    description: Optional[str]



class CompaniesResponse(BaseModel):
    id: int
    name: str
    description: Optional[str]
    owner: int


class Company_update_form(BaseModel):
    name: Optional[str]
    description: Optional[str]

    @validator('name')
    def validate_name(cls, v):
        if len(v) == 0:
            raise ValidationError('name is invalid')

        return v