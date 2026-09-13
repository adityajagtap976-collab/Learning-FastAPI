from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# A path parameter {item_id} is defined inside curly braces
@app.get("/items/{item_id}")
def read_item(item_id: int):
    # FastAPI automatically extracts item_id from the URL and converts it to an integer.
    return {"item_id": item_id, "message": f"Fetching data for {item_id}"}


# Query Parameter
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    # 'item_id' comes from the path: /items/42
    # 'q' comes from the query string: ?q=python
    return {"item_id": item_id, "query": q}


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None


@app.post("/items/")
def create_item(item: Item):
    return {"item_name": item.name, "total_price": item.price * 1.2}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_id": item_id, "item_name": item.name, "updated_price": item.price}
