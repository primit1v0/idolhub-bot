from fastapi import APIRouter

from tools.heartbeat import get_cpu_load, get_disk_usage_gb, get_ram_usage_mb

router = APIRouter()

@router.get("/health")
async def health_check():
    return {
        "status": "ok",
        "app": "idolhub",
        "system": {
            "ram_available_mb": get_ram_usage_mb(),
            "disk": get_disk_usage_gb(),
            "cpu_load_avg": get_cpu_load()
        }
    }

