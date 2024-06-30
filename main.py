########################################################################################################
from fastapi import FastAPI, Query, Path
from pydantic import BaseModel

########################################################################################################
app = FastAPI()
#app = FastAPI(swagger_ui_parameters={"syntaxHighlight": False})
app = FastAPI(swagger_ui_parametres={"syntaxHighlight.theme": "obsidian"})
########################################################################################################
class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None
# class Item(BaseModel):
#     name: str
#     price: float
#     is_offer: bool = None
######################################################################################################
@app.post("/items/")
async def create_item(item: Item):
    # print("Validation data:", item.model_dump())
    # return {"message": "Item created successfully", "data": item.model_dump()}
    print("Validation data:", item.dict())
    return {"message": "Item created successfully", "data": item.dict()}

# @app.get("/")
# async def root():
#     return {"message": "3assléma"}

# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     return {"item_id": item_id}

# @app.get("/items/")
# async def read_item(item_id: int, q: str = None):
#     return {"item_id": item_id, "q": q}

# @app.get("/items/{item_id}")
# async def read_item(item_id: int, q: str = None):
#     return {"item_id": item_id, "q": q}

# @app.post("/items/")
# async def create_item(item: Item):
#     return item

# @app.get("/items/")
# async def read_items(q: str = Query(None, min_length=3, max_length=50)):
#     return {"q": q}

# @app.get("/items/{item_id}")
# async def read_item(item_id: int = Path(..., title="The ID of the item to get", ge=1)):
#     return {"item_id": item_id}
##########################################################################################################