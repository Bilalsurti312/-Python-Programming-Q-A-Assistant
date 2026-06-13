from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

THRESHOLD = 1.0

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = Chroma(
    persist_directory="./chroma_db",
    embedding_function=embedding_model
)

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

prompt = PromptTemplate(
    input_variables=["context", "question"],
    template="""
You are a Python Programming Assistant.

Use ONLY the provided context.

If the context contains information that answers the question,
provide a detailed answer.

If the context does NOT contain enough information,
respond exactly with:

"I could not find the answer in the provided knowledge base."

Context:
{context}

Question:
{question}

Answer:
"""
)

def ask_rag(query):

    docs_with_scores = vectorstore.similarity_search_with_score(
        query,
        k=5
    )

    if not docs_with_scores:
        return {
            "answer": "I could not find the answer in the provided knowledge base.",
            "sources": []
        }

    best_score = docs_with_scores[0][1]

    if best_score > THRESHOLD:
        return {
            "answer": "I could not find the answer in the provided knowledge base.",
            "sources": []
        }

    docs = [doc for doc, score in docs_with_scores]

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    final_prompt = prompt.format(
        context=context,
        question=query
    )

    response = llm.invoke(final_prompt)

    return {
        "answer": response.content,
        "sources": [
            doc.metadata
            for doc in docs
        ]
    }