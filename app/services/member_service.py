# SQLAlchemy Session is used to communicate with the database.
from sqlalchemy.orm import Session

# Import the FamilyMember database model.
from app.models.family_member import FamilyMember

# Import the repository functions.
from app.repositories.member_repository import create_member


def create_family_member(
    db: Session,
    full_name: str,
    phone: str,
    email: str | None,
    gender: str | None,
    date_of_birth,
    address: str | None,
    profile_picture: str,
) -> FamilyMember:
    """
    Create a new family member.

    The service layer:
    1. Receives validated information.
    2. Creates a FamilyMember model.
    3. Sends it to the repository.
    4. Returns the saved member.
    """

    # Create a FamilyMember database object.
    member = FamilyMember(
        full_name=full_name,
        phone=phone,
        email=email,
        gender=gender,
        date_of_birth=date_of_birth,
        address=address,
        profile_picture=profile_picture,
    )

    # Save the member using the repository.
    created_member = create_member(
        db,
        member,
    )

    # Return the member saved in the database.
    return created_member