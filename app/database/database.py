# SQLAlchemy engine and session tools.
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Import the single Base used by all models.
from app.database.base import Base


# PostgreSQL database connection URL.
DATABASE_URL = "postgresql+psycopg://postgres:Mohamed%40212@localhost:5432/mjakulufu_fms"


# Create the SQLAlchemy database engine.
engine = create_engine(
    DATABASE_URL,
    echo=True,
)


# Create a session factory for database operations.
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


def get_db():
    """
    Provide a database session to FastAPI routes.

    The session is automatically closed after use.
    """

    # Create a new database session.
    db = SessionLocal()

    try:
        # Give the session to the caller.
        yield db

    finally:
        # Always close the database connection.
        db.close()