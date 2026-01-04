import os

# Suspicious extensions
SUSPICIOUS_EXTENSIONS = {'.exe', '.scr', '.bat', '.ps1', '.vbs', '.js', '.jar'}

# Suspicious strings (simple byte content check)
SUSPICIOUS_STRINGS = [
    b'powershell',
    b'cmd.exe',
    b'wget',
    b'curl',
    b'base64',
    b'Invoke-Expression',
    b'eval(',
    b'exec('
]

def check_double_extension(filename):
    """
    Checks if the file has a double extension (e.g., .pdf.exe).
    """
    parts = filename.lower().split('.')
    if len(parts) >= 3:
        # Check if the last extension is executable-like
        last_ext = '.' + parts[-1]
        if last_ext in SUSPICIOUS_EXTENSIONS:
            return True
    return False

def check_extension(filename):
    """
    Checks if the file has a suspicious extension.
    """
    _, ext = os.path.splitext(filename.lower())
    return ext in SUSPICIOUS_EXTENSIONS

def check_suspicious_strings(filepath):
    """
    Scans the beginning and end of the file for suspicious strings.
    For performance, we don't scan the whole file if it's huge, 
    but for this MVP we'll scan the first 1MB.
    """
    found_strings = []
    try:
        with open(filepath, "rb") as f:
            content = f.read(1024 * 1024) # Read first 1MB
            for s in SUSPICIOUS_STRINGS:
                if s in content:
                    found_strings.append(s.decode('utf-8'))
    except IOError:
        pass
    return found_strings

def calculate_score(filename, filepath, is_signature_match):
    """
    Calculates a suspicion score.
    """
    score = 0
    reasons = []

    if is_signature_match:
        score += 10
        reasons.append("signature_match")

    if check_double_extension(filename):
        score += 3
        reasons.append("double_extension")
    
    if check_extension(filename):
        score += 2
        reasons.append("suspicious_extension")

    suspicious_strs = check_suspicious_strings(filepath)
    if suspicious_strs:
        score += 2 * len(suspicious_strs)
        reasons.append(f"suspicious_strings: {', '.join(suspicious_strs)}")

    return score, reasons
