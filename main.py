#! /usr/bin/env python3

from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel
import pdb


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()

app.variable: str = "Hola"


@app.get("/")
async def read_root():
    return {"Data": app.variable}


@app.put("/{message}")
async def write_root(message: str):
    app.variable = message


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name":
                                                              "Baz"}]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]


@app.get("/items/{item_id}")
async def read_user_item(
    item_id: str, needy: str, skip: int = 0, limit: int | None = None
):
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item


@app.post("/body/item/{item_id}")
async def create_item(item_id: int, item: Item, q: str | None = None):
    pdb.set_trace()
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result
