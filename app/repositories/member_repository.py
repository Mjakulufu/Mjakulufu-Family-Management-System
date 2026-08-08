# SQLAlchemy Session is used to communicate with the database.
from sqlalchemy.orm import Session

# Import the FamilyMember database model.
from app.models.family_member import FamilyMember


def create_member(
    db: Session,
    member: FamilyMember,
) -> FamilyMember:
    """
    Save a new family member to the database.

    Steps:
    1. Add the member to the database session.
    2. Commit the transaction.
    3. Refresh the object to get generated values such as ID.
    4. Return the saved member.
    """

    # Add the member to the current database session.
    db.add(member)

    # Permanently save the changes to PostgreSQL.
    db.commit()

    # Refresh the object so generated database values are available.
    db.refresh(member)

    # Return the saved family member.
    return member


def get_member_by_id(
    db: Session,
    member_id: int,
) -> FamilyMember | None:
    """
    Find a family member using their ID.

    Returns:
        FamilyMember if found.
        None if the member does not exist.
    """

    # Search for the member whose ID matches member_id.
    return (
        db.query(FamilyMember)
        .filter(FamilyMember.id == member_id)
        .first()
    )