from transformers import pipeline


class AnswerGenerator:

    def __init__(
        self,
        model_name="google/flan-t5-base"
    ):

        print("\nLoading FLAN-T5 Model...")

        self.model_name = model_name

        self.generator = pipeline(
    task="text2text-generation",
    model=self.model_name,
    max_new_tokens=40,
    do_sample=False
)

        print("FLAN-T5 Loaded Successfully!\n")

    def generate_answer(self, question, retrieved_chunks):
 
        if not retrieved_chunks:
            return "I could not find the answer in the provided documents."

        context = "\n\n".join(
            chunk["text"] for chunk in retrieved_chunks
        )

        prompt = f"""
You are a document question answering assistant.

Answer the question ONLY using the provided context.

Rules:
1. Do not use outside knowledge.
2. If the answer is not present in the context, reply:
"I could not find the answer in the provided documents."
3. Keep the answer concise.
4. Do not explain your reasoning.
5. Do not add extra information.

Context:
{context}

Question:
{question}

Answer:
"""

        result = self.generator(prompt)

        answer = result[0]["generated_text"].strip()

        if answer == "":
            return "I could not find the answer in the provided documents."

        return answer