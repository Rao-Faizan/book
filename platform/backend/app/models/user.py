from sqlalchemy import Column, String, Enum, Integer, ForeignKey
from app.core.db import Base
import enum

class PythonExpertise(str, enum.Enum):
    BEGINNER = "Beginner"
    INTERMEDIATE = "Intermediate"
    ADVANCED = "Advanced"

class HardwareAccess(str, enum.Enum):
    SIM_ONLY = "SimOnly"
    JETSON_NANO = "JetsonNano"
    JETSON_ORIN = "JetsonOrin"
    RTX_GPU = "RTX"

class UserProfile(Base):
    __tablename__ = "user_profiles"

    user_id = Column(String, primary_key=True, index=True) # ID from Auth Provider
    email = Column(String, unique=True, index=True)
    python_expertise = Column(Enum(PythonExpertise), default=PythonExpertise.BEGINNER)
    hardware_access = Column(Enum(HardwareAccess), default=HardwareAccess.SIM_ONLY)
    preferred_language = Column(String, default="en")
