from sqlalchemy import Column, Integer, String, ForeignKey, JSON, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid
from app.db.base import Base
from sqlalchemy.dialects.postgresql import UUID

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String)
    subcategories = relationship("SubCategory", back_populates="category")

class SubCategory(Base):
    __tablename__ = "subcategories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    category_id = Column(Integer, ForeignKey("categories.id"))
    category = relationship("Category", back_populates="subcategories")
    prompts = relationship("Prompt", back_populates="subcategory")

class Prompt(Base):
    __tablename__ = "prompts"

    id = Column(Integer, primary_key=True, index=True)
    uuid = Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    prompt_text = Column(String)  # Store the actual prompt text here
    subcategory_id = Column(Integer, ForeignKey("subcategories.id"))
    variables = Column(JSON)  # Store variables as a JSON object
    prompt_metadata = Column(JSON)  # Store additional metadata as a JSON object
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    subcategory = relationship("SubCategory", back_populates="prompts")