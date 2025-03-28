from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.schemas import category
from app.crud.category_crud import (
    get_categories,
    create_category,
    get_category,
    update_category,
    delete_category
)
from app.db.session import get_db
from uuid import UUID

from app.schemas.category import Category, CategoryCreate

router = APIRouter()

@router.get("/", response_model=list[Category])
def read_categories(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_categories(db, skip=skip, limit=limit)

@router.post("/", response_model=Category)
def create_new_category(category: CategoryCreate, db: Session = Depends(get_db)):
    return create_category(db, category)

@router.get("/{category_uuid}", response_model=Category)
def read_category(category_uuid: UUID, db: Session = Depends(get_db)):
    db_category = get_category(db, category_uuid)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return db_category

@router.delete("/{category_uuid}")
def delete_existing_category(category_uuid: UUID, db: Session = Depends(get_db)):
    return delete_category(db, category_uuid)