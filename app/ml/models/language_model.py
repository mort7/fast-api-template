"""
Spacy Language Model
"""

# Imports
import logging
import spacy

from scipy import spatial

from app.config.env import environment


class LanguageModel:
    """
    NLP Model
    """

    def __init__(self) -> None:
        """
        Load model
        """
        logging.info("Loading model")
        try:
            self.model = spacy.load(environment.model_name)
            logging.info("Model load complete")
        except Exception as error:
            logging.error(error)

    def text_similarity(self, text_one, text_two) -> float:
        """
        Text similarity between two text inputs

        Args:
            text_one (str): Text input string
            text_two (str): Text input string

        Return:
            score (float): Text similarity score
        """
        similarity = lambda x, y: 1 - spatial.distance.cosine(x, y)

        text_vec1 = self.model(text_one.lower()).vector
        text_vec2 = self.model(text_two.lower()).vector

        return similarity(text_vec1, text_vec2)

    def nlp_embedding(self, text_input):
        """
        NLP embedding

        Args:
            text_input (str): Text input string

        Return:
            embedding (Floats1d): Embedding as a one dimensional float array
        """
        return self.model(text_input.lower()).vector


model = LanguageModel()
