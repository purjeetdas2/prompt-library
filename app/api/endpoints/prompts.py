from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.schemas.prompt import Prompt, PromptCreate
from app.crud.prompt_crud import (
    get_prompts,
    create_prompt,
    get_prompt,
    update_prompt,
    delete_prompt
)
from app.db.session import get_db
from uuid import UUID

router = APIRouter()

@router.get("/", response_model=list[Prompt])
def read_prompts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_prompts(db, skip=skip, limit=limit)

@router.post("/", response_model=Prompt)
def create_new_prompt(prompt: PromptCreate, db: Session = Depends(get_db)):
    return create_prompt(db, prompt)

@router.get("/{prompt_uuid}", response_model=Prompt)
def read_prompt(prompt_uuid: UUID, db: Session = Depends(get_db)):
    db_prompt = get_prompt(db, prompt_uuid)
    if db_prompt is None:
        raise HTTPException(status_code=404, detail="Prompt not found")
    return db_prompt

@router.put("/{prompt_uuid}", response_model=Prompt)
def update_existing_prompt(prompt_uuid: UUID, prompt: PromptCreate, db: Session = Depends(get_db)):
    return update_prompt(db, prompt_uuid, prompt)

@router.delete("/{prompt_uuid}")
def delete_existing_prompt(prompt_uuid: UUID, db: Session = Depends(get_db)):
    return delete_prompt(db, prompt_uuid)