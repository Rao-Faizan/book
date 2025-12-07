from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, replace with frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    from app.core.db import engine, Base
    from app.models.user import UserProfile # Import to register models
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    # pass

@app.get("/health")
def health_check():
    return {"status": "ok", "project": settings.PROJECT_NAME}

from app.api.api import api_router
app.include_router(api_router, prefix=settings.API_V1_STR)
