from fastapi import FastAPI

app = FastAPI()
#app = FastAPI(swagger_ui_parameters={"syntaxHighlight": False})
app = FastAPI(swagger_ui_parametres={"syntaxHighlight.theme": "obsidian"})

# @app.get("/")
# async def root():
#     return {"message": "3assléma"}

# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     return {"item_id": item_id}

# @app.get("/items/")
# async def read_item(item_id: int, q: str = None):
#     return {"item_id": item_id, "q": q}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}