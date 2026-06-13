# Python Programming Q&A Assistant using LangChain, Qdrant Cloud, Groq, and FastAPI

## Note

The raw Stack Overflow dataset and Qdrant vector embeddings are excluded from GitHub due to their large size. The repository contains the complete source code, notebooks, API implementation, testing artifacts, deployment configuration, and documentation.

---

## Project Overview

This project is a Retrieval-Augmented Generation (RAG) based Python Programming Question Answering Assistant built using LangChain, Qdrant Cloud, Groq LLM, and FastAPI.

The system answers Python-related questions using a knowledge base constructed from 50,000 Stack Overflow Python question-answer pairs.

Responses are generated only from retrieved context, reducing hallucinations and ensuring grounded answers.

If relevant information is not available in the knowledge base, the system responds with:

> I could not find the answer in the provided knowledge base.

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

**Source:** Stack Overflow Python Question-Answer Dataset

**Dataset Size:**

* 50,000 Python Question-Answer Pairs

**Fields Used:**

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

## Environment Variables

Create a `.env` file in the project root directory:

```env
GROQ_API_KEY=YOUR_GROQ_API_KEY

QDRANT_URL=YOUR_QDRANT_URL

QDRANT_API_KEY=YOUR_QDRANT_API_KEY
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/Bilalsurti312/-Python-Programming-Q-A-Assistant.git

cd -Python-Programming-Q-A-Assistant
```

### Create Virtual Environment

```bash
python -m venv venv
```

**Windows**

```bash
venv\Scripts\activate
```

**Linux / Mac**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

Start the FastAPI server:

```bash
uvicorn app:app --reload
```

Application URL:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## Project Structure

```text
AnalyticsVidhya_Assessment/

├── 01_data_preparation.ipynb
├── 02_rag_pipeline.ipynb
├── 03_chatbot_app.ipynb
├── 04_api_testing.ipynb
├── 05_qdrant_migration.ipynb
├── rag_pipeline.py
├── app.py
├── requirements.txt
├── Architecture Diagram.png
├── .env.example
├── .gitignore
└── README.md
```

---

## System Architecture

![System Architecture](Architecture%20Diagram.png)

The system follows a Retrieval-Augmented Generation (RAG) architecture:

1. Stack Overflow Python Q&A Dataset (50,000 records)
2. Data Preparation and Cleaning
3. Text Chunking
4. Embedding Generation using HuggingFace
5. Storage in Qdrant Cloud Vector Database
6. Similarity Search Retrieval
7. Relevant Context Extraction
8. Answer Generation using Groq Llama 3.1
9. Grounded Response with Source Attribution

---

## API Endpoints

### Health Check

**GET /health**

Response:

```json
{
  "status": "healthy"
}
```

### Ask Question

**POST /ask**

Request:

```json
{
  "question": "What is a Python decorator?"
}
```

Successful Response:

```json
{
  "answer": "...",
  "sources": [...]
}
```

Out-of-Knowledge-Base Response:

```json
{
  "answer": "I could not find the answer in the provided knowledge base."
}
```

---

## Hallucination Prevention

A similarity score threshold is used to prevent the system from generating answers when relevant context is not available.

If the retrieved documents exceed the threshold, the system returns:

> I could not find the answer in the provided knowledge base.

This ensures that responses remain grounded in the knowledge base.

---

## Example Queries

### Valid Queries

* What is a Python decorator?
* What is a metaclass in Python?
* How do Python generators work?
* What are mutable and immutable types?
* How do I execute shell commands from Python?

### Rejected Queries

* Who won FIFA World Cup 2022?
* What is the capital of France?
* Latest IPL winner

---

## Observation

The system successfully answered Python-related questions using retrieved context from the knowledge base and correctly rejected out-of-domain questions.

---

## Repository

GitHub Repository:

https://github.com/Bilalsurti312/-Python-Programming-Q-A-Assistant

---

## Author

### Bilal Surti

Computer Engineering Graduate

AI / ML Engineer

**Skills**

* Python
* Machine Learning
* Deep Learning
* LangChain
* Qdrant Cloud
* FastAPI
* Retrieval-Augmented Generation (RAG)
* LLM Applications