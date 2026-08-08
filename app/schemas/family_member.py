# date is used for the member's date of birth.
from datetime import date

# BaseModel is the foundation of Pydantic schemas.
from pydantic import BaseModel, EmailStr


class FamilyMemberBase(BaseModel):
    """
    Common fields shared by family member schemas.
    """

    # Member's full name.
    full_name: str

    # Member's phone number.
    phone: str

    # Member's email address.
    email: EmailStr | None = None

    # Member's gender.
    gender: str | None = None

    # Member's date of birth.
    date_of_birth: date | None = None

    # Member's residential address.
    address: str | None = None


class FamilyMemberCreate(FamilyMemberBase):
    """
    Data required when creating a new family member.
    """

    # Profile picture path will be added after the upload.
    profile_picture: str


class FamilyMemberResponse(FamilyMemberBase):
    """
    Data returned when displaying a family member.
    """

    # Unique ID assigned by the database.
    id: int

    # Path to the member's profile picture.
    profile_picture: str

    # Allow Pydantic to read data directly from SQLAlchemy models.
    model_config = {
        "from_attributes": True
    }