from sqlalchemy import create_engine
from app.db.base import Base
from app.core.config import settings
import app.db.models  # Ensure models are imported for table creation


def init_db():
    # Create engine using the correct SQLite URL
    engine = create_engine(settings.database_url)

    # Create tables
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    init_db()