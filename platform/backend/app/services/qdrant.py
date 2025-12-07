from qdrant_client import QdrantClient
from qdrant_client.http import models
from app.core.config import settings

class QdrantService:
    def __init__(self):
        self.client = QdrantClient(
            url=settings.QDRANT_URL,
            api_key=settings.QDRANT_API_KEY
        )
        self.collection_name = settings.QDRANT_COLLECTION

    def create_collection_if_not_exists(self):
        collections = self.client.get_collections()
        exists = any(c.name == self.collection_name for c in collections.collections)
        
        if not exists:
            self.client.create_collection(
                collection_name=self.collection_name,
                vectors_config=models.VectorParams(
                    size=768,  #text-embedding-004 dimension
                    distance=models.Distance.COSINE
                )
            )

    def search(self, vector: list[float], limit: int = 5):
        return self.client.search(
            collection_name=self.collection_name,
            query_vector=vector,
            limit=limit
        )

    def upsert(self, points: list[models.PointStruct]):
        self.client.upsert(
            collection_name=self.collection_name,
            points=points
        )

# Singleton instance
qdrant_service = QdrantService()
