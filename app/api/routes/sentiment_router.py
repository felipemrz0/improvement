"""Router for performing sentiment analysis."""
from typing import Any

import torch
from fastapi import APIRouter, HTTPException
from transformers.pipelines import TextClassificationPipeline, pipeline

from app.models.sentiment import SentimentAnalysisResponse, SentimentRequest, SentimentResult

router = APIRouter(
    prefix="/sentiment-analysis",
    tags=["Sentiment Analysis"],
)

device:int = 0 if torch.cuda.is_available() else -1
sentiment_pipeline: TextClassificationPipeline = pipeline("text-classification", device=device)


def _model_id_from_pipeline(p: TextClassificationPipeline) -> str:
    """Extract a model identifier string from a Hugging Face pipeline.

    Returns:
         Either the model's `_name_or_path`, its class name, or "unknown-model".
    """
    name = getattr(getattr(p, "model", None), "config", None)
    model_id = getattr(name, "_name_or_path", None)
    if isinstance(model_id, str) and model_id:
        return model_id
    mdl = getattr(p, "model", None)
    return mdl.__class__.__name__ if mdl is not None else "unknown-model"

@router.post("/", response_model=SentimentAnalysisResponse)
def sentiment_analysis(request: SentimentRequest):
    """Analyze the sentiment of the given text.

    This endpoint uses a Hugging Face text-classification pipeline
    to determine the sentiment of the input text (e.g., positive,
    negative, or neutral), along with the confidence score.

    Args:
        request (SentimentRequest): The input request containing the text to analyze.

    Returns:
        SentimentAnalysisResponse: The sentiment analysis results, including the
        predicted label, and confidence score.

    Raises:
        HTTPException: If the underlying model pipeline fails during inference.

    """
    try:
        result: list[dict[str, Any]] = sentiment_pipeline(request.text)
        return SentimentAnalysisResponse(
            results=[SentimentResult(
                text=request.text, label=r["label"], score=r["score"])
                for r in result
            ],
            model=_model_id_from_pipeline(sentiment_pipeline))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e

