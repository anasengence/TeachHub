from typing import Union

from fastapi import FastAPI, File, UploadFile

from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int
    email: str
    address: str

@app.get("/hello")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q = 'Item'):
    return {"item_id": item_id, "q": q}


@app.post("/users/")
def create_user(user: User):
    return { "name": f'{user.name} is created' }


@app.post("/uploadfile/")
def create_upload_file(file: UploadFile = File(...)):
    with open(f"files/{file.filename}", "wb") as buffer:
        buffer.write(file.file.read())
    return {"filename": file.filename}