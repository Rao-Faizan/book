from pydantic import BaseModel
from typing import List, Optional

class ChatRequest(BaseModel):
    query: str
    history: Optional[List[dict]] = [] # [{'role': 'user', 'content': '...'}, ...]

class ContextChatRequest(BaseModel):
    query: str
    selected_text: str

class ChatResponse(BaseModel):
    answer: str
    sources: Optional[List[str]] = []
