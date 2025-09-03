from typing import List, Dict
import boto3
from app.config.settings import settings
from pydantic_settings  import BaseSettings


def list_vpcs() -> List[Dict[str, str]]:
    """
    Returns a list of VPCs in the account using environment/role credentials.
    """
    session = boto3.Session(region_name=settings.AWS_REGION)
    ec2 = session.client("ec2")
    response = ec2.describe_vpcs()
    
    vpcs: List[Dict[str, str]] = []
    for vpc in response.get("Vpcs", []):
        vpc_id: str = vpc["VpcId"]
        cidr_block: str = vpc["CidrBlock"]
        is_default: bool = vpc["IsDefault"]
        state: str = vpc["State"]
        vpcs.append({
            "vpc_id": vpc_id,
            "cidr_block": cidr_block,
            "is_default": str(is_default).lower(),
            "state": state
        })
    return vpcs