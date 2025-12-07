import os
import sys
import asyncio
import glob
import re
from typing import List, Dict
from qdrant_client.http import models
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Add backend to path to import services
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../backend")))

from app.services.gemini import gemini_service
from app.services.qdrant import qdrant_service

DOCS_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../book/docs"))

class IngestionPipeline:
    def __init__(self):
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            separators=["\n\n", "\n", " ", ""]
        )

    def clean_mdx(self, content: str) -> str:
        # Remove import statements
        content = re.sub(r'^import\s+.*$', '', content, flags=re.MULTILINE)
        # Remove JSX tags (simplified)
        content = re.sub(r'<[^>]+>', '', content)
        return content.strip()

    def load_documents(self) -> List[Dict]:
        documents = []
        # Walk through module directories
        for module_dir in glob.glob(os.path.join(DOCS_PATH, "module*")):
            module_name = os.path.basename(module_dir)
            for file_path in glob.glob(os.path.join(module_dir, "*.mdx")):
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                    
                cleaned_content = self.clean_mdx(content)
                chapter_name = os.path.basename(file_path).replace(".mdx", "")
                
                documents.append({
                    "content": cleaned_content,
                    "metadata": {
                        "module": module_name,
                        "chapter": chapter_name,
                        "source": file_path
                    }
                })
        return documents

    async def ingest(self):
        print("Creating Qdrant collection...")
        qdrant_service.create_collection_if_not_exists()
        
        print(f"Loading documents from {DOCS_PATH}...")
        docs = self.load_documents()
        print(f"Found {len(docs)} chapters.")

        points = []
        point_id = 0

        for doc in docs:
            chunks = self.text_splitter.split_text(doc["content"])
            print(f"Processing {doc['metadata']['chapter']}: {len(chunks)} chunks")
            
            for chunk in chunks:
                # Generate embedding
                embedding = await gemini_service.get_embedding(chunk)
                
                # Create Payload
                payload = {
                    "content": chunk,
                    "module": doc["metadata"]["module"],
                    "chapter": doc["metadata"]["chapter"]
                }
                
                points.append(models.PointStruct(
                    id=point_id,
                    vector=embedding,
                    payload=payload
                ))
                point_id += 1

        print(f"Upserting {len(points)} points to Qdrant...")
        qdrant_service.upsert(points)
        print("Ingestion complete! 🚀")

if __name__ == "__main__":
    pipeline = IngestionPipeline()
    asyncio.run(pipeline.ingest())
