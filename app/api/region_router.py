from fastapi import APIRouter
from app.services.region_service import *

router = APIRouter(prefix="/regions", tags=["Regions"])

@router.get("")
def get_regions():
    return {"regions": list_regions()}

@router.post("/set-region")
def set_region_api(payload: Dict[str, str]) -> Dict[str, str]:
    """API to update AWS region at runtime."""
    message: str = set_region(payload)
    return {"message": message} 
