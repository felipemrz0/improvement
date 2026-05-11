"""Main FastAPI application entry point."""
from contextlib import asynccontextmanager
import torch
from fastapi import FastAPI
from transformers.pipelines import pipeline
from app.models.common import HealthResponse
from app.api import get_all_routers
from app.core.config import settings
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request


@asynccontextmanager
async def lifespan(fastapi_app: FastAPI) -> None:
    device: int = 0 if torch.cuda.is_available() else -1
    fastapi_app.state.sentiment_pipeline = pipeline(
        "text-classification", device=device
    )
    yield
    del fastapi_app.state.sentiment_pipeline

app = FastAPI(title=settings.app_name, version=settings.version, lifespan=lifespan)
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

for router in get_all_routers():
    app.include_router(router)


@app.get("/")
def index(req: Request):
    """Root endpoint serving the feature index page."""
    return templates.TemplateResponse(request=req, name="index.html")

@app.get("/sentiment-analysis")
def sentiment_page(req: Request):
    """Sentiment analysis feature page."""
    return templates.TemplateResponse(request=req, name="sentiment.html")


@app.get("/health", response_model=HealthResponse)
def read_root():
    """Root endpoint returning a simple health check message."""
    return HealthResponse(status="ok", version=settings.version)
