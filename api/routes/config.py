# api/routes/config.py
from fastapi import APIRouter, Request, HTTPException
import json
import copy
from core.config import load_config, AppConfig, _resolve_dict

router = APIRouter()

def mask_secrets(data: dict) -> dict:
    masked = {}
    for k, v in data.items():
        if isinstance(v, dict):
            masked[k] = mask_secrets(v)
        elif isinstance(v, list):
            masked[k] = [mask_secrets(item) if isinstance(item, dict) else item for item in v]
        elif isinstance(v, str):
            if any(sec in k.lower() for sec in ["token", "key", "secret", "password"]):
                masked[k] = "********"
            else:
                masked[k] = v
        else:
            masked[k] = v
    return masked

@router.get("/config")
async def get_config(request: Request):
    cfg = getattr(request.app.state, "cfg", None)
    if not cfg:
        cfg = load_config()
    return {"config": mask_secrets(cfg.model_dump())}

@router.post("/config")
async def update_config(payload: dict, request: Request):
    # Load existing configuration data
    try:
        with open("config.json", "r", encoding="utf-8") as f:
            cfg_data = json.load(f)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to read config.json: {str(e)}")

    # Create in-memory copy to perform deep merge and validation
    merged_data = copy.deepcopy(cfg_data)
    
    def deep_update(d, u):
        for k, v in u.items():
            if isinstance(v, dict):
                d[k] = deep_update(d.get(k, {}), v)
            else:
                # Protect existing secrets from being overwritten by masks
                is_secret_key = any(sec in k.lower() for sec in ["token", "key", "secret", "password"])
                if is_secret_key and v == "********":
                    continue
                d[k] = v
        return d

    # Perform deep merge in memory
    try:
        deep_update(merged_data, payload)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to merge configuration updates: {str(e)}")

    # Resolve environment variables and validate in memory using Pydantic AppConfig schema
    try:
        resolved_data = _resolve_dict(merged_data)
        AppConfig(**resolved_data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Configuration validation failed: {str(e)}")

    # Write changes to config.json only after successful validation
    try:
        with open("config.json", "w", encoding="utf-8") as f:
            json.dump(merged_data, f, indent=2)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to save configuration: {str(e)}")

    try:
        # Reload active config
        updated_cfg = load_config()
        request.app.state.cfg = updated_cfg
        if hasattr(request.app.state, "agent"):
            # Close old agent connections
            await request.app.state.agent.close()
            # Recreate and initialize the agent with the new config
            from core.agent import IdolhubAgent
            new_agent = IdolhubAgent(updated_cfg)
            await new_agent.initialize()
            request.app.state.agent = new_agent
            
        return {"status": "success", "config": mask_secrets(updated_cfg.model_dump())}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to reload agent config: {str(e)}")
