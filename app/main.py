from fastapi import FastAPI
from app.api import vpc_router as vpc  
from app.api import region_router


app = FastAPI(title="Infrastructure Platform")

app.include_router(vpc.router, prefix="/vpc", tags=["VPC"])
app.include_router(region_router.router)
