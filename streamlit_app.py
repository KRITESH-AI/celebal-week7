import streamlit as st
from utils.retriever import Retriever
from utils.generator import AnswerGenerator


# -------------------------------
# Page Configuration
# -------------------------------

st.set_page_config(
    page_title="Document Question Answering (RAG)",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Document Question Answering System (RAG)")

st.markdown(
    """
Ask questions from your uploaded **PDF** or **TXT** documents using
**Retrieval-Augmented Generation (RAG)**.
"""
)

# -------------------------------
# Indexed Documents
# -------------------------------

st.info(
    """
### 📂 Currently Indexed Documents

- 📄 AI.pdf
- 📄 Resume.pdf
- 📄 sample.txt

Ask questions related to these documents.
"""
)

st.divider()


# -------------------------------
# Load Components
# -------------------------------

@st.cache_resource
def load_components():
    retriever = Retriever()
    generator = AnswerGenerator()
    return retriever, generator


try:
    retriever, generator = load_components()

except Exception as e:
    st.error(f"Failed to load the RAG pipeline.\n\n{e}")
    st.stop()


# -------------------------------
# Sidebar
# -------------------------------

st.sidebar.header("Retrieval Settings")

st.sidebar.subheader("📂 Indexed Documents")

st.sidebar.markdown("""
- 📄 **AI.pdf**
- 📄 **Resume.pdf**
- 📄 **sample.txt**
""")

st.sidebar.info(
    "Ask questions related to the above indexed documents."
)

st.sidebar.divider()

top_k = st.sidebar.slider(
    "Top-K Retrieval",
    min_value=1,
    max_value=5,
    value=3
)

show_context = st.sidebar.checkbox(
    "Show Retrieved Context",
    value=True
)

st.sidebar.divider()

st.sidebar.subheader("System Information")

st.sidebar.write("**Embedding Model**")
st.sidebar.caption("Sentence-Transformers (all-MiniLM-L6-v2)")

st.sidebar.write("**Vector Database**")
st.sidebar.caption("FAISS (IndexFlatIP - Cosine Similarity)")

st.sidebar.write("**Language Model**")
st.sidebar.caption("Google FLAN-T5 Base")

st.sidebar.success("✅ Vector Database Loaded")


# -------------------------------
# User Input
# -------------------------------

question = st.text_input(
    "Ask your question"
)


# -------------------------------
# Generate Answer
# -------------------------------

if st.button("Generate Answer", use_container_width=True):

    if not question.strip():
        st.warning("Please enter a question.")
        st.stop()

    with st.spinner("Searching documents..."):

        retrieved_chunks = retriever.retrieve(
            question,
            top_k=top_k
        )

    if not retrieved_chunks:
        st.warning(
            "No relevant information was found in the indexed documents."
        )
        st.stop()

    answer = generator.generate_answer(
        question,
        retrieved_chunks
    )

    st.subheader("Answer")

    st.success(answer)

    if show_context:

        st.subheader("Retrieved Context")

        for i, chunk in enumerate(retrieved_chunks, start=1):

            with st.expander(
                f"Chunk {i} | {chunk['source']} | Page {chunk['page']}"
            ):

                st.write(chunk["text"])

                st.caption(
                    f"Similarity Score: {chunk['similarity']:.4f}"
                )


st.divider()

st.caption(
    "Built using Sentence Transformers • FAISS • FLAN-T5 • Streamlit"
)