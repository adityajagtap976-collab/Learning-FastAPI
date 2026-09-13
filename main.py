from fastapi import FastAPI, Query, status, HTTPException
from pydantic import BaseModel, SecretStr
from helper import verify_item_exists
from typing import Optional

app = FastAPI()


# A path parameter {item_id} is defined inside curly braces
@app.get("/items/{item_id}")
def read_item(item_id: int):
    # FastAPI automatically extracts item_id from the URL and converts it to an integer.
    verify_item_exists(item_id)
    return {"item_id": item_id, "message": f"Fetching data for {item_id}"}


# Query Parameter
@app.get("/items/{item_id}/query")
def read_item_with_query(item_id: int, q: Optional[str] = None):
    # 'item_id' comes from the path: /items/42
    # 'q' comes from the query string: ?q=python
    return {"item_id": item_id, "query": q}


class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None


@app.post("/items/")
def create_item(item: Item):
    return {"item_name": item.name, "total_price": item.price * 1.2}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_id": item_id, "item_name": item.name, "updated_price": item.price}


# Query parameters with validation
@app.get("/items")
def read_items(q: str = Query(None, min_length=3, max_length=10)):
    return {"query": q}


# Response Models & HTTP Status Codes
class UserIn(BaseModel):
    username: str
    password: SecretStr


class UserOut(BaseModel):
    username: str


@app.post("/users/", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def create_user(user: UserIn):
    return user


@app.get("/items/{item_id}/verified")
def get_item(item_id: int):
    # Call our helper function to check if the item exists
    verify_item_exists(item_id)

    return {"item_id": item_id, "name": "Sample Item"}
