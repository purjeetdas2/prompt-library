from pydantic import BaseModel
from uuid import UUID
from typing import Optional, Dict

class PromptBase(BaseModel):
    title: str
    description: str
    prompt_text: str
    variables: Optional[Dict[str, str]] = None
    metadata: Optional[Dict[str, str]] = None
    subcategory_uuid: UUID

class PromptCreate(PromptBase):
    pass

class Prompt(PromptBase):
    uuid: UUID

    class Config:
        orm_mode = True