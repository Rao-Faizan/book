from fastapi import APIRouter, HTTPException
from app.api.schemas import ChatRequest, ChatResponse, ContextChatRequest
from app.services.gemini import gemini_service
from app.services.qdrant import qdrant_service

router = APIRouter()

@router.post("/rag", response_model=ChatResponse)
async def chat_rag(request: ChatRequest):
    try:
        # 1. Embed Query
        query_embedding = await gemini_service.get_embedding(request.query)
        
        # 2. Search Qdrant
        search_results = qdrant_service.search(query_embedding, limit=3)
        
        # 3. Construct Context
        context_text = "\n\n".join([hit.payload['content'] for hit in search_results])
        sources = [f"{hit.payload['module']} - {hit.payload['chapter']}" for hit in search_results]
        
        # 4. Prompt Engineering
        system_prompt = """You are an expert AI teaching assistant for the 'Physical AI & Humanoid Robotics' textbook.
        Answer the user's question based ONLY on the provided context below.
        If the answer is not in the context, state that you don't know based on the book materials.
        Keep answers technical, precise, and helpful."""
        
        full_prompt = f"""{system_prompt}
        
        CONTEXT:
        {context_text}
        
        USER QUESTION:
        {request.query}
        """
        
        # 5. Generate Answer
        answer = await gemini_service.generate_content(full_prompt)
        
        return ChatResponse(answer=answer, sources=sources)
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/context", response_model=ChatResponse)
async def chat_context(request: ContextChatRequest):
    try:
        # Direct generation based on selected text
        system_prompt = """You are an expert AI teaching assistant.
        A user has selected a specific text from the textbook and asked a question about it.
        Answer based on the selected text."""
        
        full_prompt = f"""{system_prompt}
        
        SELECTED TEXT:
        {request.selected_text}
        
        USER QUESTION:
        {request.query}
        """
        
        answer = await gemini_service.generate_content(full_prompt)
        
        return ChatResponse(answer=answer, sources=["Selected Text"])
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
