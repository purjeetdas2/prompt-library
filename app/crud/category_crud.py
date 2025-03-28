from sqlalchemy.orm import Session
from uuid import UUID
from app.db.models import Category
from app.schemas.category import CategoryCreate

def get_categories(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Category).offset(skip).limit(limit).all()

def create_category(db: Session, category: CategoryCreate):
    db_category = Category(**category.dict())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def get_category(db: Session, category_uuid: UUID):
    return db.query(Category).filter(Category.uuid == category_uuid).first()

def update_category(db: Session, category_uuid: UUID, category_data: CategoryCreate):
    db_category = get_category(db, category_uuid)
    if db_category:
        for key, value in category_data.dict(exclude_unset=True).items():
            setattr(db_category, key, value)
        db.commit()
        db.refresh(db_category)
    return db_category

def delete_category(db: Session, category_uuid: UUID):
    db_category = get_category(db, category_uuid)
    if db_category:
        db.delete(db_category)
        db.commit()
    return db_category