from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
DOCUMENTS_DIR = DATA_DIR / "documents"

CHROMA_DIR = DATA_DIR / "chroma_db"
COLLECTION_NAME = "reviq_knowledge"