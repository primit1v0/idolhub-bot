import json
import os
import time
from pathlib import Path


def get_ram_usage_mb() -> int:
    """Baca RAM tersedia dari /proc/meminfo (dalam MB)"""
    try:
        with open("/proc/meminfo", "r") as f:
            for line in f:
                if line.startswith("MemAvailable:"):
                    available_kb = int(line.split()[1])
                    return available_kb // 1024
    except Exception:
        pass
    return 0

def get_disk_usage_gb(path="/") -> dict:
    """Cek disk usage via statvfs (dalam GB)"""
    try:
        stat = os.statvfs(path)
        total = stat.f_blocks * stat.f_frsize
        free = stat.f_bfree * stat.f_frsize
        used = total - free
        return {
            "total_gb": round(total / (1024**3), 2),
            "used_gb": round(used / (1024**3), 2),
            "free_gb": round(free / (1024**3), 2),
            "usage_percent": round((used / total) * 100, 2) if total > 0 else 0.0
        }
    except Exception:
        return {"total_gb": 0.0, "used_gb": 0.0, "free_gb": 0.0, "usage_percent": 0.0}

def get_cpu_load() -> list:
    """Baca 1, 5, 15 min load average"""
    try:
        with open("/proc/loadavg", "r") as f:
            load_avg = f.read().strip().split()[:3]
        return [float(x) for x in load_avg]
    except Exception:
        return [0.0, 0.0, 0.0]

def save_heartbeat():
    """Simpan data heartbeat ke storage/heartbeat.json"""
    data = {
        "timestamp": int(time.time()),
        "pid": os.getpid(),
        "system": {
            "ram_available_mb": get_ram_usage_mb(),
            "disk": get_disk_usage_gb(),
            "cpu_load_avg": get_cpu_load()
        }
    }
    storage_dir = Path("storage")
    storage_dir.mkdir(exist_ok=True)
    with open(storage_dir / "heartbeat.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    return data

if __name__ == "__main__":
    save_heartbeat()
