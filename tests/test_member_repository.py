# pytest is used to run automated tests.
import pytest

# SQLAlchemy Session manages the database connection.
from sqlalchemy.orm import Session

# Import the database session factory.
from app.database.database import SessionLocal

# Import the FamilyMember database model.
from app.models.family_member import FamilyMember

# Import the repository functions we want to test.
from app.repositories.member_repository import (
    create_member,
    get_member_by_id,
)


@pytest.fixture
def db_session():
    """
    Create a database session for the repository test.

    The test data is deleted after the test,
    so our normal database stays clean.
    """

    # Create a new database session.
    db: Session = SessionLocal()

    # Create a unique phone number for the test member.
    test_phone = "0700000001"

    try:
        # Create a test family member.
        member = FamilyMember(
            full_name="Test Member",
            phone=test_phone,
            email="test.member@example.com",
            gender="Male",
            address="Test Address",
            profile_picture="uploads/profile_pictures/test.jpg",
        )

        # Save the member using the repository.
        created_member = create_member(db, member)

        # Give the test access to the created member.
        yield db, created_member

    finally:
        # Delete the test member after the test.
        if "created_member" in locals():
            db.delete(created_member)
            db.commit()

        # Close the database session.
        db.close()


def test_create_and_get_member(db_session):
    """
    Test creating and retrieving a family member.
    """

    # Get the database session and created member.
    db, created_member = db_session

    # Make sure the database generated an ID.
    assert created_member.id is not None

    # Retrieve the member using the generated ID.
    found_member = get_member_by_id(
        db,
        created_member.id,
    )

    # Make sure the member was found.
    assert found_member is not None

    # Verify that we retrieved the correct member.
    assert found_member.full_name == "Test Member"
    assert found_member.phone == "0700000001"