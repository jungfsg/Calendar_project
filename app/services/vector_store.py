import chromadb
from chromadb.config import Settings
from typing import List, Optional
from app.core.config import get_settings

settings = get_settings()

class VectorStoreService:
    def __init__(self):
        self.client = chromadb.HttpClient(
            host=settings.CHROMADB_HOST,
            port=settings.CHROMADB_PORT
        )
        self.collection = self.client.get_or_create_collection(
            name="calendar_contexts",
            metadata={"description": "Calendar related context storage"}
        )

    async def add_context(
        self,
        texts: List[str],
        metadata: Optional[List[dict]] = None,
        ids: Optional[List[str]] = None
    ):
        """
        컨텍스트를 벡터 저장소에 추가합니다.
        """
        if metadata is None:
            metadata = [{}] * len(texts)
        if ids is None:
            ids = [f"doc_{i}" for i in range(len(texts))]
        
        self.collection.add(
            documents=texts,
            metadatas=metadata,
            ids=ids
        )

    async def search_context(
        self,
        query: str,
        n_results: int = 5
    ) -> List[dict]:
        """
        쿼리와 관련된 컨텍스트를 검색합니다.
        """
        results = self.collection.query(
            query_texts=[query],
            n_results=n_results
        )
        
        return [
            {
                "text": doc,
                "metadata": meta,
                "distance": dist
            }
            for doc, meta, dist in zip(
                results["documents"][0],
                results["metadatas"][0],
                results["distances"][0]
            )
        ]

    async def delete_context(self, ids: List[str]):
        """
        특정 컨텍스트를 삭제합니다.
        """
        self.collection.delete(ids=ids) 