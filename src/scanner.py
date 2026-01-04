import os
from .hasher import sha256_file
from .signatures import match
from .rules import calculate_score

MAX_FILE_SIZE = 20 * 1024 * 1024 # 20MB

def scan_directory(path, signatures):
    """
    Recursively scans a directory for files.
    Returns a dictionary with scan results.
    """
    results = {
        "scanned_path": path,
        "total_files": 0,
        "detections": [],
        "clean": 0,
        "errors": []
    }

    if not os.path.exists(path):
        results["errors"].append(f"Path not found: {path}")
        return results

    for root, _, files in os.walk(path):
        for file in files:
            filepath = os.path.join(root, file)
            results["total_files"] += 1
            
            try:
                # Check file size
                file_size = os.path.getsize(filepath)
                if file_size > MAX_FILE_SIZE:
                   # Skip large files for MVP
                   continue

                # Hash
                file_hash = sha256_file(filepath)
                
                # Signature Check
                is_detected = match(file_hash, signatures)
                
                # Heuristics
                score, reasons = calculate_score(file, filepath, is_detected)
                
                # Determine Status
                status = "CLEAN"
                if is_detected:
                    status = "DETECTED"
                elif score >= 5:
                    status = "SUSPICIOUS"
                
                if status != "CLEAN":
                    results["detections"].append({
                        "file": filepath,
                        "sha256": file_hash,
                        "status": status,
                        "score": score,
                        "reasons": reasons
                    })
                else:
                    results["clean"] += 1

            except Exception as e:
                results["errors"].append(f"Error scanning {filepath}: {str(e)}")

    return results
