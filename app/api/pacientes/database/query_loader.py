from pathlib import Path

BASE_PATH = Path(__file__).resolve().parent.parent / "sql"

def load_query(path: str) -> str:
    with open(BASE_PATH / path, "r", encoding="utf-8") as f:
        return f.read()