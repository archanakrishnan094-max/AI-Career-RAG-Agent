from pathlib import Path

from sentence_transformers import SentenceTransformer

from app.config import DOCUMENTS_DIR
from app.ingest import collection


# Use the same embedding model used during document ingestion
model = SentenceTransformer("all-MiniLM-L6-v2")


def search(query, n_results=6):
    query_lower = query.lower()

    # Always retrieve the complete projects file for project-related questions.
    project_keywords = [
        "all projects",
        "my projects",
        "list projects",
        "gtm automation projects",
        "gtm projects",
        "reviq",
        "rev iq",
        "revenue intelligence",
        "ai gtm copilot",
        "gtm copilot",
        "debugging challenges",
        "debugging",
        "troubleshooting",
    ]

    if any(keyword in query_lower for keyword in project_keywords):
        projects_file = Path(DOCUMENTS_DIR) / "projects.txt"

        if projects_file.exists():
            text = projects_file.read_text(encoding="utf-8-sig")
            return [text]

    # Generate an embedding for the user's question
    query_embedding = model.encode([query]).tolist()

    # Search ChromaDB using the same embedding model
    results = collection.query(
        query_embeddings=query_embedding,
        n_results=n_results
    )

    return results["documents"][0]
