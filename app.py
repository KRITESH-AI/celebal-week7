from utils.retriever import Retriever
from utils.generator import AnswerGenerator


def print_divider():
    print("=" * 70)

def main():

    print_divider()
    print("DOCUMENT QUESTION ANSWERING SYSTEM (RAG)")
    print_divider()


    retriever = Retriever()
    generator = AnswerGenerator()

    while True:

        question = input(
            "\nAsk a question (or type 'exit'): "
        ).strip()

       
        if question.lower() == "exit":
            print("\nThank you for using the RAG System.")
            break

       
        if question == "":
            print("Please enter a valid question.")
            continue

       
        retrieved_chunks = retriever.retrieve(
            question,
            top_k=3
        )

        if not retrieved_chunks:
            print("\nNo relevant information found.")
            continue

        print()
        print_divider()
        print("RETRIEVED CONTEXT")
        print_divider()

        for i, chunk in enumerate(retrieved_chunks, start=1):

            print(f"\nChunk {i}")
            print(f"Source      : {chunk['source']}")
            print(f"Page        : {chunk['page']}")
            print(f"Similarity  : {chunk['similarity']:.4f}")

            print("-" * 70)
            print(chunk["text"])

        answer = generator.generate_answer(
            question,
            retrieved_chunks
        )

        print()
        print_divider()
        print("ANSWER")
        print_divider()

        print(answer)


if __name__ == "__main__":
    main()