import cohere
from app.core.config import settings

class AIService:
    def __init__(self):
        self.client = None
        self.provider = "gemini" # default
        
        if settings.COHERE_API_KEY:
            self.provider = "cohere"
            self.client = cohere.ClientV2(settings.COHERE_API_KEY)
        # Fallback to Gemini if needed (not implemented fully for refactor simplicity)
        
    async def generate_content(self, prompt: str) -> str:
        if self.provider == "cohere":
            response = self.client.chat(
                model="command-r-plus", 
                messages=[{"role": "user", "content": prompt}]
            )
            return response.message.content[0].text
        return "AI Provider not configured"

    async def get_embedding(self, text: str) -> list[float]:
        if self.provider == "cohere":
            response = self.client.embed(
                texts=[text],
                model="embed-english-v3.0",
                input_type="search_document",
                embedding_types=["float"]
            )
            return response.embeddings.float[0]
        return []

    # Basic tool support stub (Cohere has tool use, but keeping robust RAG priority)
    async def start_chat_with_tools(self, history=[]):
        pass 

ai_service = AIService()
gemini_service = ai_service # Alias for compatibility
