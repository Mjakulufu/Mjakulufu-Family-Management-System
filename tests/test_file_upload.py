from io import BytesIO
from pathlib import Path

import pytest
from fastapi import UploadFile

from app.utils.file_upload import save_profile_picture


@pytest.mark.asyncio
async def test_save_profile_picture():
    # Create fake image content for testing
    fake_image = BytesIO(b"fake image content")

    # Create an uploaded file object
    test_file = UploadFile(
        filename="profile.jpg",
        file=fake_image,
    )

    # Save the profile picture
    saved_path = await save_profile_picture(test_file)

    # Convert the returned path to a Path object
    file_path = Path(saved_path)

    # Check that the file was created
    assert file_path.exists()

    # Check that the extension is correct
    assert file_path.suffix == ".jpg"

    # Check that it is inside profile_pictures
    assert file_path.parent.name == "profile_pictures"

    # Remove the test file after testing
    file_path.unlink()