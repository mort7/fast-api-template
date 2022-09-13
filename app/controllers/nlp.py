"""
NLP API Controller
"""

# Imports
import logging

# FastAPI
from fastapi import APIRouter, Response

# Model
from app.utils.request_body import TextSimilarity, NLPEmbedding

# Services
from app.services.nlp import text_similarity, nlp_embedding

# Exception
from app.utils.exceptions import APIException

# Router
nlp_router = APIRouter(prefix="/nlp")


@nlp_router.get("/text-similarity")
async def get_text_similarity(request_body: TextSimilarity, response: Response):
    """
    Get - Text Similarity
    """
    try:
        result = await text_similarity(**request_body.dict())
        return {"message": "success", "result": result}
    except APIException as error:
        response.status_code = error.status_code
        message = error.system + " Error -" + error.message
        logging.error(message)
        return {"message": message, "result": {}}
