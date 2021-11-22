import fastapi

app = fastapi.FastAPI()


@app.get("/")
async def get_root() -> dict[str, str]:
    return {"msg": "hello world"}
