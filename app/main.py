"""Main FastAPI application entry point."""
from contextlib import asynccontextmanager
import torch
from fastapi import FastAPI
from transformers.pipelines import pipeline
from app.models.common import HealthResponse
from app.api import get_all_routers
from app.core.config import settings


@asynccontextmanager
async def lifespan(fastapi_app: FastAPI) -> None:
    device: int = 0 if torch.cuda.is_available() else -1
    fastapi_app.state.sentiment_pipeline = pipeline(
        "text-classification", device=device
    )
    yield
    del fastapi_app.state.sentiment_pipeline

app = FastAPI(title=settings.app_name, version=settings.version, lifespan=lifespan)

for router in get_all_routers():
    app.include_router(router)


@app.get("/", response_model=HealthResponse)
def read_root():
    """Root endpoint returning a simple health check message."""
    return HealthResponse(status="ok", version=settings.version)
