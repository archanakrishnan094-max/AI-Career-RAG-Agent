from pathlib import Path
import chromadb
from sentence_transformers import SentenceTransformer

from app.config import DOCUMENTS_DIR, CHROMA_DIR, COLLECTION_NAME


model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.PersistentClient(path=str(CHROMA_DIR))
collection = client.get_or_create_collection(COLLECTION_NAME)


def ingest_documents():
    documents = []
    ids = []

    for file in Path(DOCUMENTS_DIR).glob("*.txt"):
        text = file.read_text(encoding="utf-8-sig")

        # Keep each major section together as a retrieval unit
        sections = text.split("\n==================================================\n")

        for index, section in enumerate(sections):
            section = section.strip()

            if not section:
                continue

            documents.append(section)
            ids.append(f"{file.stem}_{index}")

    if documents:
        # Generate embeddings using Sentence Transformers
        embeddings = model.encode(documents).tolist()

        # Store documents and embeddings in ChromaDB
        collection.upsert(
            documents=documents,
            embeddings=embeddings,
            ids=ids
        )

    print(f"Ingested {len(documents)} chunks.")


if __name__ == "__main__":
    ingest_documents()
