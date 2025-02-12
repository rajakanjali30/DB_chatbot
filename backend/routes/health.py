from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
async def health_check():
    """
    Health check endpoint to verify if the backend is running.
    """
    return {"status": "Backend is running"}
