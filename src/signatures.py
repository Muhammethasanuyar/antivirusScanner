import json
import os

def load_signatures(db_path):
    """
    Loads signatures from a JSON file.
    Expected format: ["hash1", "hash2", ...]
    """
    if not os.path.exists(db_path):
        return set()
    
    try:
        with open(db_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return set(data) # Use set for O(1) lookup
    except Exception as e:
        print(f"Error loading signatures from {db_path}: {e}")
        return set()

def match(file_hash, signatures):
    """
    Checks if the file hash exists in the loaded signatures.
    """
    if not file_hash:
        return False
    return file_hash in signatures
