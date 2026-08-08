# pytest is used to run our automated tests.
import pytest

# SQLAlchemy Session is used for database operations.
from sqlalchemy.orm import Session

# Import the service function we want to test.
from app.services.member_service import create_family_member

# Import our database session factory.
from app.database.database import SessionLocal


@pytest.fixture
def db_session():
    """
    Create a database session for the service test.

    The test member will be removed after the test.
    """

    # Create a new database session.
    db: Session = SessionLocal()

    try:
        # Give the test access to the database session.
        yield db

    finally:
        # Close the database session.
        db.close()


def test_create_family_member(db_session):
    """
    Test creating a family member through the service layer.
    """

    # Create a family member using the service.
    member = create_family_member(
        db=db_session,
        full_name="Service Test Member",
        phone="0700000002",
        email="service.test@example.com",
        gender="Female",
        date_of_birth=None,
        address="Service Test Address",
        profile_picture="uploads/profile_pictures/service_test.jpg",
    )

    # The database should generate an ID.
    assert member.id is not None

    # Check that the information was saved correctly.
    assert member.full_name == "Service Test Member"
    assert member.phone == "0700000002"
    assert member.email == "service.test@example.com"

    # Remove the test member from the database.
    db_session.delete(member)
    db_session.commit()