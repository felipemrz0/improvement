"""Pydantic models for sentiment analysis."""
from enum import Enum

from pydantic import BaseModel, Field


class SentimentRequest(BaseModel):
    """Request model for sentiment analysis.

    Attributes:
        text (str): Input text to be analyzed. Must be between 6 and 100 characters.

    """

    text: str = Field(..., min_length=6, max_length=100, example="I love this project!")


class SentimentLabel(str, Enum):
    """Enumeration of sentiment labels returned by the analysis."""

    positive = "POSITIVE"
    negative = "NEGATIVE"
    neutral = "NEUTRAL"


class SentimentResult(BaseModel):
    """Represents the sentiment analysis result for a single input text.

    Attributes:
        text (str): Original text analyzed.
        label (SentimentLabel): Predicted sentiment label.
        score (float): Confidence score of the prediction.
    """

    text: str
    label: SentimentLabel
    score: float


class SentimentAnalysisResponse(BaseModel):
    """Response model for sentiment analysis requests.

    Attributes:
        results (list[SentimentResult]): List of analysis results.
        model (str): Name of the underlying model used.
    """

    results: list[SentimentResult]
    model: str
