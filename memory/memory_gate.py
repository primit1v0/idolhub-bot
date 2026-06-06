APPROVAL_KEYWORDS = ["SIMPAN KE MEMORI", "SAVE TO MEMORY"]
BLOCK_KEYWORDS = [
    "push", "commit", "delete", "send",
    "execute", "deploy", "run", "rm ", "rm -",
    "curl", "wget", "hapus", "kirim",
    "jalankan", "eksekusi",
]

def gate_write(content: str, user_message: str) -> dict:
    msg_upper = user_message.upper()
    # 1. Check approval keyword
    if not any(kw in msg_upper for kw in APPROVAL_KEYWORDS):
        return {
            "status": "REJECTED",
            "reason": "Penulisan memori ditolak. User harus mencantumkan instruksi eksplisit: 'SIMPAN KE MEMORI' atau 'SAVE TO MEMORY'."
        }
    
    # 2. Check dangerous keywords in content
    content_lower = content.lower()
    for kw in BLOCK_KEYWORDS:
        if kw in content_lower:
            return {
                "status": "REJECTED",
                "reason": f"Penulisan memori ditolak. Ditemukan indikasi perintah berbahaya: '{kw}'."
            }
            
    return {"status": "ALLOWED"}
