# Path is used to work with folders and file extensions.
from pathlib import Path

# uuid4 generates a unique name for every uploaded file.
from uuid import uuid4

# UploadFile allows FastAPI to receive uploaded files.
from fastapi import UploadFile


# Folder where profile pictures will be stored.
UPLOAD_DIR = Path("uploads/profile_pictures")


# File extensions allowed by our system.
ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp"}


async def save_profile_picture(file: UploadFile) -> str:
    """
    Save a family member's profile picture.

    The function:
    1. Checks that a file was provided.
    2. Checks that the file type is allowed.
    3. Creates the upload folder if necessary.
    4. Generates a unique filename.
    5. Saves the file.
    6. Returns the saved file path.
    """

    # Make sure the user uploaded a file.
    if not file.filename:
        raise ValueError("Profile picture is required.")

    # Get the file extension, for example .jpg or .png.
    extension = Path(file.filename).suffix.lower()

    # Check whether the uploaded file type is allowed.
    if extension not in ALLOWED_EXTENSIONS:
        raise ValueError(
            "Invalid image format. "
            "Allowed formats: JPG, JPEG, PNG, WEBP."
        )

    # Create the upload folder if it doesn't exist.
    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

    # Generate a unique filename.
    filename = f"{uuid4()}{extension}"

    # Create the complete file path.
    file_path = UPLOAD_DIR / filename

    # Read the uploaded file.
    content = await file.read()

    # Save the file to disk.
    with open(file_path, "wb") as buffer:
        buffer.write(content)

    # Return the path for storing in the database.
    return str(file_path)