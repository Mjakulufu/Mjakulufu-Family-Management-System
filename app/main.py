# FastAPI application.
from fastapi import FastAPI

# Import the family member router.
from app.api.routes.family_member import router as family_member_router


# Create the main FastAPI application.
app = FastAPI(
    title="Mjakulufu Family Management System",
    description="API for managing Mjakulufu family members.",
    version="1.0.0",
)


# Register the family member routes.
app.include_router(family_member_router)


@app.get("/")
def root():
    """
    Basic endpoint to confirm that the API is running.
    """

    return {
        "message": "Mjakulufu Family Management System API is running"
    }