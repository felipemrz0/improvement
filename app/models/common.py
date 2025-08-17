"""Common/shared Pydantic models used across the application."""
from pydantic import BaseModel


class ErrorResponse(BaseModel):
    """Standard error response model."""

    detail: str


class HealthResponse(BaseModel):
    """Standard health check response model."""

    status: str
    version: str | None = None