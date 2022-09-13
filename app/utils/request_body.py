"""
Request Bodies
"""

from pydantic import BaseModel


class TextSimilarity(BaseModel):
    """
    Text Similarity Request Body
    """

    text_one: str
    text_two: str


class NLPEmbedding(BaseModel):
    """
    NLP Embedding Request Body
    """

    text_input: str
