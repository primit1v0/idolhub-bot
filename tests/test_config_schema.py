"""
Tests for core/config_schema.py - Pydantic configuration validation.
"""

import pytest
from pydantic import ValidationError

from core.config_schema import (
    AgentSection,
    ApiSection,
    AppConfig,
    AppSection,
    LlmSection,
    LoggingSection,
    LongTermMemory,
    McpSection,
    MemorySection,
    PluginsSection,
    ProviderCredentials,
    ShortTermMemory,
    SkillsSection,
    TelegramSection,
    ToolsSection,
)


class TestAppSection:
    def test_valid_app_section(self):
        """Test valid app section configuration."""
        app = AppSection(
            name="test",
            mode="bot",
            debug=True,
            timezone="UTC"
        )
        assert app.name == "test"
        assert app.mode == "bot"
        assert app.debug is True
        assert app.timezone == "UTC"
    
    def test_invalid_mode(self):
        """Test invalid mode value."""
        with pytest.raises(ValidationError):
            AppSection(mode="invalid")
    
    def test_invalid_timezone(self):
        """Test invalid timezone value."""
        with pytest.raises(ValidationError) as exc_info:
            AppSection(timezone="Invalid/Timezone")
        assert "Invalid timezone" in str(exc_info.value)


class TestAgentSection:
    def test_valid_agent_section(self):
        """Test valid agent configuration."""
        agent = AgentSection(
            system_prompt="You are a helpful assistant",
            max_iterations=20,
            tools_enabled=True,
            memory_enabled=True
        )
        assert agent.max_iterations == 20
        assert agent.tools_enabled is True
    
    def test_max_iterations_bounds(self):
        """Test max_iterations validation bounds."""
        with pytest.raises(ValidationError):
            AgentSection(system_prompt="test", max_iterations=0)
        
        with pytest.raises(ValidationError):
            AgentSection(system_prompt="test", max_iterations=101)
    
    def test_empty_system_prompt(self):
        """Test empty system prompt validation."""
        with pytest.raises(ValidationError) as exc_info:
            AgentSection(system_prompt="   ")
        assert "at least 10 characters" in str(exc_info.value)


class TestTelegramSection:
    def test_valid_telegram_section(self):
        """Test valid Telegram configuration."""
        telegram = TelegramSection(
            token="123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11",
            allowed_users=[123, 456],
            parse_mode="Markdown"
        )
        assert len(telegram.allowed_users) == 2
    
    def test_invalid_token_format(self):
        """Test invalid token format."""
        with pytest.raises(ValidationError) as exc_info:
            TelegramSection(token="invalid_token")
        assert "Invalid Telegram token format" in str(exc_info.value)
    
    def test_invalid_user_id(self):
        """Test invalid user ID (negative)."""
        with pytest.raises(ValidationError) as exc_info:
            TelegramSection(
                token="123:abc",
                allowed_users=[-1]
            )
        assert "Must be positive integer" in str(exc_info.value)


class TestLlmSection:
    def test_valid_llm_section(self):
        """Test valid LLM configuration."""
        llm = LlmSection(
            provider="openai",
            model="gpt-4",
            temperature=0.7,
            max_tokens=2000
        )
        assert llm.temperature == 0.7
    
    def test_temperature_bounds(self):
        """Test temperature validation bounds."""
        with pytest.raises(ValidationError):
            LlmSection(provider="openai", model="gpt-4", temperature=-0.1)
        
        with pytest.raises(ValidationError):
            LlmSection(provider="openai", model="gpt-4", temperature=2.1)


class TestProviderCredentials:
    def test_valid_provider_with_api_key(self):
        """Test valid provider with API key."""
        provider = ProviderCredentials(
            base_url="https://api.openai.com/v1",
            api_key="sk-test123"
        )
        assert provider.api_key == "sk-test123"
    
    def test_invalid_base_url(self):
        """Test invalid base URL format."""
        with pytest.raises(ValidationError) as exc_info:
            ProviderCredentials(
                base_url="invalid-url",
                api_key="test"
            )
        assert "Must start with http://" in str(exc_info.value)
    
    def test_no_credentials(self):
        """Test provider without any credentials."""
        with pytest.raises(ValidationError) as exc_info:
            ProviderCredentials(base_url="https://api.test.com")
        assert "at least one credential" in str(exc_info.value)


