INJECTION_PATTERNS = [
    "ignore previous", "ignore all", "forget everything",
    "you are now", "act as", "pretend you",
    "lupakan semua", "abaikan instruksi",
    "kamu sekarang", "pura-pura",
]

def filter_query(query: str) -> dict:
    query_lower = query.lower()
    for pattern in INJECTION_PATTERNS:
        if pattern in query_lower:
            return {"status": "BLOCKED", "reason": f"Prompt injection: {pattern}"}
    return {"status": "ALLOWED"}
