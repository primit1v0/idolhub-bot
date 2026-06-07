import sys
from unittest.mock import MagicMock, patch

import pytest

from core.config import AppConfig
from main import main


@pytest.fixture
def mock_cfg():
    cfg = MagicMock(spec=AppConfig)
    cfg.app = MagicMock()
    cfg.app.mode = "bot"
    cfg.logging = MagicMock()
    cfg.logging.level = "INFO"
    cfg.logging.format = "text"
    cfg.api = MagicMock()
    cfg.api.host = "127.0.0.1"
    cfg.api.port = 8000
    return cfg

@patch("main.load_config")
@patch("main.setup_logging")
@patch("main.TelegramBot")
def test_main_dispatch_bot_default(mock_bot_class, mock_setup_logging, mock_load_config, mock_cfg):
    mock_load_config.return_value = mock_cfg
    
    # Mock system arguments to have no extra arguments
    with patch.object(sys, "argv", ["main.py"]):
        main()
        
    mock_bot_class.assert_called_once_with(mock_cfg)
    mock_bot_class.return_value.run.assert_called_once()

@patch("main.load_config")
@patch("main.setup_logging")
@patch("uvicorn.run")
def test_main_dispatch_api_cli(mock_uvicorn_run, mock_setup_logging, mock_load_config, mock_cfg):
    mock_load_config.return_value = mock_cfg
    
    with patch.object(sys, "argv", ["main.py", "api"]):
        main()
        
    mock_uvicorn_run.assert_called_once_with("api.server:app", host="127.0.0.1", port=8000, reload=False)

@patch("main.load_config")
@patch("main.setup_logging")
@patch("mcp_server.server.run_mcp_server")
def test_main_dispatch_mcp_cli(mock_run_mcp, mock_setup_logging, mock_load_config, mock_cfg):
    mock_load_config.return_value = mock_cfg
    
    with patch.object(sys, "argv", ["main.py", "mcp"]):
        main()
        
    mock_run_mcp.assert_called_once()
