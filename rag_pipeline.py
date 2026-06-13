from dotenv import load_dotenv
import os

from qdrant_client import QdrantClient
from langchain_qdrant import QdrantVectorStore
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

load_dotenv()

QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")

THRESHOLD = 1.0

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

client = QdrantClient(
    url=QDRANT_URL,
    api_key=QDRANT_API_KEY
)

vectorstore = QdrantVectorStore(
    client=client,
    collection_name="python_qa",
    embedding=embedding_model
)

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

prompt = PromptTemplate(
    input_variables=["context", "question"],
    template="""
You are a Python Programming Assistant.

Answer ONLY from the provided context.

Rules:
1. Do NOT add information that is not present in the context.
2. Do NOT use outside knowledge.
3. If the answer is not fully available in the context, respond exactly:
"I could not find the answer in the provided knowledge base."
4. Format answers using clear headings and bullet points.
5. Keep code examples only if they exist in the context.
6. Do not repeat information.

Context:
{context}

Question:
{question}

Answer:
"""
)


def ask_rag(query: str):

    docs_with_scores = vectorstore.similarity_search_with_score(
        query,
        k=5
    )

    if not docs_with_scores:
        return {
            "answer": "I could not find the answer in the provided knowledge base."
        }

    best_score = docs_with_scores[0][1]

    if best_score > THRESHOLD:
        return {
            "answer": "I could not find the answer in the provided knowledge base."
        }

    docs = [doc for doc, score in docs_with_scores]

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    final_prompt = prompt.format(
        context=context,
        question=query
    )

    response = llm.invoke(final_prompt)

    answer = response.content.strip()

# Remove excessive blank lines
    while "\n\n\n" in answer:
        answer = answer.replace("\n\n\n", "\n\n")

# Convert escaped newlines if present
    answer = answer.replace("\\n", "\n")

    if answer == "" or (
        "I could not find the answer in the provided knowledge base."
        in answer
    ):
        return {
            "answer": "I could not find the answer in the provided knowledge base."
        }

    return {
        "answer": answer,
        "sources": [
            doc.metadata
            for doc in docs
        ]
    }   