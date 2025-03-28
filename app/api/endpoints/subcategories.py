from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.schemas.subcategory import SubCategory, SubCategoryCreate
from app.crud.subcategory_crud import (
    get_subcategories,
    create_subcategory,
    get_subcategory,
    update_subcategory,
    delete_subcategory
)
from app.db.session import get_db
from uuid import UUID

router = APIRouter()

@router.get("/", response_model=list[SubCategory])
def read_subcategories(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_subcategories(db, skip=skip, limit=limit)

@router.post("/", response_model=SubCategory)
def create_new_subcategory(subcategory: SubCategoryCreate, db: Session = Depends(get_db)):
    return create_subcategory(db, subcategory)

@router.get("/{subcategory_uuid}", response_model=SubCategory)
def read_subcategory(subcategory_uuid: UUID, db: Session = Depends(get_db)):
    db_subcategory = get_subcategory(db, subcategory_uuid)
    if db_subcategory is None:
        raise HTTPException(status_code=404, detail="SubCategory not found")
    return db_subcategory

@router.delete("/{subcategory_uuid}")
def delete_existing_subcategory(subcategory_uuid: UUID, db: Session = Depends(get_db)):
    return delete_subcategory(db, subcategory_uuid)