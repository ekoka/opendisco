from .bootstrapper import app 

@app.get("/test/{msg}")
async def test(msg: str):
    return {"test": msg}
