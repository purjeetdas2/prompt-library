from pydantic import BaseModel
from uuid import UUID

class SubCategoryBase(BaseModel):
    name: str
    description: str
    category_uuid: UUID

class SubCategoryCreate(SubCategoryBase):
    pass

class SubCategory(SubCategoryBase):
    uuid: UUID

    class Config:
        orm_mode = True