from fastapi import APIRouter, Depends, HTTPException
from typing import Optional
from sqlalchemy.orm import Session
import os

import shutil

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse


from dependencies import get_db
from crud.price import get_price

router = APIRouter(
    prefix="/app",
    tags=["app"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
def read_root():
    return {"Hello": "World"}


@router.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@router.get("/price")
def getPrice(db: Session = Depends(get_db)):
    price = get_price(db)
    if not price:
        raise HTTPException(status_code=400, detail="Email already registered")
    return {'hello':'world'}

@router.post("/upload-file")
async def create_upload_file(uploaded_file: UploadFile = File(...)):    
    file_location = f"files/{uploaded_file.filename}"
    with open(file_location, "wb+") as file_object:
        shutil.copyfileobj(uploaded_file.file, file_object)    
    return {"info": f"file '{uploaded_file.filename}' saved at '{file_location}'"}


@router.get("/file")
def read_item( path: Optional[str] = None):
    if not path:
        return {"file": "ups"}
    else:
        return FileResponse(path)

@router.get("/files")
def read_item( path: Optional[str] = None):
    if not path:
        return {"file": "ups"}
    else:
        remove_file(path)
        return {"file": "ooops"}

def remove_file(path: str) -> None:
    os.unlink(path)