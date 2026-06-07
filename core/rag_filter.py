import logging
import re

logger = logging.getLogger("idolhub.security")

INJECTION_PATTERNS = [
    r"ignore\s+previous",
    r"ignore\s+all",
    r"forget\s+everything",
    r"you\s+are\s+now",
    r"act\s+as",
    r"pretend\s+you",
    r"lupakan\s+semua",
    r"abaikan\s+instruksi",
    r"kamu\s+sekarang",
    r"pura-pura\s+(?:menjadi|kamu|ialah|adalah)",
]

def filter_query(query: str) -> dict:
    if not isinstance(query, str):
        return {"status": "ALLOWED"}

    query_lower = query.lower()
    for pattern in INJECTION_PATTERNS:
        if re.search(r"\b" + pattern + r"\b", query_lower):
            logger.warning(f"Blocked prompt injection attempt matching pattern: '{pattern}'")
            return {"status": "BLOCKED", "reason": f"Prompt injection: {pattern}"}
    return {"status": "ALLOWED"}

