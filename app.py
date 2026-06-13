from fastapi import FastAPI
from pydantic import BaseModel

from rag_pipeline import ask_rag

app = FastAPI(
    title="Python Programming Q&A Assistant"
)

class QuestionRequest(BaseModel):
    question: str

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

@app.post("/ask")
def ask(request: QuestionRequest):

    result = ask_rag(
        request.question
    )

    return result