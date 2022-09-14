"""
NLP API Controller
"""

# FastAPI
from fastapi import APIRouter, Response

# Environment
from app.config.env import environment

# Model
from app.utils.request_body import TextSimilarity, NLPEmbedding

# Services
from app.services.nlp import text_similarity

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
        environment.log.error(message)
        return {"message": message, "result": {}}
