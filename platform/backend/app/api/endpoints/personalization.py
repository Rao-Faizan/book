from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.core.db import get_db
from app.models.user import UserProfile
from app.services.gemini import gemini_service

router = APIRouter()

class PersonalizeRequest(BaseModel):
    text: str
    user_id: str

class TranslateRequest(BaseModel):
    text: str

class ContentResponse(BaseModel):
    transformed_text: str

@router.post("/rewrite", response_model=ContentResponse)
async def personalize_content(request: PersonalizeRequest, db: AsyncSession = Depends(get_db)):
    # 1. Fetch User Profile
    result = await db.execute(select(UserProfile).filter(UserProfile.user_id == request.user_id))
    user = result.scalars().first()
    
    expertise = "Beginner"
    if user:
        expertise = user.python_expertise.value
        
    # 2. Build Prompt
    system_prompt = f"""You are an expert technical editor.
    Rewrite the following text to be suitable for a '{expertise}' level Python/Robotics student.
    - If Beginner: Use simple analogies, explain jargon, and focus on 'why'.
    - If Advanced: Be concise, strictly technical, and focus on implementation details.
    
    Keep the core technical facts accurate."""
    
    full_prompt = f"{system_prompt}\n\nORIGINAL TEXT:\n{request.text}"
    
    # 3. Generate
    rewritten = await gemini_service.generate_content(full_prompt)
    return ContentResponse(transformed_text=rewritten)

@router.post("/translate", response_model=ContentResponse)
async def translate_content(request: TranslateRequest):
    # 1. Build Prompt
    system_prompt = """You are an expert technical translator.
    Translate the following text into Urdu.
    - Keep technical terms (like ROS, Node, Topic, Sensor, Lidar) in English.
    - Translate the explanation and context into clear, natural Urdu.
    - You can use Roman Urdu if the script is not supported, but preferably use Urdu Script."""
    
    full_prompt = f"{system_prompt}\n\nTEXT:\n{request.text}"
    
    # 2. Generate
    translation = await gemini_service.generate_content(full_prompt)
    return ContentResponse(transformed_text=translation)
