# Base class used by all SQLAlchemy database models.
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """
    Base class for all database models.

    Every SQLAlchemy model in our system will inherit from this class.
    """
    pass