from fastapi import APIRouter
from app.api.endpoints import chat, profile, personalization

api_router = APIRouter()
api_router.include_router(chat.router, prefix="/chat", tags=["chat"])
api_router.include_router(profile.router, prefix="/profile", tags=["profile"])
api_router.include_router(personalization.router, prefix="/tools", tags=["tools"])