class TestMemorySection:
    def test_valid_memory_section(self):
        """Test valid memory configuration."""
        memory = MemorySection(
            short_term=ShortTermMemory(
                backend="sqlite",
                path="./data/test.db",
                max_messages=100
            ),
            long_term=LongTermMemory(
                backend="none",
                path="./data/vectors.db"
            )
        )
        assert memory.short_term.max_messages == 100
    
    def test_max_messages_bounds(self):
        """Test max_messages validation bounds."""
        with pytest.raises(ValidationError):
            ShortTermMemory(max_messages=0)
        
        with pytest.raises(ValidationError):
            ShortTermMemory(max_messages=10001)


class TestApiSection:
    def test_valid_api_section(self):
        """Test valid API configuration."""
        api = ApiSection(
            enabled=True,
            host="0.0.0.0",
            port=8000
        )
        assert api.port == 8000
    
    def test_port_bounds(self):
        """Test port validation bounds."""
        with pytest.raises(ValidationError):
            ApiSection(port=0)
        
        with pytest.raises(ValidationError):
            ApiSection(port=65536)


class TestAppConfig:
    def test_valid_full_config(self):
        """Test valid complete configuration."""
        config = AppConfig(
            app=AppSection(name="test", mode="bot"),
            agent=AgentSection(system_prompt="Test prompt"),
            telegram=TelegramSection(token="123:abc"),
            llm=LlmSection(provider="openai", model="gpt-4"),
            providers={
                "openai": ProviderCredentials(
                    base_url="https://api.openai.com/v1",
                    api_key="sk-test"
                )
            },
            memory=MemorySection(
                short_term=ShortTermMemory(),
                long_term=LongTermMemory()
            ),
            skills=SkillsSection(),
            tools=ToolsSection(),
            plugins=PluginsSection(),
            api=ApiSection(),
            mcp=McpSection(),
            logging=LoggingSection()
        )
        assert config.app.name == "test"
    
    def test_provider_not_found(self):
        """Test validation when selected provider doesn't exist."""
        with pytest.raises(ValidationError) as exc_info:
            AppConfig(
                app=AppSection(),
                agent=AgentSection(system_prompt="Test prompt for validation"),
                telegram=TelegramSection(token="123:abc"),
                llm=LlmSection(provider="nonexistent", model="test"),
                providers={
                    "openai": ProviderCredentials(
                        base_url="https://api.openai.com/v1",
                        api_key="sk-test"
                    )
                },
                memory=MemorySection(
                    short_term=ShortTermMemory(),
                    long_term=LongTermMemory()
                ),
                skills=SkillsSection(),
                tools=ToolsSection(),
                plugins=PluginsSection(),
                api=ApiSection(),
                mcp=McpSection(),
                logging=LoggingSection()
            )
        assert "not found in providers" in str(exc_info.value)
    
    def test_api_mode_disabled(self):
        """Test validation when API mode selected but disabled."""
        with pytest.raises(ValidationError) as exc_info:
            AppConfig(
                app=AppSection(mode="api"),
                agent=AgentSection(system_prompt="Test prompt for validation"),
                telegram=TelegramSection(token="123:abc"),
                llm=LlmSection(provider="openai", model="test"),
                providers={
                    "openai": ProviderCredentials(
                        base_url="https://api.openai.com/v1",
                        api_key="sk-test"
                    )
                },
                memory=MemorySection(
                    short_term=ShortTermMemory(),
                    long_term=LongTermMemory()
                ),
                skills=SkillsSection(),
                tools=ToolsSection(),
                plugins=PluginsSection(),
                api=ApiSection(enabled=False),
                mcp=McpSection(),
                logging=LoggingSection()
            )
        assert "Cannot run in 'api' mode" in str(exc_info.value)
    
    def test_port_conflict(self):
        """Test validation when API and MCP use same port."""
        with pytest.raises(ValidationError) as exc_info:
            AppConfig(
                app=AppSection(),
                agent=AgentSection(system_prompt="Test prompt for validation"),
                telegram=TelegramSection(token="123:abc"),
                llm=LlmSection(provider="openai", model="test"),
                providers={
                    "openai": ProviderCredentials(
                        base_url="https://api.openai.com/v1",
                        api_key="sk-test"
                    )
                },
                memory=MemorySection(
                    short_term=ShortTermMemory(),
                    long_term=LongTermMemory()
                ),
                skills=SkillsSection(),
                tools=ToolsSection(),
                plugins=PluginsSection(),
                api=ApiSection(port=8000),
                mcp=McpSection(port=8000),
                logging=LoggingSection()
            )
        assert "cannot use the same port" in str(exc_info.value)
