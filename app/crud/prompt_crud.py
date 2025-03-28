from sqlalchemy.orm import Session
from uuid import UUID
from app.db.models import Prompt
from app.schemas.prompt import PromptCreate

def get_prompts(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Prompt).offset(skip).limit(limit).all()

def create_prompt(db: Session, prompt: PromptCreate):
    db_prompt = Prompt(**prompt.dict())
    db.add(db_prompt)
    db.commit()
    db.refresh(db_prompt)
    return db_prompt

def get_prompt(db: Session, prompt_uuid: UUID):
    return db.query(Prompt).filter(Prompt.uuid == prompt_uuid).first()

def update_prompt(db: Session, prompt_uuid: UUID, prompt_data: PromptCreate):
    db_prompt = get_prompt(db, prompt_uuid)
    if db_prompt:
        for key, value in prompt_data.dict(exclude_unset=True).items():
            setattr(db_prompt, key, value)
        db.commit()
        db.refresh(db_prompt)
    return db_prompt

def delete_prompt(db: Session, prompt_uuid: UUID):
    db_prompt = get_prompt(db, prompt_uuid)
    if db_prompt:
        db.delete(db_prompt)
        db.commit()
    return db_prompt