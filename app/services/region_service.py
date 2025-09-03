import boto3
from typing import List, Dict
from fastapi import HTTPException
from app.config.settings import settings

def list_regions() -> List[Dict[str, str]]:
    """
    Returns a list of all AWS regions for the account.
    """
    session = boto3.Session(region_name=settings.AWS_REGION)
    ec2 = session.client("ec2")
    response = ec2.describe_regions(AllRegions=True)

    regions = []
    for r in response.get("Regions", []):
        regions.append({
            "region_name": r["RegionName"],
            "opt_in_status": r["OptInStatus"]
        })
    return regions


def set_region(payload: Dict[str, str]) -> str:
    """
    Validate and update the AWS region at runtime.
    """
    region: str | None = payload.get("region")
    if not region:
        raise HTTPException(status_code=400, detail="Missing 'region' in request body")
    
    available_regions: List[Dict[str, str]] = list_regions()
    region_names = [r["region_name"] for r in available_regions]

    if region not in region_names:
        raise HTTPException(
            status_code=400,
            detail={
                "error": f"Invalid region '{region}'",
                "available_regions": region_names
            }
        )

    settings.AWS_REGION = region
    return f"AWS region successfully updated to '{region}'"
