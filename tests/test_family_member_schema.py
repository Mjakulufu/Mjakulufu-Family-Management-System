# pytest is used to run our automated tests.
import pytest
from pydantic import ValidationError

# Import the schema we want to test.
from app.schemas.family_member import FamilyMemberCreate


def test_family_member_schema_valid_data():
    """
    Test that valid family member data is accepted.
    """

    # Create valid member data.
    member = FamilyMemberCreate(
        full_name="Ramadhani Mjakulufu",
        phone="0712345678",
        email="ramadhani@example.com",
        gender="Male",
        date_of_birth="2005-11-19",
        address="Mbeya",
        profile_picture="uploads/profile_pictures/member.jpg",
    )

    # Check that the values were accepted correctly.
    assert member.full_name == "Ramadhani Mjakulufu"
    assert member.phone == "0712345678"
    assert member.email == "ramadhani@example.com"


def test_family_member_schema_invalid_email():
    """
    Test that an invalid email address is rejected.
    """

    # Pydantic should reject an invalid email.
    with pytest.raises(ValidationError):
        FamilyMemberCreate(
            full_name="Ramadhani Mjakulufu",
            phone="0712345678",
            email="not-an-email",
            gender="Male",
            profile_picture="uploads/profile_pictures/member.jpg",
        )