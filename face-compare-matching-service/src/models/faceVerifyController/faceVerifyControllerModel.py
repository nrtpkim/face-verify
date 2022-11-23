from pydantic import BaseModel
from fastapi import File, UploadFile


class FaceVerifyControllerModel(BaseModel):
    img1: bytes 
    img2: UploadFile


class imgPairsModel(BaseModel):
    img1: bytes 
    img2: bytes
    img1_name : str
    img2_name : str
