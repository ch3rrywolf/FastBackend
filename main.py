from fastapi import FastAPI

app = FastAPI()
app = FastAPI(swagger_ui_parameters={"syntaxHighlight": False})

@app.get("/")
async def root():
    return {"message": "3assléma"}