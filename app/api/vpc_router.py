from fastapi import APIRouter
from typing import Dict, List
from app.services.vpc_service import list_vpcs

router = APIRouter()

@router.get("/vpcs", response_model=Dict[str, List[Dict[str, str]]])
def get_vpcs():
    """
    Controller to return VPCs in current AWS account/region.
    """
    vpcs = list_vpcs()
    return {"vpcs": vpcs}
