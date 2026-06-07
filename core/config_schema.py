"""
Enhanced Pydantic configuration schema with comprehensive validation.

This module provides strict type checking, validation rules, and clear error
messages for all configuration sections. It replaces the basic models in
config.py with enhanced versions that include:

- Field validators with custom error messages
- Cross-field validation
- Timezone validation
- Provider whitelist checking
- Port range validation
- Path existence checking
"""

import os
from typing import Dict, List, Literal, Optional

from pydantic import BaseModel, Field, field_validator, model_validator


class AppSection(BaseModel):
    """Application-level configuration."""
    
    name: str = Field(default="idolhub", min_length=1, max_length=100)
    mode: Literal["bot", "api", "mcp"] = "bot"
    debug: bool = False
    timezone: str = "Asia/Jakarta"
    
    @field_validator("timezone")
    @classmethod
    def validate_timezone(cls, v: str) -> str:
        """Validate timezone string against common timezones."""
        # Import here to avoid startup overhead
        try:
            import zoneinfo
            zoneinfo.ZoneInfo(v)
        except Exception:
            # Fallback to pytz if zoneinfo not available
            try:
                import pytz
                pytz.timezone(v)
            except Exception:
                raise ValueError(
                    f"Invalid timezone '{v}'. Must be a valid IANA timezone "
                    f"(e.g., 'Asia/Jakarta', 'UTC', 'America/New_York')"
                )
        return v


class AgentSection(BaseModel):
    """Agent behavior configuration."""
    
    system_prompt: str = Field(min_length=10)
    max_iterations: int = Field(default=10, ge=1, le=100)
    tools_enabled: bool = True
    memory_enabled: bool = True
    filter_enabled: bool = True
    gating_enabled: bool = True
    
    @field_validator("system_prompt")
    @classmethod
    def validate_system_prompt(cls, v: str) -> str:
        """Ensure system prompt is not empty or whitespace-only."""
        if not v.strip():
            raise ValueError("system_prompt cannot be empty or whitespace-only")
        return v


class TelegramSection(BaseModel):
    """Telegram bot configuration."""
    
    token: str = Field(min_length=1)
    allowed_users: List[int] = Field(default_factory=list)
    parse_mode: Literal["Markdown", "HTML", "MarkdownV2"] = "Markdown"
    
    @field_validator("token")
    @classmethod
    def validate_token(cls, v: str) -> str:
        """Validate Telegram token format (basic check)."""
        if not v.strip():
            raise ValueError("Telegram token cannot be empty")
        # Basic format check: should contain ':' and be numeric:alphanumeric
        if ":" not in v:
            raise ValueError(
                "Invalid Telegram token format. Expected format: 'bot_id:token'"
            )
        return v
    
    @field_validator("allowed_users")
    @classmethod
    def validate_allowed_users(cls, v: List[int]) -> List[int]:
        """Validate user IDs are positive integers."""
        for user_id in v:
            if user_id <= 0:
                raise ValueError(f"Invalid user ID {user_id}. Must be positive integer")
        return v


class LlmSection(BaseModel):
    """LLM provider configuration."""
    
    provider: str = Field(min_length=1)
    model: str = Field(min_length=1)
    temperature: float = Field(default=0.7, ge=0.0, le=2.0)
    max_tokens: int = Field(default=4096, ge=1, le=1000000)
    timeout: int = Field(default=30, ge=1, le=300)
    
    @field_validator("provider", "model")
    @classmethod
    def validate_not_empty(cls, v: str) -> str:
        """Ensure provider and model are not empty."""
        if not v.strip():
            raise ValueError("Field cannot be empty or whitespace-only")
        return v


class ProviderCredentials(BaseModel):
    """Provider authentication credentials."""
    
    base_url: str = Field(min_length=1)
    api_key: Optional[str] = None
    oauth_token: Optional[str] = None
    cli_token: Optional[str] = None
    
    @field_validator("base_url")
    @classmethod
    def validate_base_url(cls, v: str) -> str:
        """Validate base URL format."""
        if not v.strip():
            raise ValueError("base_url cannot be empty")
        if not (v.startswith("http://") or v.startswith("https://")):
            raise ValueError(
                f"Invalid base_url '{v}'. Must start with http:// or https://"
            )
        return v
    
    @model_validator(mode="after")
    def validate_has_credential(self) -> "ProviderCredentials":
        """Ensure at least one credential is provided."""
        if not any([self.api_key, self.oauth_token, self.cli_token]):
            raise ValueError(
                "Provider must have at least one credential: "
                "api_key, oauth_token, or cli_token"
            )
        return self


