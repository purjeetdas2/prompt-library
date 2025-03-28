from pydantic import BaseModel
from uuid import UUID

class CategoryBase(BaseModel):
    name: str
    description: str

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    uuid: UUID

    class Config:
        orm_mode = True