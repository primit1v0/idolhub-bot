import os
import re
import json
from typing import Any, Dict, List, Literal, Optional
from pydantic import BaseModel, Field

def resolve_env(value: str) -> str:
    """Resolve $VAR_NAME tokens in a string using os.environ."""
    if not isinstance(value, str):
        return value
    
    # Matches $VAR_NAME (letters, numbers, underscores, must start with letter/underscore)
    pattern = re.compile(r'\$([A-Z_][A-Z0-9_]*)')
    
    def replacer(match: re.Match) -> str:
        var_name = match.group(1)
        # Raises KeyError if not found, which is expected behavior for secrets
        return os.environ[var_name]
        
    return pattern.sub(replacer, value)

def _resolve_dict(data: Any) -> Any:
    """Recursively resolve $VAR_NAME in dictionaries and lists."""
    if isinstance(data, dict):
        return {k: _resolve_dict(v) for k, v in data.items() if not k.startswith("_")}
    elif isinstance(data, list):
        return [_resolve_dict(item) for item in data]
    elif isinstance(data, str):
        return resolve_env(data)
    else:
        return data


# --- Pydantic Schemas for Configuration ---

class AppSection(BaseModel):
    name: str = "idolhub"
    mode: Literal["bot", "api", "mcp"] = "bot"
    debug: bool = False
    timezone: str = "Asia/Jakarta"

class AgentSection(BaseModel):
    system_prompt: str
    max_iterations: int = 10
    tools_enabled: bool = True
    memory_enabled: bool = True

class TelegramSection(BaseModel):
    token: str
    allowed_users: List[int] = Field(default_factory=list)
    parse_mode: str = "Markdown"

class LlmSection(BaseModel):
    provider: str = "openai"
    model: str = "gpt-4o"
    temperature: float = 0.7
    max_tokens: int = 4096
    timeout: int = 30

class ProviderCredentials(BaseModel):
    base_url: str
    api_key: Optional[str] = None
    oauth_token: Optional[str] = None
    cli_token: Optional[str] = None

class ShortTermMemory(BaseModel):
    backend: Literal["sqlite"] = "sqlite"
    path: str = "./data/memory.db"
    max_messages: int = 50

class LongTermMemory(BaseModel):
    backend: Literal["none", "sqlite_vec"] = "none"
    path: str = "./data/vectors.db"

class MemorySection(BaseModel):
    short_term: ShortTermMemory
    long_term: LongTermMemory

class SkillsSection(BaseModel):
    dir: str = "./skills"
    enabled: List[str] = Field(default_factory=list)

class ToolsSection(BaseModel):
    dir: str = "./tools"
    enabled: List[str] = Field(default_factory=list)

class PluginsSection(BaseModel):
    dir: str = "./plugins"
    enabled: List[str] = Field(default_factory=list)

class ApiSection(BaseModel):
    enabled: bool = True
    host: str = "0.0.0.0"
    port: int = 8000
    cors_origins: List[str] = Field(default_factory=list)

class McpSection(BaseModel):
    enabled: bool = True
    port: int = 8001

class LoggingSection(BaseModel):
    level: str = "INFO"
    format: str = "text"

class AppConfig(BaseModel):
    app: AppSection
    agent: AgentSection
    telegram: TelegramSection
    llm: LlmSection
    providers: Dict[str, ProviderCredentials]
    memory: MemorySection
    skills: SkillsSection
    tools: ToolsSection
    plugins: PluginsSection
    api: ApiSection
    mcp: McpSection
    logging: LoggingSection

def load_config(path: str = "config.json") -> AppConfig:
    """Load config.json, resolve $VAR variables, and return strongly-typed Config."""
    with open(path, "r", encoding="utf-8") as f:
        raw_data = json.load(f)
        
    resolved_data = _resolve_dict(raw_data)
    return AppConfig(**resolved_data)
