"""
FastAPI Template - Main
"""
# Imports
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config.env import environment

# Routers
from app.controllers.nlp import nlp_router

# Fast API
app = FastAPI(title=environment.app_name, version=environment.app_version)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add Routers
app.include_router(nlp_router, prefix="/api/v1")


@app.get("/")
async def root():
    """
    Run check endpoint
    """
    return {"message": "FastAPI Template - Running"}
