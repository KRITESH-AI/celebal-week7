from sentence_transformers import SentenceTransformer


class EmbeddingModel:

    def __init__(
        self,
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    ):

        print("\nLoading Embedding Model...")

        self.model_name = model_name
        self.model = SentenceTransformer(self.model_name)

        print("Embedding Model Loaded Successfully!\n")

    def create_embeddings(self, chunks):

        texts = [chunk["text"] for chunk in chunks]

        embeddings = self.model.encode(
            texts,
            convert_to_numpy=True,
            show_progress_bar=True,
            normalize_embeddings=True
        )

        print("========== EMBEDDING STATISTICS ==========")
        print(f"Embedding Model     : {self.model_name}")
        print(f"Embedding Dimension : {embeddings.shape[1]}")
        print(f"Total Embeddings    : {embeddings.shape[0]}")
        print("Normalization       : Enabled")
        print("==========================================\n")

        return embeddings

    def embed_query(self, query):

        embedding = self.model.encode(
            [query],
            convert_to_numpy=True,
            normalize_embeddings=True
        )

        return embedding