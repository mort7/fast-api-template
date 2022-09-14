"""
NLP API Service
"""

# Language Model
from app.ml.models.language_model import model


async def text_similarity(**kwargs):
    """
    Text Similarity
    """

    output = {}

    # Parse Parameters
    text_one = kwargs["text_one"]
    text_two = kwargs["text_two"]

    output["text_one"] = text_one
    output["text_two"] = text_two
    output["score"] = model.text_similarity(text_one, text_two)

    return output
