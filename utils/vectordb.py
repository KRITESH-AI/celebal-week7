import os
import pickle
import faiss
import numpy as np

class VectorDatabase:

    def __init__(self, db_path="vectorstore"):

        self.db_path = db_path
        os.makedirs(self.db_path, exist_ok=True)

        self.index = None

        self.index_file = os.path.join(self.db_path, "faiss_index.bin")
        self.chunk_file = os.path.join(self.db_path, "chunks.pkl")
        self.meta_file = os.path.join(self.db_path, "metadata.pkl")


    def build_index(self, embeddings):

        dimension = embeddings.shape[1]

        self.index = faiss.IndexFlatIP(dimension)

        self.index.add(
            np.asarray(
                embeddings,
                dtype=np.float32
            )
        )

        print("\n========== VECTOR DATABASE ==========")
        print(f"Embedding Dimension : {dimension}")
        print(f"Vectors Stored      : {self.index.ntotal}")
        print("Similarity Metric   : Cosine Similarity")
        print("FAISS Index         : IndexFlatIP")
        print("=====================================\n")

    def save(self, chunks):

        if self.index is None:
            raise RuntimeError(
                "Vector index has not been created."
            )

        faiss.write_index(
            self.index,
            self.index_file
        )

        with open(self.chunk_file, "wb") as f:
            pickle.dump(chunks, f)

        metadata = {
            "embedding_dimension": self.index.d,
            "index_type": "IndexFlatIP",
            "similarity": "Cosine Similarity"
        }

        with open(self.meta_file, "wb") as f:
            pickle.dump(metadata, f)

        print("Vector Database Saved Successfully.\n")

    def load(self):

        if not os.path.exists(self.index_file):
            raise FileNotFoundError(
                "\nFAISS index not found.\n"
                "Run 'python ingest.py' first."
            )

        if not os.path.exists(self.chunk_file):
            raise FileNotFoundError(
                "\nChunk metadata not found.\n"
                "Run 'python ingest.py' first."
            )

        self.index = faiss.read_index(
            self.index_file
        )

        with open(self.chunk_file, "rb") as f:
            chunks = pickle.load(f)


        if os.path.exists(self.meta_file):

            with open(self.meta_file, "rb") as f:
                metadata = pickle.load(f)

            if metadata["embedding_dimension"] != self.index.d:

                raise ValueError(
                    f"Embedding dimension mismatch.\n"
                    f"Index Dimension : {self.index.d}\n"
                    f"Metadata Dimension : {metadata['embedding_dimension']}\n\n"
                    "Please run 'python ingest.py' again."
                )

        return chunks


    def search(self, query_embedding, top_k=3):

        similarities, indices = self.index.search(
            np.asarray(
                query_embedding,
                dtype=np.float32
            ),
            top_k
        )

        return similarities, indices