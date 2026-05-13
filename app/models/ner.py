"""Pydantic models for Named Entity Recognition."""
from enum import Enum

from pydantic import BaseModel, Field


class NERRequest(BaseModel):
    """Request model for NER analysis.
    Attributes:
        text (str): Input text to be analyzed. Must be between 6 and 512 characters."""

    text: str = Field(..., min_length=6, max_length=512, example="Pol is working at Amazon")


class EntityType(str, Enum):
    """Enumeration of named entity types."""

    PER = "PER"
    ORG = "ORG"
    LOC = "LOC"
    MISC = "MISC"


class EntityResult(BaseModel):
    """Represents a single named entity found in the text.

    Attributes:
        word (str): The entity text as it appears in the input.
        entity (EntityType): The type of entity detected.
        score (float): Confidence score of the prediction.
        start (int): Start character position in the original text.
        end (int): End character position in the original text.
    """
    word: str
    entity: EntityType
    score: float
    start: int
    end: int


class NERResponse(BaseModel):
    """Response model for NER requests.

    Attributes:
    entities (list[EntityResult]): List of entities found in the text.
    model (str): Name of the underlying model used.
    """

    entities: list[EntityResult]
    model: str
