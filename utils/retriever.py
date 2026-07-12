from utils.embeddings import EmbeddingModel
from utils.vectordb import VectorDatabase


class Retriever:
    """
    Retrieves the most relevant document chunks
    using semantic similarity search.
    """

    def __init__(self):

        print("Loading Retriever...")

        self.embedding_model = EmbeddingModel()

        self.vector_db = VectorDatabase()

        self.chunks = self.vector_db.load()

        print("Retriever Ready!\n")


    def retrieve(self, query, top_k=3, min_score=0.30):

        query_embedding = self.embedding_model.embed_query(query)

        similarities, indices = self.vector_db.search(
            query_embedding,
            top_k
        )

        retrieved_chunks = []

        for similarity, index in zip(similarities[0], indices[0]):

            if index == -1:
                continue

            if similarity < min_score:
                continue

            chunk = self.chunks[index].copy()
            chunk["similarity"] = float(similarity)

            retrieved_chunks.append(chunk)

        return retrieved_chunks