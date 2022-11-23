from src.controllers.faceVerifyController import train_endpoint
from fastapi import APIRouter

api_router = APIRouter()
api_router.include_router(train_endpoint, prefix='/verify',tags=["FaceVerify"])

