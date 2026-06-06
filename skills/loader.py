import os
import yaml
import logging
from typing import Tuple, Optional
from core.config import AppConfig
from core.llm import call_llm

logger = logging.getLogger("idolhub.skills")

def parse_skill_file(filepath: str) -> Optional[Tuple[dict, str]]:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
        
    if not content.startswith("---"):
        return None
        
    parts = content.split("---", 2)
    if len(parts) < 3:
        return None
        
    yaml_text = parts[1]
    markdown_body = parts[2].strip()
    
    try:
        metadata = yaml.safe_load(yaml_text)
        return metadata, markdown_body
    except Exception as e:
        logger.error(f"Failed to parse frontmatter YAML in {filepath}: {e}")
        return None

def make_tool_schema(metadata: dict) -> dict:
    properties = {}
    required = []
    
    params = metadata.get("parameters", {})
    if isinstance(params, dict):
        for param_name, param_cfg in params.items():
            param_type = param_cfg.get("type", "string")
            param_desc = param_cfg.get("description", "")
            properties[param_name] = {
                "type": param_type,
                "description": param_desc
            }
            if param_cfg.get("required", False):
                required.append(param_name)
            
    return {
        "type": "function",
        "function": {
            "name": metadata.get("name"),
            "description": metadata.get("description"),
            "parameters": {
                "type": "object",
                "properties": properties,
                "required": required
            }
        }
    }

def make_skill_runner(cfg: AppConfig, instructions: str, metadata: dict):
    async def run_skill(**kwargs) -> str:
        param_str = "\n".join(f"- {k}: {v}" for k, v in kwargs.items())
        prompt = f"""You are executing the skill: {metadata.get('name')}
Description: {metadata.get('description')}

Instructions to follow:
{instructions}

Input parameters:
{param_str}

Please execute the instructions and output only the final result.
"""
        messages = [{"role": "user", "content": prompt}]
        res = await call_llm(cfg, messages)
        if res["type"] == "text":
            return res["content"]
        else:
            return "Error: Skill execution generated tool calls, which is not supported in simple skill runner."
    return run_skill

def load_skills(skills_dir: str, cfg: AppConfig, tools_schema: list, tools_mapping: dict):
    if not os.path.exists(skills_dir):
        logger.warning(f"Skills directory {skills_dir} does not exist.")
        return

    enabled_skills = cfg.skills.enabled

    for filename in os.listdir(skills_dir):
        if filename.endswith(".md"):
            skill_name = filename[:-3]
            if enabled_skills and skill_name not in enabled_skills:
                continue
                
            filepath = os.path.join(skills_dir, filename)
            try:
                parsed = parse_skill_file(filepath)
                if not parsed:
                    continue
                metadata, instructions = parsed
                
                schema = make_tool_schema(metadata)
                runner = make_skill_runner(cfg, instructions, metadata)
                
                tools_schema.append(schema)
                tools_mapping[metadata["name"]] = runner
                logger.info(f"Loaded skill tool: {metadata['name']}")
            except Exception as e:
                logger.error(f"Failed to load skill {filename}: {e}", exc_info=True)
