from fastapi import FastAPI
from app.api import get_all_routers

app = FastAPI()

for router in get_all_routers():
    app.include_router(router)

@app.get("/")
def read_root():
    return {"Hello": "World"}

