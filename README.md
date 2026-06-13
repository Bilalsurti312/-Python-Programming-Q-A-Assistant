# Python Programming Q&A Assistant using LangChain, Qdrant Cloud, Groq, and FastAPI

## Note

The raw Stack Overflow dataset is excluded from GitHub due to its large size. The repository contains the complete source code, notebooks, API implementation, testing artifacts, deployment configuration, and documentation.

---

## Project Overview

This project is a Retrieval-Augmented Generation (RAG) based Python Programming Question Answering Assistant built using LangChain, Qdrant Cloud, Groq LLM, and FastAPI.

The system answers Python-related questions using a knowledge base constructed from 50,000 Stack Overflow Python question-answer pairs.

Responses are generated only from retrieved context, reducing hallucinations and ensuring grounded answers.

If relevant information is not available in the knowledge base, the system responds with:

"I could not find the answer in the provided knowledge base."

---

## Live Deployment

### Railway API URL

https://web-production-6bbe1.up.railway.app

### Swagger Documentation

https://web-production-6bbe1.up.railway.app/docs

### Health Check

https://web-production-6bbe1.up.railway.app/health

---

## Features

* Retrieval-Augmented Generation (RAG)
* Qdrant Cloud Vector Database
* HuggingFace Embeddings (all-MiniLM-L6-v2)
* Groq Llama 3.1 8B Instant Integration
* FastAPI REST API
* Railway Cloud Deployment
* Hallucination Prevention using Similarity Threshold
* Source Attribution
* API Testing and Evaluation

---

## Dataset

Source: Stack Overflow Python Question-Answer Dataset

Dataset Size:

* 50,000 Python Question-Answer Pairs

Fields Used:

* Title
* Question Body
* Answer Body
* Tags

---

## Technology Stack

* Python
* LangChain
* Qdrant Cloud
* HuggingFace Embeddings
* Groq (Llama 3.1 8B Instant)
* FastAPI
* Railway
* Pandas

---

## Project Structure

AnalyticsVidhya_Assessment/

├── 01_data_preparation.ipynb

├── 02_rag_pipeline.ipynb

├── 03_chatbot_app.ipynb

├── 04_api_testing.ipynb

├── 05_qdrant_migration.ipynb

├── rag_pipeline.py

├── app.py

├── requirements.txt

├── .env

├── .gitignore

└── README.md

---

## System Architecture

User Question

↓

FastAPI (/ask)

↓

Qdrant Cloud Retriever

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

Successful Response:

{
"answer": "...",
"sources": [...]
}

Out-of-Knowledge-Base Response:

{
"answer": "I could not find the answer in the provided knowledge base."
}

---

## Hallucination Prevention

A similarity score threshold is used to prevent the system from generating answers when relevant context is not available.

If the retrieved documents exceed the threshold, the system returns:

"I could not find the answer in the provided knowledge base."

This ensures that responses remain grounded in the knowledge base.

---

## Example Queries

### Valid Queries

* What is a Python decorator?
* What is a metaclass in Python?
* How do Python generators work?
* How do I execute shell commands from Python?

### Rejected Queries

* Who won FIFA World Cup 2022?
* What is the capital of France?
* Latest IPL winner

---

## Future Improvements

* Streamlit User Interface
* Hybrid Search
* Advanced Retrieval Techniques
* Conversation Memory
* User Authentication

---

## Author

Bilal Surti

Computer Engineering Graduate

AI / ML Engineer