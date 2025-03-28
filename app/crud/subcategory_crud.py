from sqlalchemy.orm import Session
from uuid import UUID
from app.db.models import SubCategory
from app.schemas.subcategory import SubCategoryCreate

def get_subcategories(db: Session, skip: int = 0, limit: int = 10):
    return db.query(SubCategory).offset(skip).limit(limit).all()

def create_subcategory(db: Session, subcategory: SubCategoryCreate):
    db_subcategory = SubCategory(**subcategory.dict())
    db.add(db_subcategory)
    db.commit()
    db.refresh(db_subcategory)
    return db_subcategory

def get_subcategory(db: Session, subcategory_uuid: UUID):
    return db.query(SubCategory).filter(SubCategory.uuid == subcategory_uuid).first()

def update_subcategory(db: Session, subcategory_uuid: UUID, subcategory_data: SubCategoryCreate):
    db_subcategory = get_subcategory(db, subcategory_uuid)
    if db_subcategory:
        for key, value in subcategory_data.dict(exclude_unset=True).items():
            setattr(db_subcategory, key, value)
        db.commit()
        db.refresh(db_subcategory)
    return db_subcategory

def delete_subcategory(db: Session, subcategory_uuid: UUID):
    db_subcategory = get_subcategory(db, subcategory_uuid)
    if db_subcategory:
        db.delete(db_subcategory)
        db.commit()
    return db_subcategory