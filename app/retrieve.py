from pathlib import Path

from sentence_transformers import SentenceTransformer

from app.config import DOCUMENTS_DIR
from app.ingest import collection


# Use the same embedding model used during document ingestion
model = SentenceTransformer("all-MiniLM-L6-v2")


def search(query, n_results=6):
    query_lower = query.lower()

    # Specific retrieval for AI Career RAG Agent questions.
    career_rag_keywords = [
        "ai career rag agent",
        "career rag agent",
        "career rag project",
        "status of the ai career rag agent",
        "current status of the ai career rag agent",
        "what is implemented in the ai career rag agent",
        "what is still in progress in the ai career rag agent",
    ]

    if any(keyword in query_lower for keyword in career_rag_keywords):
        projects_file = Path(DOCUMENTS_DIR) / "projects.txt"

        if projects_file.exists():
            text = projects_file.read_text(encoding="utf-8-sig")
            sections = text.split("\n==================================================\n")

            for section in sections:
                if "AI Career RAG Agent" in section:
                    return [section.strip()]

    # Retrieve the complete projects file for portfolio/project questions.
    project_keywords = [
        "all projects",
        "all of archana's projects",
        "all of archana projects",
        "archana's projects",
        "archana projects",
        "my projects",
        "list projects",
        "list all projects",
        "project inventory",
        "which projects",
        "what projects",
        "gtm automation projects",
        "gtm projects",
        "ai automation projects",
        "reviq",
        "rev iq",
        "revenue intelligence",
        "ai gtm copilot",
        "gtm copilot",
        "debugging challenges",
        "debugging",
        "troubleshooting",
        "technical challenge",
        "technical challenges",
        "challenge",
        "challenges",
        "how did you solve",
        "how did you fix",
        "how did you troubleshoot",
        "technical issue",
        "issues faced",
        "problems faced",
        "all 10 projects",
        "10 projects",
        "portfolio",
        "portfolio projects",
        "all projects in my portfolio",
        "list all 10 projects",
        "projects in my portfolio",
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
