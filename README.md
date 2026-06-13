# Project Name: Python RAG Assistant using LangChain, ChromaDB, Groq, and FastAPI

## Project Overview:

This project is a Retrieval-Augmented Generation (RAG) based on Python Question Answering Assistant built using LangChain, ChromaDB, Groq LLM, and FastAPI(Swagger UI).

The system answers Python-related questions using a knowledge base constructed from Stack Overflow Python question-answer pairs. Responses are generated only from retrieved context, reducing hallucinations and ensuring grounded answers.

If relevant information is not available in the knowledge base, the system responds with:

"I could not find the answer in the provided knowledge base."

---

## Features:

* Retrieval-Augmented Generation (RAG)
* ChromaDB Vector Database
* HuggingFace Embeddings
* Groq Llama 3.1 Integration
* FastAPI REST API
* Hallucination Prevention using Similarity Threshold-1.0
* Source Attribution
* API Testing and Evaluation

---

## Dataset:

Source: Stack Overflow Python Question-Answer Dataset

Dataset Size:

* 50,000 Python Question-Answer pairs

Fields Used:

* Title
* Question Body
* Answer Body
* Tags

---

## Technology Stack

* Python
* LangChain
* ChromaDB
* HuggingFace Embeddings
* Groq (Llama 3.1 8B Instant)
* FastAPI
* Pandas

---

## Project Structure

AnalyticsVidhya_Assessment/

├── 01_data_preparation.ipynb

├── 02_rag_pipeline.ipynb

├── 03_chatbot_app.ipynb

├── 04_api_testing.ipynb

├── rag_pipeline.py

├── app.py

├── chroma_db/

├── .env

├── .gitignore

└── README.md

---

## System Architecture

User Question

↓

FastAPI (/ask)

↓

Retriever (ChromaDB)

↓

Top-K Relevant Documents

↓

Groq LLM

↓

Grounded Response

↓

JSON Response

---

## API Endpoints

### Health Check

GET /health

Response:

{
"status": "healthy"
}

### Ask Question

POST /ask

Request:

{
"question": "What is a Python decorator?"
}

Response:

{
"answer": "...",
"sources": [...]
}

---

## Hallucination Prevention

A similarity score threshold is used to prevent the system from generating answers when relevant context is not available.

If the retrieved documents exceed the threshold, the system returns:

"I could not find the answer in the provided knowledge base."

This ensures that answers remain grounded in the knowledge base.

---

## Example Queries

Valid Queries:

* What is a Python decorator?
* What is a metaclass in Python?
* How do Python generators work?
* How do I execute shell commands from Python?

Rejected Queries:

* Who won FIFA World Cup 2022?
* What is the capital of France?
* Latest IPL winner

---

## Future Improvements

* Streamlit User Interface
* Public Deployment
* Advanced Retrieval Techniques
* Hybrid Search
* Conversation Memory

---

## Author

Bilal Surti
Computer Engineering Graduate - AI/ML Engineer