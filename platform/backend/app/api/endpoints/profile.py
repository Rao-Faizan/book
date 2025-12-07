from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from pydantic import BaseModel

from app.core.db import get_db
from app.models.user import UserProfile, PythonExpertise, HardwareAccess

router = APIRouter()

class ProfileUpdate(BaseModel):
    user_id: str
    email: str
    python_expertise: PythonExpertise
    hardware_access: HardwareAccess

class ProfileResponse(ProfileUpdate):
    pass

@router.post("/", response_model=ProfileResponse)
async def update_profile(profile: ProfileUpdate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(UserProfile).filter(UserProfile.user_id == profile.user_id))
    existing_user = result.scalars().first()

    if existing_user:
        existing_user.python_expertise = profile.python_expertise
        existing_user.hardware_access = profile.hardware_access
        existing_user.email = profile.email
    else:
        new_user = UserProfile(
            user_id=profile.user_id,
            email=profile.email,
            python_expertise=profile.python_expertise,
            hardware_access=profile.hardware_access
        )
        db.add(new_user)
    
    await db.commit()
    await db.refresh(existing_user if existing_user else new_user)
    return profile

@router.get("/{user_id}", response_model=ProfileResponse)
async def get_profile(user_id: str, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(UserProfile).filter(UserProfile.user_id == user_id))
    user = result.scalars().first()
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
        
    return ProfileResponse(
        user_id=user.user_id,
        email=user.email,
        python_expertise=user.python_expertise,
        hardware_access=user.hardware_access
    )
