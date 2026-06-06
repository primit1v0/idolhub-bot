import os
import subprocess
import shlex
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

# Tool Calling Schema (Format OpenAI)
TOOLS_SCHEMA = [
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
    }
]

# Mapping function
TOOLS_MAPPING = {
    "execute_bash": execute_bash
}
