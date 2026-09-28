from fastapi import FastAPI
from pydantic import BaseModel

from app.retrieve import search

app = FastAPI(title="AI Career RAG API")


class SearchRequest(BaseModel):
    query: str
    n_results: int = 6


@app.get("/")
def health_check():
    return {"status": "AI Career RAG API is running"}


@app.post("/search")
def search_knowledge(request: SearchRequest):
    results = search(request.query, request.n_results)

    return {
        "query": request.query,
        "results": results
    }