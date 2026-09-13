from fastapi import FastAPI

app = FastAPI()


# A path parameter {item_id} is defined inside curly braces
@app.get("/items/{item_id}")
def read_item(item_id: int):
    # FastAPI automatically extracts item_id from the URL and converts it to an integer.
    return {"item_id": item_id, "message": f"Fetching data for {item_id}"}
