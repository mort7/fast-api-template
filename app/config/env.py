"""
Environment Configuration File
"""

# Imports
import os
import logging
from pydantic import BaseSettings


class Environment(BaseSettings):
    """
    Environment and Settings
    """

    # App settings
    app_name: str = "FastAPI Template"
    app_version: str = "0.1.0"

    # Logging
    log_name = "fastapi-template"
    log = logging.getLogger(log_name)
    logging.basicConfig(level=logging.INFO)

    # Redis
    redis_host: str = os.getenv("redis_host", "localhost")
    redis_port: str = os.getenv("redis_port", "6379")
    redis_pass: str = os.getenv("redis_pass", None)
    redis_prefix = os.getenv("redis_prefix", "fastapi")

    # Model
    model_name: str = "en_core_web_md"


environment = Environment()
