"""Main FastAPI application entry point."""
from fastapi import FastAPI

from app.api import get_all_routers

app = FastAPI()

for router in get_all_routers():
    app.include_router(router)

@app.get("/")
def read_root():
    """Root endpoint returning a simple health check message."""
    return {"Hello": "World"}

