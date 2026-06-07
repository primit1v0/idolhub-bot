import os
import shlex
import subprocess

from memory.memory_gate import gate_write
from tools.sandbox import wrap_bwrap

WORKSPACE_DIR = os.path.join(os.getcwd(), "workspace")
os.makedirs(WORKSPACE_DIR, exist_ok=True)

def execute_bash(command: str) -> str:
    """Eksekusi bash command secara aman via bwrap."""
    import logging
    logger = logging.getLogger("idolhub.tools")
    
    bwrap_cmd = wrap_bwrap(command, WORKSPACE_DIR, WORKSPACE_DIR)
    logger.info(f"Executing sandbox command: {shlex.join(bwrap_cmd)}")
    
    try:
        # Eksekusi dengan subprocess, timeout 30 detik
        result = subprocess.run(  # nosec
            bwrap_cmd, 
            shell=False, 
            text=True, 
            capture_output=True, 
            timeout=30
        )
        # Gabungkan stdout dan stderr
        output = result.stdout + result.stderr
        logger.info(f"Sandbox output: {output}")
        if not output.strip():
            output = "Berhasil dieksekusi (Tidak ada output)."
        return output
    except subprocess.TimeoutExpired:
        return "ERROR: Eksekusi gagal karena lebih dari 30 detik (Timeout)."
    except Exception as e:
        return f"ERROR Internal: {e}"

async def save_fact(entity: str, nilai: str, user_id: str, memory, user_input: str = "", gating_enabled: bool = True) -> str:
    """Menyimpan fakta pengguna dengan verifikasi keamanan."""
    if gating_enabled:
        gate_res = gate_write(f"{entity}: {nilai}", user_input)
        if gate_res["status"] == "REJECTED":
            return f"GATING ERROR: REJECTED - {gate_res['reason']}"
        
    fact_id = await memory.save_fakta(user_id, entity, nilai)
    return f"Fakta berhasil disimpan (ID: {fact_id})."

async def set_preference(kunci: str, nilai: str, user_id: str, memory, user_input: str = "", gating_enabled: bool = True) -> str:
    """Menyimpan preferensi pengguna dengan verifikasi keamanan."""
    if gating_enabled:
        gate_res = gate_write(f"{kunci}: {nilai}", user_input)
        if gate_res["status"] == "REJECTED":
            return f"GATING ERROR: REJECTED - {gate_res['reason']}"
        
    await memory.set_preferensi(user_id, kunci, nilai)
    return f"Preferensi {kunci} berhasil diset menjadi {nilai}."

def search_web(query: str) -> str:
    """Mencari informasi di internet/Wikipedia berdasarkan query yang diberikan."""
    import logging

    import httpx
    logger = logging.getLogger("idolhub.tools")
    logger.info(f"Executing web search for query: {query}")
    
    results = []
    
    # 1. Query DuckDuckGo Instant Answer API
    try:
        ddg_url = f"https://api.duckduckgo.com/?q={query}&format=json&no_html=1"
        response = httpx.get(ddg_url, headers={"User-Agent": "idolhub/0.1.0"}, timeout=10)
        if response.status_code == 200:
            data = response.json()
            abstract = data.get("AbstractText", "")
            if abstract:
                results.append(f"DuckDuckGo Abstract:\n{abstract}")
            
            related = data.get("RelatedTopics", [])
            if related:
                topics_text = []
                for topic in related[:3]:
                    if "Text" in topic:
                        topics_text.append(f"- {topic['Text']}")
                if topics_text:
                    results.append("Topik Terkait (DuckDuckGo):\n" + "\n".join(topics_text))
    except Exception as e:
        logger.warning(f"DuckDuckGo search failed: {e}")
        
    # 2. Query Indonesian Wikipedia Search API
    try:
        wiki_url_id = f"https://id.wikipedia.org/w/api.php?action=query&list=search&srsearch={query}&format=json"
        response = httpx.get(wiki_url_id, headers={"User-Agent": "idolhub/0.1.0"}, timeout=10)
        if response.status_code == 200:
            data = response.json()
            search_items = data.get("query", {}).get("search", [])
            if search_items:
                wiki_text = []
                for item in search_items[:3]:
                    title = item.get("title", "")
                    snippet = item.get("snippet", "")
                    snippet = snippet.replace("<span class=\"searchmatch\">", "").replace("</span>", "")
                    wiki_text.append(f"- **{title}**: {snippet}")
                if wiki_text:
                    results.append("Hasil Wikipedia (ID):\n" + "\n".join(wiki_text))
    except Exception as e:
        logger.warning(f"Indonesian Wikipedia search failed: {e}")

    # 3. Query English Wikipedia Search API
    try:
        wiki_url_en = f"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch={query}&format=json"
        response = httpx.get(wiki_url_en, headers={"User-Agent": "idolhub/0.1.0"}, timeout=10)
        if response.status_code == 200:
            data = response.json()
            search_items = data.get("query", {}).get("search", [])
            if search_items:
                wiki_text = []
                for item in search_items[:3]:
                    title = item.get("title", "")
                    snippet = item.get("snippet", "")
                    snippet = snippet.replace("<span class=\"searchmatch\">", "").replace("</span>", "")
                    wiki_text.append(f"- **{title}**: {snippet}")
                if wiki_text:
                    results.append("Hasil Wikipedia (EN):\n" + "\n".join(wiki_text))
    except Exception as e:
        logger.warning(f"English Wikipedia search failed: {e}")
        
    if not results:
        return f"Pencarian untuk '{query}' tidak menemukan hasil."
        
    return "\n\n".join(results)

# Tool Calling Schema (Format OpenAI)
TOOLS_SCHEMA = [
    {
        "type": "function",
        "function": {
            "name": "search_web",
            "description": "Mencari informasi di internet/web/Wikipedia untuk query/topik tertentu jika agent tidak mengetahui jawabannya atau butuh informasi terbaru.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Kata kunci pencarian (misal: 'perkembangan AI terbaru' atau 'kucing anggora')"
                    }
                },
                "required": ["query"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "execute_bash",
            "description": "Menjalankan bash command di Linux host system (Ubuntu). Agent dapat membaca file (cat), listing folder (ls), membuat file, dsb. Command berjalan secara aman di dalam Sandbox (Workspace directory).",
            "parameters": {
                "type": "object",
                "properties": {
                    "command": {
                        "type": "string",
                        "description": "Bash command valid (misal: 'ls -la' atau 'cat file.txt')"
                    }
                },
                "required": ["command"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "save_fact",
            "description": "Menyimpan fakta pengguna.",
            "parameters": {
                "type": "object",
                "properties": {
                    "entity": {
                        "type": "string",
                        "description": "Entitas atau subjek fakta (misal: 'nama', 'pekerjaan', 'hobi')"
                    },
                    "nilai": {
                        "type": "string",
                        "description": "Isi atau nilai dari fakta tersebut"
                    }
                },
                "required": ["entity", "nilai"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "set_preference",
            "description": "Menyimpan preferensi pengguna.",
            "parameters": {
                "type": "object",
                "properties": {
                    "kunci": {
                        "type": "string",
                        "description": "Kunci preferensi (misal: 'bahasa', 'tema', 'kecepatan_bicara')"
                    },
                    "nilai": {
                        "type": "string",
                        "description": "Isi atau nilai dari preferensi tersebut"
                    }
                },
                "required": ["kunci", "nilai"]
            }
        }
    }
]

# Mapping function
TOOLS_MAPPING = {
    "search_web": search_web,
    "execute_bash": execute_bash,
    "save_fact": save_fact,
    "set_preference": set_preference
}