class ShortTermMemory(BaseModel):
    """Short-term memory configuration."""
    
    backend: Literal["sqlite"] = "sqlite"
    path: str = "./data/memory.db"
    max_messages: int = Field(default=50, ge=1, le=10000)
    fts_context_window: int = Field(default=2, ge=0, le=10)
    auto_prune_enabled: bool = True
    auto_prune_limit: int = Field(default=1000, ge=100, le=100000)
    
    @field_validator("path")
    @classmethod
    def validate_path(cls, v: str) -> str:
        """Validate database path and ensure directory exists."""
        if not v.strip():
            raise ValueError("Database path cannot be empty")
        
        # Ensure parent directory exists or can be created
        parent_dir = os.path.dirname(v)
        if parent_dir and not os.path.exists(parent_dir):
            try:
                os.makedirs(parent_dir, exist_ok=True)
            except Exception as e:
                raise ValueError(
                    f"Cannot create directory for database path '{v}': {e}"
                )
        return v


class LongTermMemory(BaseModel):
    """Long-term memory configuration."""
    
    backend: Literal["none", "sqlite_vec"] = "none"
    path: str = "./data/vectors.db"
    embedding_model: str = "text-embedding-3-small"
    
    @field_validator("path")
    @classmethod
    def validate_path(cls, v: str) -> str:
        """Validate database path and ensure directory exists."""
        if not v.strip():
            raise ValueError("Database path cannot be empty")
        
        parent_dir = os.path.dirname(v)
        if parent_dir and not os.path.exists(parent_dir):
            try:
                os.makedirs(parent_dir, exist_ok=True)
            except Exception as e:
                raise ValueError(
                    f"Cannot create directory for database path '{v}': {e}"
                )
        return v
    
    @field_validator("embedding_model")
    @classmethod
    def validate_embedding_model(cls, v: str) -> str:
        """Ensure embedding model is not empty."""
        if not v.strip():
            raise ValueError("embedding_model cannot be empty")
        return v


class MemorySection(BaseModel):
    """Memory system configuration."""
    
    short_term: ShortTermMemory
    long_term: LongTermMemory


class SkillsSection(BaseModel):
    """Skills system configuration."""
    
    dir: str = "./skills"
    enabled: List[str] = Field(default_factory=list)
    
    @field_validator("dir")
    @classmethod
    def validate_dir(cls, v: str) -> str:
        """Validate skills directory path."""
        if not v.strip():
            raise ValueError("Skills directory cannot be empty")
        return v


class ToolsSection(BaseModel):
    """Tools system configuration."""
    
    dir: str = "./tools"
    enabled: List[str] = Field(default_factory=list)
    
    @field_validator("dir")
    @classmethod
    def validate_dir(cls, v: str) -> str:
        """Validate tools directory path."""
        if not v.strip():
            raise ValueError("Tools directory cannot be empty")
        return v


class PluginsSection(BaseModel):
    """Plugins system configuration."""
    
    dir: str = "./plugins"
    enabled: List[str] = Field(default_factory=list)
    
    @field_validator("dir")
    @classmethod
    def validate_dir(cls, v: str) -> str:
        """Validate plugins directory path."""
        if not v.strip():
            raise ValueError("Plugins directory cannot be empty")
        return v


class ApiSection(BaseModel):
    """API server configuration."""
    
    enabled: bool = True
    host: str = "127.0.0.1"
    port: int = Field(default=8000, ge=1, le=65535)
    cors_origins: List[str] = Field(default_factory=list)
    
    @field_validator("host")
    @classmethod
    def validate_host(cls, v: str) -> str:
        """Validate host address."""
        if not v.strip():
            raise ValueError("API host cannot be empty")
        return v


class McpSection(BaseModel):
    """MCP server configuration."""
    
    enabled: bool = True
    port: int = Field(default=8001, ge=1, le=65535)


class LoggingSection(BaseModel):
    """Logging configuration."""
    
    level: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = "INFO"
    format: Literal["text", "json"] = "text"


class AppConfig(BaseModel):
    """Root configuration model with cross-section validation."""
    
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
    
    @model_validator(mode="after")
    def validate_provider_exists(self) -> "AppConfig":
        """Ensure selected LLM provider exists in providers dict."""
        if self.llm.provider not in self.providers:
            available = ", ".join(self.providers.keys())
            raise ValueError(
                f"Selected provider '{self.llm.provider}' not found in providers. "
                f"Available providers: {available}"
            )
        return self
    
    @model_validator(mode="after")
    def validate_mode_enabled(self) -> "AppConfig":
        """Ensure selected mode is enabled."""
        if self.app.mode == "api" and not self.api.enabled:
            raise ValueError(
                "Cannot run in 'api' mode when api.enabled is False. "
                "Set api.enabled to true or change app.mode."
            )
        if self.app.mode == "mcp" and not self.mcp.enabled:
            raise ValueError(
                "Cannot run in 'mcp' mode when mcp.enabled is False. "
                "Set mcp.enabled to true or change app.mode."
            )
        return self
    
    @model_validator(mode="after")
    def validate_port_conflicts(self) -> "AppConfig":
        """Ensure API and MCP ports don't conflict."""
        if self.api.enabled and self.mcp.enabled:
            if self.api.port == self.mcp.port:
                raise ValueError(
                    f"API and MCP cannot use the same port ({self.api.port}). "
                    "Change api.port or mcp.port to different values."
                )
        return self
