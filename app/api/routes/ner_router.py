"""Router for performing Named Entity Recognition."""
from fastapi import APIRouter


router = APIRouter(
    prefix="/ner",
    tags=["Named Entity Recognition"],
)

