from langchain.text_splitter import RecursiveCharacterTextSplitter


class TextChunker:

    def __init__(
        self,
        chunk_size=500,
        chunk_overlap=100
    ):

        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap,
            separators=[
                "\n\n",
                "\n",
                ". ",
                " ",
                ""
            ]
        )

    def create_chunks(self, documents):

        chunks = []

        chunk_id = 1

        for doc in documents:

            split_text = self.splitter.split_text(doc["text"])

            for text in split_text:

        
                if not text.strip():
                    continue

                chunks.append(
                    {
                        "id": chunk_id,
                        "text": text,
                        "source": doc["source"],
                        "page": doc["page"]
                    }
                )

                chunk_id += 1

        return chunks

    def print_statistics(self, chunks):

        if not chunks:

            print("\nNo chunks were created.")
            print("Please check the documents in the data folder.\n")
            return

        lengths = [len(chunk["text"]) for chunk in chunks]

        print("\n========== CHUNK STATISTICS ==========")
        print(f"Chunk Size      : {self.chunk_size}")
        print(f"Chunk Overlap   : {self.chunk_overlap}")
        print(f"Total Chunks    : {len(chunks)}")
        print(f"Largest Chunk   : {max(lengths)}")
        print(f"Smallest Chunk  : {min(lengths)}")
        print(f"Average Length  : {sum(lengths) / len(lengths):.2f}")
        print("======================================")