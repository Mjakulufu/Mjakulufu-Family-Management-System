# FastAPI tools for creating API routes and receiving uploaded files.
from fastapi import APIRouter, Depends, File, Form, UploadFile

# SQLAlchemy session used to communicate with PostgreSQL.
from sqlalchemy.orm import Session

# Import our database dependency.
from app.database.database import get_db

# Import the response schema.
from app.schemas.family_member import FamilyMemberResponse

# Import the service responsible for creating a family member.
from app.services.member_service import create_family_member

# Import our profile picture upload utility.
from app.utils.file_upload import save_profile_picture


# Create a router for family member endpoints.
router = APIRouter(
    prefix="/family-members",
    tags=["Family Members"],
)


@router.post(
    "/",
    response_model=FamilyMemberResponse,
)
async def register_family_member(
    # Receive the member's full name from the form.
    full_name: str = Form(...),

    # Receive the member's phone number from the form.
    phone: str = Form(...),

    # Email is optional.
    email: str | None = Form(None),

    # Gender is optional.
    gender: str | None = Form(None),

    # Date of birth is optional.
    date_of_birth: str | None = Form(None),

    # Address is optional.
    address: str | None = Form(None),

    # Receive the profile picture.
    profile_picture: UploadFile = File(...),

    # Get a database session.
    db: Session = Depends(get_db),
):
    """
    Register a new family member.

    The endpoint:
    1. Receives member information.
    2. Receives the profile picture.
    3. Saves the picture.
    4. Creates the family member.
    5. Returns the saved member.
    """

    # Save the uploaded profile picture.
    picture_path = await save_profile_picture(profile_picture)

    # Create the family member through the service layer.
    member = create_family_member(
        db=db,
        full_name=full_name,
        phone=phone,
        email=email,
        gender=gender,
        date_of_birth=date_of_birth,
        address=address,
        profile_picture=picture_path,
    )

    # Return the newly registered member.
    return member