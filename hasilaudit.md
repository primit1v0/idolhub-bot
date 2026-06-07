# idolhub Security & Quality Audit Report

**Generated:** 2026-06-07 04:23:47 UTC
**Project:** idolhub
**Location:** /home/sandi/PocketFlow/idolhub

---

## 1. Test Suite (pytest)

```
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-9.0.3, pluggy-1.6.0 -- /home/sandi/PocketFlow/idolhub/.venv/bin/python3
cachedir: .pytest_cache
rootdir: /home/sandi/PocketFlow/idolhub
configfile: pyproject.toml
plugins: anyio-4.13.0, asyncio-1.4.0
asyncio: mode=Mode.AUTO, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collecting ... collected 113 items

tests/test_agent.py::test_agent_simple_response FAILED                   [  0%]
tests/test_agent.py::test_agent_memory_tools_execution FAILED            [  1%]
tests/test_agent.py::test_agent_relevant_facts_injection FAILED          [  2%]
tests/test_agent.py::test_agent_fts_injection FAILED                     [  3%]
tests/test_agent.py::test_agent_facts_scoring FAILED                     [  4%]
tests/test_agent.py::test_agent_prompt_injection_blocking FAILED         [  5%]
tests/test_agent.py::test_agent_prompt_injection_after_before_message FAILED [  6%]
tests/test_agent.py::test_agent_memory_gating_unapproved FAILED          [  7%]
tests/test_agent.py::test_agent_rrf_merger FAILED                        [  7%]
tests/test_agent.py::test_agent_tools_filtering FAILED                   [  8%]
tests/test_agent.py::test_agent_tools_globally_disabled FAILED           [  9%]
tests/test_agent.py::test_agent_filter_disabled FAILED                   [ 10%]
tests/test_agent.py::test_agent_gating_disabled FAILED                   [ 11%]
tests/test_agent.py::test_agent_fts_threading_integration FAILED         [ 12%]
tests/test_agent.py::test_agent_semantic_rrf_integration FAILED          [ 13%]
tests/test_api.py::test_health_endpoint ERROR                            [ 14%]
tests/test_api.py::test_chat_endpoint ERROR                              [ 15%]
tests/test_api.py::test_get_config_masked ERROR                          [ 15%]
tests/test_api.py::test_update_config ERROR                              [ 16%]
tests/test_api.py::test_update_config_invalid_fails ERROR                [ 17%]
tests/test_api.py::test_update_config_secrets_overwrite_protection ERROR [ 18%]
tests/test_api.py::test_health_metrics ERROR                             [ 19%]
tests/test_api_server.py::test_app_instance ERROR                        [ 20%]
tests/test_api_server.py::test_app_lifespan ERROR                        [ 21%]
tests/test_api_server.py::test_cors_allow_credentials_wildcard ERROR     [ 22%]
tests/test_api_server.py::test_cors_allow_credentials_specific ERROR     [ 23%]
tests/test_config.py::test_resolve_env_success PASSED                    [ 23%]
tests/test_config.py::test_resolve_env_embedded PASSED                   [ 24%]
tests/test_config.py::test_resolve_env_missing_raises_error PASSED       [ 25%]
tests/test_config.py::test_resolve_env_no_var PASSED                     [ 26%]
tests/test_config.py::test_load_config_resolves_nested_dict FAILED       [ 27%]
tests/test_config.py::test_long_term_config_embedding_model FAILED       [ 28%]
tests/test_config_reloader.py::TestInitializeConfig::test_initialize_valid_config PASSED [ 29%]
tests/test_config_reloader.py::TestInitializeConfig::test_initialize_invalid_config PASSED [ 30%]
tests/test_config_reloader.py::TestGetCurrentConfig::test_get_config_after_init PASSED [ 30%]
tests/test_config_reloader.py::TestGetCurrentConfig::test_get_config_before_init PASSED [ 31%]
tests/test_config_reloader.py::TestReloadConfig::test_reload_valid_config PASSED [ 32%]
tests/test_config_reloader.py::TestReloadConfig::test_reload_invalid_config_rollback PASSED [ 33%]
tests/test_config_reloader.py::TestReloadConfig::test_reload_missing_file PASSED [ 34%]
tests/test_config_reloader.py::TestChangeHandlers::test_register_and_call_handler PASSED [ 35%]
tests/test_config_reloader.py::TestChangeHandlers::test_unregister_handler PASSED [ 36%]
tests/test_config_reloader.py::TestChangeHandlers::test_handler_error_doesnt_break_reload PASSED [ 37%]
tests/test_config_reloader.py::TestChangeHandlers::test_clear_handlers PASSED [ 38%]
tests/test_config_schema.py::TestAppSection::test_valid_app_section PASSED [ 38%]
tests/test_config_schema.py::TestAppSection::test_invalid_mode PASSED    [ 39%]
tests/test_config_schema.py::TestAppSection::test_invalid_timezone PASSED [ 40%]
tests/test_config_schema.py::TestAgentSection::test_valid_agent_section PASSED [ 41%]
tests/test_config_schema.py::TestAgentSection::test_max_iterations_bounds PASSED [ 42%]
tests/test_config_schema.py::TestAgentSection::test_empty_system_prompt PASSED [ 43%]
tests/test_config_schema.py::TestTelegramSection::test_valid_telegram_section PASSED [ 44%]
tests/test_config_schema.py::TestTelegramSection::test_invalid_token_format PASSED [ 45%]
tests/test_config_schema.py::TestTelegramSection::test_invalid_user_id PASSED [ 46%]
tests/test_config_schema.py::TestLlmSection::test_valid_llm_section PASSED [ 46%]
tests/test_config_schema.py::TestLlmSection::test_temperature_bounds PASSED [ 47%]
tests/test_config_schema.py::TestProviderCredentials::test_valid_provider_with_api_key PASSED [ 48%]
tests/test_config_schema.py::TestProviderCredentials::test_invalid_base_url PASSED [ 49%]
tests/test_config_schema.py::TestProviderCredentials::test_no_credentials PASSED [ 50%]
tests/test_config_schema.py::TestMemorySection::test_valid_memory_section PASSED [ 51%]
tests/test_config_schema.py::TestMemorySection::test_max_messages_bounds PASSED [ 52%]
tests/test_config_schema.py::TestApiSection::test_valid_api_section PASSED [ 53%]
tests/test_config_schema.py::TestApiSection::test_port_bounds PASSED     [ 53%]
tests/test_config_schema.py::TestAppConfig::test_valid_full_config PASSED [ 54%]
tests/test_config_schema.py::TestAppConfig::test_provider_not_found PASSED [ 55%]
tests/test_config_schema.py::TestAppConfig::test_api_mode_disabled PASSED [ 56%]
tests/test_config_schema.py::TestAppConfig::test_port_conflict PASSED    [ 57%]
tests/test_config_validator.py::TestResolveEnv::test_resolve_single_var PASSED [ 58%]
tests/test_config_validator.py::TestResolveEnv::test_resolve_multiple_vars PASSED [ 59%]
tests/test_config_validator.py::TestResolveEnv::test_missing_var_raises_error PASSED [ 60%]
tests/test_config_validator.py::TestResolveEnv::test_non_string_passthrough PASSED [ 61%]
tests/test_config_validator.py::TestLoadConfig::test_load_valid_config PASSED [ 61%]
tests/test_config_validator.py::TestLoadConfig::test_load_config_with_env_vars PASSED [ 62%]
tests/test_config_validator.py::TestLoadConfig::test_load_config_missing_file PASSED [ 63%]
tests/test_config_validator.py::TestLoadConfig::test_load_config_invalid_json PASSED [ 64%]
tests/test_config_validator.py::TestLoadConfig::test_load_config_missing_env_var PASSED [ 65%]
tests/test_config_validator.py::TestValidateCapabilityWhitelists::test_validate_with_existing_dirs PASSED [ 66%]
tests/test_config_validator.py::TestValidateCapabilityWhitelists::test_validate_missing_skills_dir PASSED [ 67%]
tests/test_config_validator.py::TestHelperFunctions::test_get_available_providers PASSED [ 68%]
tests/test_config_validator.py::TestHelperFunctions::test_get_enabled_capabilities PASSED [ 69%]
tests/test_llm.py::test_get_openai_client FAILED                         [ 69%]
tests/test_llm.py::test_get_github_copilot_client FAILED                 [ 70%]
tests/test_llm.py::test_get_openai_codex_client FAILED                   [ 71%]
tests/test_llm.py::test_get_gemini_client FAILED                         [ 72%]
tests/test_llm.py::test_invalid_provider_raises_error FAILED             [ 73%]
tests/test_main.py::test_main_dispatch_bot_default FAILED                [ 74%]
tests/test_main.py::test_main_dispatch_api_cli FAILED                    [ 75%]
tests/test_main.py::test_main_dispatch_mcp_cli FAILED                    [ 76%]
tests/test_mcp.py::test_mcp_server_tool_registry FAILED                  [ 76%]
tests/test_memory.py::test_sqlite_store_import_without_sqlite_vec PASSED [ 77%]
tests/test_memory.py::test_vector_init_missing_dependency_fails_before_opening_db FAILED [ 78%]
tests/test_memory.py::test_memory_add_and_get ERROR                      [ 79%]
tests/test_memory.py::test_memory_respects_max_messages ERROR            [ 80%]
tests/test_memory.py::test_memory_filters_out_invalid_roles ERROR        [ 81%]
tests/test_memory.py::test_memory_facts_eav ERROR                        [ 82%]
tests/test_memory.py::test_memory_preferences ERROR                      [ 83%]
tests/test_memory.py::test_jaccard_deduplication FAILED                  [ 84%]
tests/test_memory.py::test_fts5_search FAILED                            [ 84%]
tests/test_memory.py::test_fts5_context_threading FAILED                 [ 85%]
tests/test_memory.py::test_memory_auto_prune_enforced FAILED             [ 86%]
tests/test_memory.py::test_memory_auto_prune_disabled FAILED             [ 87%]
tests/test_memory.py::test_sqlite_store_vector_init FAILED               [ 88%]
tests/test_memory.py::test_sqlite_store_get_embedding FAILED             [ 89%]
tests/test_memory.py::test_sqlite_store_add_message_vector FAILED        [ 90%]
tests/test_memory.py::test_sqlite_store_add_message_vector_failure_falls_back FAILED [ 91%]
tests/test_memory.py::test_sqlite_store_search_semantic FAILED           [ 92%]
tests/test_rag_filter.py::test_filter_query_allowed PASSED               [ 92%]
tests/test_rag_filter.py::test_filter_query_blocked PASSED               [ 93%]
tests/test_rag_filter.py::test_filter_query_type_safety PASSED           [ 94%]
tests/test_sandbox.py::test_wrap_bwrap_formatting PASSED                 [ 95%]
tests/test_sandbox.py::test_wrap_bwrap_fallback_cwd PASSED               [ 96%]
tests/test_search.py::test_search_web_success PASSED                     [ 97%]
tests/test_search.py::test_search_web_no_results PASSED                  [ 98%]
tests/test_skills_plugins.py::test_event_bus_subscribe_emit PASSED       [ 99%]
tests/test_skills_plugins.py::test_skills_parsing PASSED                 [100%]

==================================== ERRORS ====================================
____________________ ERROR at setup of test_health_endpoint ____________________
tests/test_api.py:12: in mock_cfg
    return AppConfig.model_validate({
E   pydantic_core._pydantic_core.ValidationError: 3 validation errors for AppConfig
E   telegram.token
E     Value error, Invalid Telegram token format. Expected format: 'bot_id:token' [type=value_error, input_value='test', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
E   providers.openai.base_url
E     Value error, Invalid base_url 'dummy'. Must start with http:// or https:// [type=value_error, input_value='dummy', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
E   memory.long_term.path
E     Value error, Database path cannot be empty [type=value_error, input_value='', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
_____________________ ERROR at setup of test_chat_endpoint _____________________
tests/test_api.py:12: in mock_cfg
    return AppConfig.model_validate({
E   pydantic_core._pydantic_core.ValidationError: 3 validation errors for AppConfig
E   telegram.token
E     Value error, Invalid Telegram token format. Expected format: 'bot_id:token' [type=value_error, input_value='test', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
E   providers.openai.base_url
E     Value error, Invalid base_url 'dummy'. Must start with http:// or https:// [type=value_error, input_value='dummy', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
E   memory.long_term.path
E     Value error, Database path cannot be empty [type=value_error, input_value='', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
___________________ ERROR at setup of test_get_config_masked ___________________
tests/test_api.py:12: in mock_cfg
    return AppConfig.model_validate({
E   pydantic_core._pydantic_core.ValidationError: 3 validation errors for AppConfig
E   telegram.token
E     Value error, Invalid Telegram token format. Expected format: 'bot_id:token' [type=value_error, input_value='test', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
E   providers.openai.base_url
E     Value error, Invalid base_url 'dummy'. Must start with http:// or https:// [type=value_error, input_value='dummy', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
E   memory.long_term.path
E     Value error, Database path cannot be empty [type=value_error, input_value='', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
_____________________ ERROR at setup of test_update_config _____________________
tests/test_api.py:12: in mock_cfg
    return AppConfig.model_validate({
E   pydantic_core._pydantic_core.ValidationError: 3 validation errors for AppConfig
E   telegram.token
E     Value error, Invalid Telegram token format. Expected format: 'bot_id:token' [type=value_error, input_value='test', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
E   providers.openai.base_url
E     Value error, Invalid base_url 'dummy'. Must start with http:// or https:// [type=value_error, input_value='dummy', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
E   memory.long_term.path
E     Value error, Database path cannot be empty [type=value_error, input_value='', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
______________ ERROR at setup of test_update_config_invalid_fails ______________
tests/test_api.py:12: in mock_cfg
    return AppConfig.model_validate({
E   pydantic_core._pydantic_core.ValidationError: 3 validation errors for AppConfig
E   telegram.token
E     Value error, Invalid Telegram token format. Expected format: 'bot_id:token' [type=value_error, input_value='test', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
E   providers.openai.base_url
E     Value error, Invalid base_url 'dummy'. Must start with http:// or https:// [type=value_error, input_value='dummy', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
E   memory.long_term.path
E     Value error, Database path cannot be empty [type=value_error, input_value='', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
______ ERROR at setup of test_update_config_secrets_overwrite_protection _______
tests/test_api.py:12: in mock_cfg
    return AppConfig.model_validate({
E   pydantic_core._pydantic_core.ValidationError: 3 validation errors for AppConfig
E   telegram.token
E     Value error, Invalid Telegram token format. Expected format: 'bot_id:token' [type=value_error, input_value='test', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
E   providers.openai.base_url
E     Value error, Invalid base_url 'dummy'. Must start with http:// or https:// [type=value_error, input_value='dummy', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
E   memory.long_term.path
E     Value error, Database path cannot be empty [type=value_error, input_value='', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
____________________ ERROR at setup of test_health_metrics _____________________
tests/test_api.py:12: in mock_cfg
    return AppConfig.model_validate({
E   pydantic_core._pydantic_core.ValidationError: 3 validation errors for AppConfig
E   telegram.token
E     Value error, Invalid Telegram token format. Expected format: 'bot_id:token' [type=value_error, input_value='test', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
E   providers.openai.base_url
E     Value error, Invalid base_url 'dummy'. Must start with http:// or https:// [type=value_error, input_value='dummy', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
E   memory.long_term.path
E     Value error, Database path cannot be empty [type=value_error, input_value='', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
_____________________ ERROR at setup of test_app_instance ______________________
tests/test_api_server.py:10: in mock_cfg
    return AppConfig.model_validate({
E   pydantic_core._pydantic_core.ValidationError: 3 validation errors for AppConfig
E   telegram.token
E     Value error, Invalid Telegram token format. Expected format: 'bot_id:token' [type=value_error, input_value='test', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
E   providers.openai.base_url
E     Value error, Invalid base_url 'dummy'. Must start with http:// or https:// [type=value_error, input_value='dummy', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
E   memory.long_term.path
E     Value error, Database path cannot be empty [type=value_error, input_value='', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
_____________________ ERROR at setup of test_app_lifespan ______________________
tests/test_api_server.py:10: in mock_cfg
    return AppConfig.model_validate({
E   pydantic_core._pydantic_core.ValidationError: 3 validation errors for AppConfig
E   telegram.token
E     Value error, Invalid Telegram token format. Expected format: 'bot_id:token' [type=value_error, input_value='test', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
E   providers.openai.base_url
E     Value error, Invalid base_url 'dummy'. Must start with http:// or https:// [type=value_error, input_value='dummy', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
E   memory.long_term.path
E     Value error, Database path cannot be empty [type=value_error, input_value='', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
____________ ERROR at setup of test_cors_allow_credentials_wildcard ____________
tests/test_api_server.py:10: in mock_cfg
    return AppConfig.model_validate({
E   pydantic_core._pydantic_core.ValidationError: 3 validation errors for AppConfig
E   telegram.token
E     Value error, Invalid Telegram token format. Expected format: 'bot_id:token' [type=value_error, input_value='test', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
E   providers.openai.base_url
E     Value error, Invalid base_url 'dummy'. Must start with http:// or https:// [type=value_error, input_value='dummy', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
E   memory.long_term.path
E     Value error, Database path cannot be empty [type=value_error, input_value='', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
____________ ERROR at setup of test_cors_allow_credentials_specific ____________
tests/test_api_server.py:10: in mock_cfg
    return AppConfig.model_validate({
E   pydantic_core._pydantic_core.ValidationError: 3 validation errors for AppConfig
E   telegram.token
E     Value error, Invalid Telegram token format. Expected format: 'bot_id:token' [type=value_error, input_value='test', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
E   providers.openai.base_url
E     Value error, Invalid base_url 'dummy'. Must start with http:// or https:// [type=value_error, input_value='dummy', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
E   memory.long_term.path
E     Value error, Database path cannot be empty [type=value_error, input_value='', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
__________________ ERROR at setup of test_memory_add_and_get ___________________
tests/test_memory.py:88: in memory_store
    cfg = AppConfig.model_validate({
E   pydantic_core._pydantic_core.ValidationError: 4 validation errors for AppConfig
E   agent.system_prompt
E     String should have at least 10 characters [type=string_too_short, input_value='sys', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/string_too_short
E   telegram.token
E     Value error, Invalid Telegram token format. Expected format: 'bot_id:token' [type=value_error, input_value='test', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
E   providers.openai.base_url
E     Value error, Invalid base_url 'dummy'. Must start with http:// or https:// [type=value_error, input_value='dummy', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
E   memory.long_term.path
E     Value error, Database path cannot be empty [type=value_error, input_value='', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
_____________ ERROR at setup of test_memory_respects_max_messages ______________
tests/test_memory.py:88: in memory_store
    cfg = AppConfig.model_validate({
E   pydantic_core._pydantic_core.ValidationError: 4 validation errors for AppConfig
E   agent.system_prompt
E     String should have at least 10 characters [type=string_too_short, input_value='sys', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/string_too_short
E   telegram.token
E     Value error, Invalid Telegram token format. Expected format: 'bot_id:token' [type=value_error, input_value='test', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
E   providers.openai.base_url
E     Value error, Invalid base_url 'dummy'. Must start with http:// or https:// [type=value_error, input_value='dummy', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
E   memory.long_term.path
E     Value error, Database path cannot be empty [type=value_error, input_value='', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
___________ ERROR at setup of test_memory_filters_out_invalid_roles ____________
tests/test_memory.py:88: in memory_store
    cfg = AppConfig.model_validate({
E   pydantic_core._pydantic_core.ValidationError: 4 validation errors for AppConfig
E   agent.system_prompt
E     String should have at least 10 characters [type=string_too_short, input_value='sys', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/string_too_short
E   telegram.token
E     Value error, Invalid Telegram token format. Expected format: 'bot_id:token' [type=value_error, input_value='test', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
E   providers.openai.base_url
E     Value error, Invalid base_url 'dummy'. Must start with http:// or https:// [type=value_error, input_value='dummy', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
E   memory.long_term.path
E     Value error, Database path cannot be empty [type=value_error, input_value='', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
___________________ ERROR at setup of test_memory_facts_eav ____________________
tests/test_memory.py:88: in memory_store
    cfg = AppConfig.model_validate({
E   pydantic_core._pydantic_core.ValidationError: 4 validation errors for AppConfig
E   agent.system_prompt
E     String should have at least 10 characters [type=string_too_short, input_value='sys', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/string_too_short
E   telegram.token
E     Value error, Invalid Telegram token format. Expected format: 'bot_id:token' [type=value_error, input_value='test', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
E   providers.openai.base_url
E     Value error, Invalid base_url 'dummy'. Must start with http:// or https:// [type=value_error, input_value='dummy', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
E   memory.long_term.path
E     Value error, Database path cannot be empty [type=value_error, input_value='', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
__________________ ERROR at setup of test_memory_preferences ___________________
tests/test_memory.py:88: in memory_store
    cfg = AppConfig.model_validate({
E   pydantic_core._pydantic_core.ValidationError: 4 validation errors for AppConfig
E   agent.system_prompt
E     String should have at least 10 characters [type=string_too_short, input_value='sys', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/string_too_short
E   telegram.token
E     Value error, Invalid Telegram token format. Expected format: 'bot_id:token' [type=value_error, input_value='test', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
E   providers.openai.base_url
E     Value error, Invalid base_url 'dummy'. Must start with http:// or https:// [type=value_error, input_value='dummy', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
E   memory.long_term.path
E     Value error, Database path cannot be empty [type=value_error, input_value='', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
=================================== FAILURES ===================================
__________________________ test_agent_simple_response __________________________
tests/test_agent.py:11: in test_agent_simple_response
    cfg = AppConfig.model_validate({
E   pydantic_core._pydantic_core.ValidationError: 3 validation errors for AppConfig
E   telegram.token
E     Value error, Invalid Telegram token format. Expected format: 'bot_id:token' [type=value_error, input_value='test', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
E   providers.openai.base_url
E     Value error, Invalid base_url 'dummy'. Must start with http:// or https:// [type=value_error, input_value='dummy', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
E   memory.long_term.path
E     Value error, Database path cannot be empty [type=value_error, input_value='', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
______________________ test_agent_memory_tools_execution _______________________
tests/test_agent.py:55: in test_agent_memory_tools_execution
    cfg = AppConfig.model_validate({
E   pydantic_core._pydantic_core.ValidationError: 3 validation errors for AppConfig
E   telegram.token
E     Value error, Invalid Telegram token format. Expected format: 'bot_id:token' [type=value_error, input_value='test', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
E   providers.openai.base_url
E     Value error, Invalid base_url 'dummy'. Must start with http:// or https:// [type=value_error, input_value='dummy', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
E   memory.long_term.path
E     Value error, Database path cannot be empty [type=value_error, input_value='', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
_____________________ test_agent_relevant_facts_injection ______________________
tests/test_agent.py:137: in test_agent_relevant_facts_injection
    cfg = AppConfig.model_validate({
E   pydantic_core._pydantic_core.ValidationError: 3 validation errors for AppConfig
E   telegram.token
E     Value error, Invalid Telegram token format. Expected format: 'bot_id:token' [type=value_error, input_value='test', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
E   providers.openai.base_url
E     Value error, Invalid base_url 'dummy'. Must start with http:// or https:// [type=value_error, input_value='dummy', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
E   memory.long_term.path
E     Value error, Database path cannot be empty [type=value_error, input_value='', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
___________________________ test_agent_fts_injection ___________________________
tests/test_agent.py:204: in test_agent_fts_injection
    cfg = AppConfig.model_validate({
E   pydantic_core._pydantic_core.ValidationError: 4 validation errors for AppConfig
E   agent.system_prompt
E     String should have at least 10 characters [type=string_too_short, input_value='test', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/string_too_short
E   telegram.token
E     Value error, Invalid Telegram token format. Expected format: 'bot_id:token' [type=value_error, input_value='test', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
E   providers.openai.base_url
E     Value error, Invalid base_url 'dummy'. Must start with http:// or https:// [type=value_error, input_value='dummy', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
E   memory.long_term.path
E     Value error, Database path cannot be empty [type=value_error, input_value='', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
___________________________ test_agent_facts_scoring ___________________________
tests/test_agent.py:248: in test_agent_facts_scoring
    cfg = AppConfig.model_validate({
E   pydantic_core._pydantic_core.ValidationError: 4 validation errors for AppConfig
E   agent.system_prompt
E     String should have at least 10 characters [type=string_too_short, input_value='test', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/string_too_short
E   telegram.token
E     Value error, Invalid Telegram token format. Expected format: 'bot_id:token' [type=value_error, input_value='test', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
E   providers.openai.base_url
E     Value error, Invalid base_url 'dummy'. Must start with http:// or https:// [type=value_error, input_value='dummy', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
E   memory.long_term.path
E     Value error, Database path cannot be empty [type=value_error, input_value='', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
_____________________ test_agent_prompt_injection_blocking _____________________
tests/test_agent.py:298: in test_agent_prompt_injection_blocking
    cfg = AppConfig.model_validate({
E   pydantic_core._pydantic_core.ValidationError: 4 validation errors for AppConfig
E   agent.system_prompt
E     String should have at least 10 characters [type=string_too_short, input_value='test', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/string_too_short
E   telegram.token
E     Value error, Invalid Telegram token format. Expected format: 'bot_id:token' [type=value_error, input_value='test', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
E   providers.openai.base_url
E     Value error, Invalid base_url 'dummy'. Must start with http:// or https:// [type=value_error, input_value='dummy', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
E   memory.long_term.path
E     Value error, Database path cannot be empty [type=value_error, input_value='', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
_______________ test_agent_prompt_injection_after_before_message _______________
tests/test_agent.py:321: in test_agent_prompt_injection_after_before_message
    cfg = AppConfig.model_validate({
E   pydantic_core._pydantic_core.ValidationError: 4 validation errors for AppConfig
E   agent.system_prompt
E     String should have at least 10 characters [type=string_too_short, input_value='test', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/string_too_short
E   telegram.token
E     Value error, Invalid Telegram token format. Expected format: 'bot_id:token' [type=value_error, input_value='test', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
E   providers.openai.base_url
E     Value error, Invalid base_url 'dummy'. Must start with http:// or https:// [type=value_error, input_value='dummy', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
E   memory.long_term.path
E     Value error, Database path cannot be empty [type=value_error, input_value='', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
_____________________ test_agent_memory_gating_unapproved ______________________
tests/test_agent.py:374: in test_agent_memory_gating_unapproved
    cfg = AppConfig.model_validate({
E   pydantic_core._pydantic_core.ValidationError: 4 validation errors for AppConfig
E   agent.system_prompt
E     String should have at least 10 characters [type=string_too_short, input_value='test', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/string_too_short
E   telegram.token
E     Value error, Invalid Telegram token format. Expected format: 'bot_id:token' [type=value_error, input_value='test', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
E   providers.openai.base_url
E     Value error, Invalid base_url 'dummy'. Must start with http:// or https:// [type=value_error, input_value='dummy', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
E   memory.long_term.path
E     Value error, Database path cannot be empty [type=value_error, input_value='', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
____________________________ test_agent_rrf_merger _____________________________
tests/test_agent.py:412: in test_agent_rrf_merger
    cfg = AppConfig.model_validate({
E   pydantic_core._pydantic_core.ValidationError: 4 validation errors for AppConfig
E   agent.system_prompt
E     String should have at least 10 characters [type=string_too_short, input_value='test', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/string_too_short
E   telegram.token
E     Value error, Invalid Telegram token format. Expected format: 'bot_id:token' [type=value_error, input_value='test', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
E   providers.openai.base_url
E     Value error, Invalid base_url 'dummy'. Must start with http:// or https:// [type=value_error, input_value='dummy', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
E   memory.long_term.path
E     Value error, Database path cannot be empty [type=value_error, input_value='', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
__________________________ test_agent_tools_filtering __________________________
tests/test_agent.py:460: in test_agent_tools_filtering
    cfg = AppConfig.model_validate({
E   pydantic_core._pydantic_core.ValidationError: 4 validation errors for AppConfig
E   agent.system_prompt
E     String should have at least 10 characters [type=string_too_short, input_value='test', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/string_too_short
E   telegram.token
E     Value error, Invalid Telegram token format. Expected format: 'bot_id:token' [type=value_error, input_value='test', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
E   providers.openai.base_url
E     Value error, Invalid base_url 'dummy'. Must start with http:// or https:// [type=value_error, input_value='dummy', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
E   memory.long_term.path
E     Value error, Database path cannot be empty [type=value_error, input_value='', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
______________________ test_agent_tools_globally_disabled ______________________
tests/test_agent.py:489: in test_agent_tools_globally_disabled
    cfg = AppConfig.model_validate({
E   pydantic_core._pydantic_core.ValidationError: 4 validation errors for AppConfig
E   agent.system_prompt
E     String should have at least 10 characters [type=string_too_short, input_value='test', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/string_too_short
E   telegram.token
E     Value error, Invalid Telegram token format. Expected format: 'bot_id:token' [type=value_error, input_value='test', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
E   providers.openai.base_url
E     Value error, Invalid base_url 'dummy'. Must start with http:// or https:// [type=value_error, input_value='dummy', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
E   memory.long_term.path
E     Value error, Database path cannot be empty [type=value_error, input_value='', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
__________________________ test_agent_filter_disabled __________________________
tests/test_agent.py:522: in test_agent_filter_disabled
    cfg = AppConfig.model_validate({
E   pydantic_core._pydantic_core.ValidationError: 4 validation errors for AppConfig
E   agent.system_prompt
E     String should have at least 10 characters [type=string_too_short, input_value='test', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/string_too_short
E   telegram.token
E     Value error, Invalid Telegram token format. Expected format: 'bot_id:token' [type=value_error, input_value='test', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
E   providers.openai.base_url
E     Value error, Invalid base_url 'dummy'. Must start with http:// or https:// [type=value_error, input_value='dummy', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
E   memory.long_term.path
E     Value error, Database path cannot be empty [type=value_error, input_value='', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
__________________________ test_agent_gating_disabled __________________________
tests/test_agent.py:552: in test_agent_gating_disabled
    cfg = AppConfig.model_validate({
E   pydantic_core._pydantic_core.ValidationError: 4 validation errors for AppConfig
E   agent.system_prompt
E     String should have at least 10 characters [type=string_too_short, input_value='test', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/string_too_short
E   telegram.token
E     Value error, Invalid Telegram token format. Expected format: 'bot_id:token' [type=value_error, input_value='test', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
E   providers.openai.base_url
E     Value error, Invalid base_url 'dummy'. Must start with http:// or https:// [type=value_error, input_value='dummy', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
E   memory.long_term.path
E     Value error, Database path cannot be empty [type=value_error, input_value='', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
_____________________ test_agent_fts_threading_integration _____________________
tests/test_agent.py:606: in test_agent_fts_threading_integration
    cfg = AppConfig.model_validate({
E   pydantic_core._pydantic_core.ValidationError: 4 validation errors for AppConfig
E   agent.system_prompt
E     String should have at least 10 characters [type=string_too_short, input_value='test', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/string_too_short
E   telegram.token
E     Value error, Invalid Telegram token format. Expected format: 'bot_id:token' [type=value_error, input_value='test', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
E   providers.openai.base_url
E     Value error, Invalid base_url 'dummy'. Must start with http:// or https:// [type=value_error, input_value='dummy', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
E   memory.long_term.path
E     Value error, Database path cannot be empty [type=value_error, input_value='', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
_____________________ test_agent_semantic_rrf_integration ______________________
tests/test_agent.py:668: in test_agent_semantic_rrf_integration
    cfg = AppConfig.model_validate(
E   pydantic_core._pydantic_core.ValidationError: 2 validation errors for AppConfig
E   telegram.token
E     Value error, Invalid Telegram token format. Expected format: 'bot_id:token' [type=value_error, input_value='test', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
E   providers.openai.base_url
E     Value error, Invalid base_url 'dummy'. Must start with http:// or https:// [type=value_error, input_value='dummy', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
____________________ test_load_config_resolves_nested_dict _____________________
core/config_validator.py:112: in load_config
    config = AppConfig(**resolved_data)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^
E   pydantic_core._pydantic_core.ValidationError: 2 validation errors for AppConfig
E   agent.system_prompt
E     String should have at least 10 characters [type=string_too_short, input_value='test', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/string_too_short
E   telegram.token
E     Value error, Invalid Telegram token format. Expected format: 'bot_id:token' [type=value_error, input_value='secret-key', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error

During handling of the above exception, another exception occurred:
tests/test_config.py:48: in test_load_config_resolves_nested_dict
    cfg = load_config(str(config_file))
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
core/config_validator.py:114: in load_config
    raise ValueError(
E   ValueError: Configuration validation failed for /tmp/pytest-of-sandi/pytest-139/test_load_config_resolves_nest0/config.json:
E   2 validation errors for AppConfig
E   agent.system_prompt
E     String should have at least 10 characters [type=string_too_short, input_value='test', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/string_too_short
E   telegram.token
E     Value error, Invalid Telegram token format. Expected format: 'bot_id:token' [type=value_error, input_value='secret-key', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
____________________ test_long_term_config_embedding_model _____________________
core/config_validator.py:112: in load_config
    config = AppConfig(**resolved_data)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^
E   pydantic_core._pydantic_core.ValidationError: 3 validation errors for AppConfig
E   agent.system_prompt
E     String should have at least 10 characters [type=string_too_short, input_value='sys', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/string_too_short
E   telegram.token
E     Value error, Invalid Telegram token format. Expected format: 'bot_id:token' [type=value_error, input_value='test', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
E   providers.openai.base_url
E     Value error, Invalid base_url 'dummy'. Must start with http:// or https:// [type=value_error, input_value='dummy', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error

During handling of the above exception, another exception occurred:
tests/test_config.py:77: in test_long_term_config_embedding_model
    cfg = load_config(f.name)
          ^^^^^^^^^^^^^^^^^^^
core/config_validator.py:114: in load_config
    raise ValueError(
E   ValueError: Configuration validation failed for /tmp/tmp8ifaepy6.json:
E   3 validation errors for AppConfig
E   agent.system_prompt
E     String should have at least 10 characters [type=string_too_short, input_value='sys', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/string_too_short
E   telegram.token
E     Value error, Invalid Telegram token format. Expected format: 'bot_id:token' [type=value_error, input_value='test', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
E   providers.openai.base_url
E     Value error, Invalid base_url 'dummy'. Must start with http:// or https:// [type=value_error, input_value='dummy', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
____________________________ test_get_openai_client ____________________________
tests/test_llm.py:9: in test_get_openai_client
    cfg = AppConfig.model_validate({
E   pydantic_core._pydantic_core.ValidationError: 3 validation errors for AppConfig
E   agent.system_prompt
E     String should have at least 10 characters [type=string_too_short, input_value='sys', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/string_too_short
E   telegram.token
E     Value error, Invalid Telegram token format. Expected format: 'bot_id:token' [type=value_error, input_value='test', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
E   memory.long_term.path
E     Value error, Database path cannot be empty [type=value_error, input_value='', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
________________________ test_get_github_copilot_client ________________________
tests/test_llm.py:34: in test_get_github_copilot_client
    cfg = AppConfig.model_validate({
E   pydantic_core._pydantic_core.ValidationError: 3 validation errors for AppConfig
E   agent.system_prompt
E     String should have at least 10 characters [type=string_too_short, input_value='sys', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/string_too_short
E   telegram.token
E     Value error, Invalid Telegram token format. Expected format: 'bot_id:token' [type=value_error, input_value='test', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
E   memory.long_term.path
E     Value error, Database path cannot be empty [type=value_error, input_value='', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
_________________________ test_get_openai_codex_client _________________________
tests/test_llm.py:56: in test_get_openai_codex_client
    cfg = AppConfig.model_validate({
E   pydantic_core._pydantic_core.ValidationError: 3 validation errors for AppConfig
E   agent.system_prompt
E     String should have at least 10 characters [type=string_too_short, input_value='sys', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/string_too_short
E   telegram.token
E     Value error, Invalid Telegram token format. Expected format: 'bot_id:token' [type=value_error, input_value='test', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
E   memory.long_term.path
E     Value error, Database path cannot be empty [type=value_error, input_value='', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
____________________________ test_get_gemini_client ____________________________
tests/test_llm.py:78: in test_get_gemini_client
    cfg = AppConfig.model_validate({
E   pydantic_core._pydantic_core.ValidationError: 3 validation errors for AppConfig
E   agent.system_prompt
E     String should have at least 10 characters [type=string_too_short, input_value='sys', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/string_too_short
E   telegram.token
E     Value error, Invalid Telegram token format. Expected format: 'bot_id:token' [type=value_error, input_value='test', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
E   memory.long_term.path
E     Value error, Database path cannot be empty [type=value_error, input_value='', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
______________________ test_invalid_provider_raises_error ______________________
tests/test_llm.py:100: in test_invalid_provider_raises_error
    cfg = AppConfig.model_validate({
E   pydantic_core._pydantic_core.ValidationError: 3 validation errors for AppConfig
E   agent.system_prompt
E     String should have at least 10 characters [type=string_too_short, input_value='sys', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/string_too_short
E   telegram.token
E     Value error, Invalid Telegram token format. Expected format: 'bot_id:token' [type=value_error, input_value='test', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
E   memory.long_term.path
E     Value error, Database path cannot be empty [type=value_error, input_value='', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
________________________ test_main_dispatch_bot_default ________________________
core/config_validator.py:37: in replacer
    return os.environ[var_name]
           ^^^^^^^^^^^^^^^^^^^^
E   KeyError: 'TELEGRAM_BOT_TOKEN'

During handling of the above exception, another exception occurred:
core/config_validator.py:103: in load_config
    resolved_data = _resolve_dict(raw_data)
                    ^^^^^^^^^^^^^^^^^^^^^^^
core/config_validator.py:54: in _resolve_dict
    return {k: _resolve_dict(v) for k, v in data.items() if not k.startswith("_")}
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
core/config_validator.py:54: in <dictcomp>
    return {k: _resolve_dict(v) for k, v in data.items() if not k.startswith("_")}
               ^^^^^^^^^^^^^^^^
core/config_validator.py:54: in _resolve_dict
    return {k: _resolve_dict(v) for k, v in data.items() if not k.startswith("_")}
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
core/config_validator.py:54: in <dictcomp>
    return {k: _resolve_dict(v) for k, v in data.items() if not k.startswith("_")}
               ^^^^^^^^^^^^^^^^
core/config_validator.py:58: in _resolve_dict
    return resolve_env(data)
           ^^^^^^^^^^^^^^^^^
core/config_validator.py:44: in resolve_env
    return pattern.sub(replacer, value)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
core/config_validator.py:39: in replacer
    raise KeyError(
E   KeyError: 'Environment variable $TELEGRAM_BOT_TOKEN not found. Please set it before running the application.'

During handling of the above exception, another exception occurred:
main.py:34: in main
    cfg = initialize_config("config.json")
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
core/config_reloader.py:45: in initialize_config
    config = load_config(path)
             ^^^^^^^^^^^^^^^^^
core/config_validator.py:105: in load_config
    raise KeyError(
E   KeyError: "Configuration error in config.json: 'Environment variable $TELEGRAM_BOT_TOKEN not found. Please set it before running the application.'\nEnsure all $VARIABLE references have corresponding environment variables set."

During handling of the above exception, another exception occurred:
tests/test_main.py:31: in test_main_dispatch_bot_default
    main()
main.py:38: in main
    sys.exit(1)
E   SystemExit: 1
----------------------------- Captured stdout call -----------------------------
CRITICAL ERROR: Secret untuk "Configuration error in config.json: 'Environment variable $TELEGRAM_BOT_TOKEN not found. Please set it before running the application.'\nEnsure all $VARIABLE references have corresponding environment variables set." tidak ditemukan di environment!
Pastikan environment atau EnvironmentFile lokal sudah diisi.
__________________________ test_main_dispatch_api_cli __________________________
core/config_validator.py:37: in replacer
    return os.environ[var_name]
           ^^^^^^^^^^^^^^^^^^^^
E   KeyError: 'TELEGRAM_BOT_TOKEN'

During handling of the above exception, another exception occurred:
core/config_validator.py:103: in load_config
    resolved_data = _resolve_dict(raw_data)
                    ^^^^^^^^^^^^^^^^^^^^^^^
core/config_validator.py:54: in _resolve_dict
    return {k: _resolve_dict(v) for k, v in data.items() if not k.startswith("_")}
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
core/config_validator.py:54: in <dictcomp>
    return {k: _resolve_dict(v) for k, v in data.items() if not k.startswith("_")}
               ^^^^^^^^^^^^^^^^
core/config_validator.py:54: in _resolve_dict
    return {k: _resolve_dict(v) for k, v in data.items() if not k.startswith("_")}
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
core/config_validator.py:54: in <dictcomp>
    return {k: _resolve_dict(v) for k, v in data.items() if not k.startswith("_")}
               ^^^^^^^^^^^^^^^^
core/config_validator.py:58: in _resolve_dict
    return resolve_env(data)
           ^^^^^^^^^^^^^^^^^
core/config_validator.py:44: in resolve_env
    return pattern.sub(replacer, value)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
core/config_validator.py:39: in replacer
    raise KeyError(
E   KeyError: 'Environment variable $TELEGRAM_BOT_TOKEN not found. Please set it before running the application.'

During handling of the above exception, another exception occurred:
main.py:34: in main
    cfg = initialize_config("config.json")
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
core/config_reloader.py:45: in initialize_config
    config = load_config(path)
             ^^^^^^^^^^^^^^^^^
core/config_validator.py:105: in load_config
    raise KeyError(
E   KeyError: "Configuration error in config.json: 'Environment variable $TELEGRAM_BOT_TOKEN not found. Please set it before running the application.'\nEnsure all $VARIABLE references have corresponding environment variables set."

During handling of the above exception, another exception occurred:
tests/test_main.py:43: in test_main_dispatch_api_cli
    main()
main.py:38: in main
    sys.exit(1)
E   SystemExit: 1
----------------------------- Captured stdout call -----------------------------
CRITICAL ERROR: Secret untuk "Configuration error in config.json: 'Environment variable $TELEGRAM_BOT_TOKEN not found. Please set it before running the application.'\nEnsure all $VARIABLE references have corresponding environment variables set." tidak ditemukan di environment!
Pastikan environment atau EnvironmentFile lokal sudah diisi.
__________________________ test_main_dispatch_mcp_cli __________________________
core/config_validator.py:37: in replacer
    return os.environ[var_name]
           ^^^^^^^^^^^^^^^^^^^^
E   KeyError: 'TELEGRAM_BOT_TOKEN'

During handling of the above exception, another exception occurred:
core/config_validator.py:103: in load_config
    resolved_data = _resolve_dict(raw_data)
                    ^^^^^^^^^^^^^^^^^^^^^^^
core/config_validator.py:54: in _resolve_dict
    return {k: _resolve_dict(v) for k, v in data.items() if not k.startswith("_")}
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
core/config_validator.py:54: in <dictcomp>
    return {k: _resolve_dict(v) for k, v in data.items() if not k.startswith("_")}
               ^^^^^^^^^^^^^^^^
core/config_validator.py:54: in _resolve_dict
    return {k: _resolve_dict(v) for k, v in data.items() if not k.startswith("_")}
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
core/config_validator.py:54: in <dictcomp>
    return {k: _resolve_dict(v) for k, v in data.items() if not k.startswith("_")}
               ^^^^^^^^^^^^^^^^
core/config_validator.py:58: in _resolve_dict
    return resolve_env(data)
           ^^^^^^^^^^^^^^^^^
core/config_validator.py:44: in resolve_env
    return pattern.sub(replacer, value)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
core/config_validator.py:39: in replacer
    raise KeyError(
E   KeyError: 'Environment variable $TELEGRAM_BOT_TOKEN not found. Please set it before running the application.'

During handling of the above exception, another exception occurred:
main.py:34: in main
    cfg = initialize_config("config.json")
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
core/config_reloader.py:45: in initialize_config
    config = load_config(path)
             ^^^^^^^^^^^^^^^^^
core/config_validator.py:105: in load_config
    raise KeyError(
E   KeyError: "Configuration error in config.json: 'Environment variable $TELEGRAM_BOT_TOKEN not found. Please set it before running the application.'\nEnsure all $VARIABLE references have corresponding environment variables set."

During handling of the above exception, another exception occurred:
tests/test_main.py:54: in test_main_dispatch_mcp_cli
    main()
main.py:38: in main
    sys.exit(1)
E   SystemExit: 1
----------------------------- Captured stdout call -----------------------------
CRITICAL ERROR: Secret untuk "Configuration error in config.json: 'Environment variable $TELEGRAM_BOT_TOKEN not found. Please set it before running the application.'\nEnsure all $VARIABLE references have corresponding environment variables set." tidak ditemukan di environment!
Pastikan environment atau EnvironmentFile lokal sudah diisi.
________________________ test_mcp_server_tool_registry _________________________
tests/test_mcp.py:12: in test_mcp_server_tool_registry
    mock_cfg = AppConfig.model_validate({
E   pydantic_core._pydantic_core.ValidationError: 3 validation errors for AppConfig
E   telegram.token
E     Value error, Invalid Telegram token format. Expected format: 'bot_id:token' [type=value_error, input_value='test', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
E   providers.openai.base_url
E     Value error, Invalid base_url 'dummy'. Must start with http:// or https:// [type=value_error, input_value='dummy', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
E   memory.long_term.path
E     Value error, Database path cannot be empty [type=value_error, input_value='', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
_________ test_vector_init_missing_dependency_fails_before_opening_db __________
tests/test_memory.py:41: in test_vector_init_missing_dependency_fails_before_opening_db
    cfg = AppConfig.model_validate(
E   pydantic_core._pydantic_core.ValidationError: 3 validation errors for AppConfig
E   agent.system_prompt
E     String should have at least 10 characters [type=string_too_short, input_value='sys', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/string_too_short
E   telegram.token
E     Value error, Invalid Telegram token format. Expected format: 'bot_id:token' [type=value_error, input_value='test', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
E   providers.openai.base_url
E     Value error, Invalid base_url 'dummy'. Must start with http:// or https:// [type=value_error, input_value='dummy', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
__________________________ test_jaccard_deduplication __________________________
tests/test_memory.py:213: in test_jaccard_deduplication
    cfg = AppConfig.model_validate({
E   pydantic_core._pydantic_core.ValidationError: 4 validation errors for AppConfig
E   agent.system_prompt
E     String should have at least 10 characters [type=string_too_short, input_value='test', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/string_too_short
E   telegram.token
E     Value error, Invalid Telegram token format. Expected format: 'bot_id:token' [type=value_error, input_value='test', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
E   providers.openai.base_url
E     Value error, Invalid base_url 'dummy'. Must start with http:// or https:// [type=value_error, input_value='dummy', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
E   memory.long_term.path
E     Value error, Database path cannot be empty [type=value_error, input_value='', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
_______________________________ test_fts5_search _______________________________
tests/test_memory.py:250: in test_fts5_search
    cfg = AppConfig.model_validate({
E   pydantic_core._pydantic_core.ValidationError: 4 validation errors for AppConfig
E   agent.system_prompt
E     String should have at least 10 characters [type=string_too_short, input_value='test', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/string_too_short
E   telegram.token
E     Value error, Invalid Telegram token format. Expected format: 'bot_id:token' [type=value_error, input_value='test', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
E   providers.openai.base_url
E     Value error, Invalid base_url 'dummy'. Must start with http:// or https:// [type=value_error, input_value='dummy', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
E   memory.long_term.path
E     Value error, Database path cannot be empty [type=value_error, input_value='', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
_________________________ test_fts5_context_threading __________________________
tests/test_memory.py:282: in test_fts5_context_threading
    cfg = AppConfig.model_validate({
E   pydantic_core._pydantic_core.ValidationError: 4 validation errors for AppConfig
E   agent.system_prompt
E     String should have at least 10 characters [type=string_too_short, input_value='test', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/string_too_short
E   telegram.token
E     Value error, Invalid Telegram token format. Expected format: 'bot_id:token' [type=value_error, input_value='test', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
E   providers.openai.base_url
E     Value error, Invalid base_url 'dummy'. Must start with http:// or https:// [type=value_error, input_value='dummy', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
E   memory.long_term.path
E     Value error, Database path cannot be empty [type=value_error, input_value='', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
_______________________ test_memory_auto_prune_enforced ________________________
tests/test_memory.py:328: in test_memory_auto_prune_enforced
    cfg = AppConfig.model_validate({
E   pydantic_core._pydantic_core.ValidationError: 5 validation errors for AppConfig
E   agent.system_prompt
E     String should have at least 10 characters [type=string_too_short, input_value='sys', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/string_too_short
E   telegram.token
E     Value error, Invalid Telegram token format. Expected format: 'bot_id:token' [type=value_error, input_value='test', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
E   providers.openai.base_url
E     Value error, Invalid base_url 'dummy'. Must start with http:// or https:// [type=value_error, input_value='dummy', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
E   memory.short_term.auto_prune_limit
E     Input should be greater than or equal to 100 [type=greater_than_equal, input_value=3, input_type=int]
E       For further information visit https://errors.pydantic.dev/2.13/v/greater_than_equal
E   memory.long_term.path
E     Value error, Database path cannot be empty [type=value_error, input_value='', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
_______________________ test_memory_auto_prune_disabled ________________________
tests/test_memory.py:385: in test_memory_auto_prune_disabled
    cfg = AppConfig.model_validate({
E   pydantic_core._pydantic_core.ValidationError: 5 validation errors for AppConfig
E   agent.system_prompt
E     String should have at least 10 characters [type=string_too_short, input_value='sys', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/string_too_short
E   telegram.token
E     Value error, Invalid Telegram token format. Expected format: 'bot_id:token' [type=value_error, input_value='test', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
E   providers.openai.base_url
E     Value error, Invalid base_url 'dummy'. Must start with http:// or https:// [type=value_error, input_value='dummy', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
E   memory.short_term.auto_prune_limit
E     Input should be greater than or equal to 100 [type=greater_than_equal, input_value=3, input_type=int]
E       For further information visit https://errors.pydantic.dev/2.13/v/greater_than_equal
E   memory.long_term.path
E     Value error, Database path cannot be empty [type=value_error, input_value='', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
________________________ test_sqlite_store_vector_init _________________________
tests/test_memory.py:433: in test_sqlite_store_vector_init
    cfg = AppConfig.model_validate({
E   pydantic_core._pydantic_core.ValidationError: 3 validation errors for AppConfig
E   agent.system_prompt
E     String should have at least 10 characters [type=string_too_short, input_value='sys', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/string_too_short
E   telegram.token
E     Value error, Invalid Telegram token format. Expected format: 'bot_id:token' [type=value_error, input_value='test', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
E   providers.openai.base_url
E     Value error, Invalid base_url 'dummy'. Must start with http:// or https:// [type=value_error, input_value='dummy', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
_______________________ test_sqlite_store_get_embedding ________________________
tests/test_memory.py:467: in test_sqlite_store_get_embedding
    cfg = AppConfig.model_validate({
E   pydantic_core._pydantic_core.ValidationError: 3 validation errors for AppConfig
E   agent.system_prompt
E     String should have at least 10 characters [type=string_too_short, input_value='sys', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/string_too_short
E   telegram.token
E     Value error, Invalid Telegram token format. Expected format: 'bot_id:token' [type=value_error, input_value='test', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
E   providers.openai.base_url
E     Value error, Invalid base_url 'dummy'. Must start with http:// or https:// [type=value_error, input_value='dummy', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
_____________________ test_sqlite_store_add_message_vector _____________________
tests/test_memory.py:514: in test_sqlite_store_add_message_vector
    cfg = AppConfig.model_validate({
E   pydantic_core._pydantic_core.ValidationError: 3 validation errors for AppConfig
E   agent.system_prompt
E     String should have at least 10 characters [type=string_too_short, input_value='sys', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/string_too_short
E   telegram.token
E     Value error, Invalid Telegram token format. Expected format: 'bot_id:token' [type=value_error, input_value='test', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
E   providers.openai.base_url
E     Value error, Invalid base_url 'dummy'. Must start with http:// or https:// [type=value_error, input_value='dummy', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
___________ test_sqlite_store_add_message_vector_failure_falls_back ____________
tests/test_memory.py:564: in test_sqlite_store_add_message_vector_failure_falls_back
    cfg = AppConfig.model_validate(
E   pydantic_core._pydantic_core.ValidationError: 3 validation errors for AppConfig
E   agent.system_prompt
E     String should have at least 10 characters [type=string_too_short, input_value='sys', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/string_too_short
E   telegram.token
E     Value error, Invalid Telegram token format. Expected format: 'bot_id:token' [type=value_error, input_value='test', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
E   providers.openai.base_url
E     Value error, Invalid base_url 'dummy'. Must start with http:// or https:// [type=value_error, input_value='dummy', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
______________________ test_sqlite_store_search_semantic _______________________
tests/test_memory.py:611: in test_sqlite_store_search_semantic
    cfg = AppConfig.model_validate({
E   pydantic_core._pydantic_core.ValidationError: 3 validation errors for AppConfig
E   agent.system_prompt
E     String should have at least 10 characters [type=string_too_short, input_value='sys', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/string_too_short
E   telegram.token
E     Value error, Invalid Telegram token format. Expected format: 'bot_id:token' [type=value_error, input_value='test', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
E   providers.openai.base_url
E     Value error, Invalid base_url 'dummy'. Must start with http:// or https:// [type=value_error, input_value='dummy', input_type=str]
E       For further information visit https://errors.pydantic.dev/2.13/v/value_error
=============================== warnings summary ===============================
.venv/lib/python3.11/site-packages/fastapi/testclient.py:1
  /home/sandi/PocketFlow/idolhub/.venv/lib/python3.11/site-packages/fastapi/testclient.py:1: StarletteDeprecationWarning: Using `httpx` with `starlette.testclient` is deprecated; install `httpx2` instead.
    from starlette.testclient import TestClient as TestClient  # noqa

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ============================
FAILED tests/test_agent.py::test_agent_simple_response - pydantic_core._pydan...
FAILED tests/test_agent.py::test_agent_memory_tools_execution - pydantic_core...
FAILED tests/test_agent.py::test_agent_relevant_facts_injection - pydantic_co...
FAILED tests/test_agent.py::test_agent_fts_injection - pydantic_core._pydanti...
FAILED tests/test_agent.py::test_agent_facts_scoring - pydantic_core._pydanti...
FAILED tests/test_agent.py::test_agent_prompt_injection_blocking - pydantic_c...
FAILED tests/test_agent.py::test_agent_prompt_injection_after_before_message
FAILED tests/test_agent.py::test_agent_memory_gating_unapproved - pydantic_co...
FAILED tests/test_agent.py::test_agent_rrf_merger - pydantic_core._pydantic_c...
FAILED tests/test_agent.py::test_agent_tools_filtering - pydantic_core._pydan...
FAILED tests/test_agent.py::test_agent_tools_globally_disabled - pydantic_cor...
FAILED tests/test_agent.py::test_agent_filter_disabled - pydantic_core._pydan...
FAILED tests/test_agent.py::test_agent_gating_disabled - pydantic_core._pydan...
FAILED tests/test_agent.py::test_agent_fts_threading_integration - pydantic_c...
FAILED tests/test_agent.py::test_agent_semantic_rrf_integration - pydantic_co...
FAILED tests/test_config.py::test_load_config_resolves_nested_dict - ValueErr...
FAILED tests/test_config.py::test_long_term_config_embedding_model - ValueErr...
FAILED tests/test_llm.py::test_get_openai_client - pydantic_core._pydantic_co...
FAILED tests/test_llm.py::test_get_github_copilot_client - pydantic_core._pyd...
FAILED tests/test_llm.py::test_get_openai_codex_client - pydantic_core._pydan...
FAILED tests/test_llm.py::test_get_gemini_client - pydantic_core._pydantic_co...
FAILED tests/test_llm.py::test_invalid_provider_raises_error - pydantic_core....
FAILED tests/test_main.py::test_main_dispatch_bot_default - SystemExit: 1
FAILED tests/test_main.py::test_main_dispatch_api_cli - SystemExit: 1
FAILED tests/test_main.py::test_main_dispatch_mcp_cli - SystemExit: 1
FAILED tests/test_mcp.py::test_mcp_server_tool_registry - pydantic_core._pyda...
FAILED tests/test_memory.py::test_vector_init_missing_dependency_fails_before_opening_db
FAILED tests/test_memory.py::test_jaccard_deduplication - pydantic_core._pyda...
FAILED tests/test_memory.py::test_fts5_search - pydantic_core._pydantic_core....
FAILED tests/test_memory.py::test_fts5_context_threading - pydantic_core._pyd...
FAILED tests/test_memory.py::test_memory_auto_prune_enforced - pydantic_core....
FAILED tests/test_memory.py::test_memory_auto_prune_disabled - pydantic_core....
FAILED tests/test_memory.py::test_sqlite_store_vector_init - pydantic_core._p...
FAILED tests/test_memory.py::test_sqlite_store_get_embedding - pydantic_core....
FAILED tests/test_memory.py::test_sqlite_store_add_message_vector - pydantic_...
FAILED tests/test_memory.py::test_sqlite_store_add_message_vector_failure_falls_back
FAILED tests/test_memory.py::test_sqlite_store_search_semantic - pydantic_cor...
ERROR tests/test_api.py::test_health_endpoint - pydantic_core._pydantic_core....
ERROR tests/test_api.py::test_chat_endpoint - pydantic_core._pydantic_core.Va...
ERROR tests/test_api.py::test_get_config_masked - pydantic_core._pydantic_cor...
ERROR tests/test_api.py::test_update_config - pydantic_core._pydantic_core.Va...
ERROR tests/test_api.py::test_update_config_invalid_fails - pydantic_core._py...
ERROR tests/test_api.py::test_update_config_secrets_overwrite_protection - py...
ERROR tests/test_api.py::test_health_metrics - pydantic_core._pydantic_core.V...
ERROR tests/test_api_server.py::test_app_instance - pydantic_core._pydantic_c...
ERROR tests/test_api_server.py::test_app_lifespan - pydantic_core._pydantic_c...
ERROR tests/test_api_server.py::test_cors_allow_credentials_wildcard - pydant...
ERROR tests/test_api_server.py::test_cors_allow_credentials_specific - pydant...
ERROR tests/test_memory.py::test_memory_add_and_get - pydantic_core._pydantic...
ERROR tests/test_memory.py::test_memory_respects_max_messages - pydantic_core...
ERROR tests/test_memory.py::test_memory_filters_out_invalid_roles - pydantic_...
ERROR tests/test_memory.py::test_memory_facts_eav - pydantic_core._pydantic_c...
ERROR tests/test_memory.py::test_memory_preferences - pydantic_core._pydantic...
============= 37 failed, 60 passed, 1 warning, 16 errors in 5.74s ==============
```

## 2. Code Quality (ruff)

```
E501 Line too long (103 > 100)
  --> api/routes/config.py:52:101
   |
50 |             else:
51 |                 # Protect existing secrets from being overwritten by masks
52 |                 is_secret_key = any(sec in k.lower() for sec in ["token", "key", "secret", "password"])
   |                                                                                                     ^^^
53 |                 if is_secret_key and v == "********":
54 |                     continue
   |

E501 Line too long (103 > 100)
  --> api/routes/config.py:62:101
   |
60 |         deep_update(merged_data, payload)
61 |     except Exception as e:
62 |         raise HTTPException(status_code=400, detail=f"Failed to merge configuration updates: {str(e)}")
   |                                                                                                     ^^^
63 |
64 |     # Resolve environment variables and validate in memory using Pydantic AppConfig schema
   |

E501 Line too long (101 > 100)
   --> core/agent.py:137:101
    |
135 |         """Build the PocketFlow execution graph."""
136 |         self.answer_node = AnswerNode(self.cfg)
137 |         self.tool_node = ToolExecutionNode(self.cfg, self.tools_mapping, self.event_bus, self.memory)
    |                                                                                                     ^
138 |         
139 |         # Wire graph using PocketFlow custom transition operators
    |

E501 Line too long (127 > 100)
   --> core/agent.py:204:101
    |
202 |         if self.cfg.agent.memory_enabled:
203 |             fts_messages = await self.memory.search_history_fts(user_id, user_input, limit=3)
204 |             recent_contents = [m["content"] for m in messages[-4:]] if len(messages) >= 4 else [m["content"] for m in messages]
    |                                                                                                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^
205 |             unique_fts = [m for m in fts_messages if m.get("matched_content", m["content"]) not in recent_contents]
    |

E501 Line too long (115 > 100)
   --> core/agent.py:205:101
    |
203 |             fts_messages = await self.memory.search_history_fts(user_id, user_input, limit=3)
204 |             recent_contents = [m["content"] for m in messages[-4:]] if len(messages) >= 4 else [m["content"] for m in messages]
205 |             unique_fts = [m for m in fts_messages if m.get("matched_content", m["content"]) not in recent_contents]
    |                                                                                                     ^^^^^^^^^^^^^^^
206 |
207 |         # 2b. Retrieve semantic matching messages (only if memory enabled)
    |

E501 Line too long (127 > 100)
   --> core/agent.py:213:101
    |
211 |                 user_id, user_input, limit=3
212 |             )
213 |             recent_contents = [m["content"] for m in messages[-4:]] if len(messages) >= 4 else [m["content"] for m in messages]
    |                                                                                                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^
214 |             unique_semantic = [
215 |                 message
    |

E501 Line too long (142 > 100)
  --> core/bot.py:85:101
   |
83 | …
84 | …
85 | …parse_mode={self.cfg.telegram.parse_mode} ({e}). Mencoba mengirim sebagai plain text.")
   |                                               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
86 | …
87 | …
   |

E501 Line too long (102 > 100)
  --> core/bot.py:92:101
   |
90 |         except Exception as e:
91 |             logger.error(f"Error saat memproses pesan: {e}", exc_info=True)
92 |             await update.message.reply_text("Maaf, terjadi kesalahan saat memproses permintaan Anda.")
   |                                                                                                     ^^
93 |
94 |     def run(self):
   |

I001 [*] Import block is un-sorted or un-formatted
  --> core/config.py:13:1
   |
11 |   """
12 |
13 | / from core.config_schema import (
14 | |     AppConfig,
15 | |     AppSection,
16 | |     AgentSection,
17 | |     TelegramSection,
18 | |     LlmSection,
19 | |     ProviderCredentials,
20 | |     ShortTermMemory,
21 | |     LongTermMemory,
22 | |     MemorySection,
23 | |     SkillsSection,
24 | |     ToolsSection,
25 | |     PluginsSection,
26 | |     ApiSection,
27 | |     McpSection,
28 | |     LoggingSection,
29 | | )
30 | | from core.config_validator import (
31 | |     load_config,
32 | |     resolve_env,
33 | |     validate_capability_whitelists,
34 | |     validate_provider_credentials,
35 | |     get_available_providers,
36 | |     get_enabled_capabilities,
37 | | )
   | |_^
38 |
39 |   # Re-export for backward compatibility
   |
help: Organize imports

I001 [*] Import block is un-sorted or un-formatted
  --> core/config_reloader.py:12:1
   |
10 |   """
11 |
12 | / import asyncio
13 | | import threading
14 | | from typing import Callable, List, Optional, Tuple
15 | |
16 | | from core.config_schema import AppConfig
17 | | from core.config_validator import load_config
   | |_____________________________________________^
   |
help: Organize imports

F401 [*] `typing.Any` imported but unused
  --> core/config_schema.py:17:20
   |
16 | import os
17 | from typing import Any, Dict, List, Literal, Optional
   |                    ^^^
18 |
19 | from pydantic import BaseModel, Field, field_validator, model_validator
   |
help: Remove unused import: `typing.Any`

E501 Line too long (107 > 100)
  --> core/llm.py:44:101
   |
42 | async def call_llm(cfg: AppConfig, messages: list, tools: list = None):
43 |     """
44 |     Helper function untuk memanggil LLM secara asinkron dengan menginjeksi system prompt dari agent config.
   |                                                                                                     ^^^^^^^
45 |     """
46 |     client = get_llm_client(cfg)
   |

F401 [*] `core.config.load_config` imported but unused
 --> main.py:5:25
  |
4 | from core.bot import TelegramBot
5 | from core.config import load_config
  |                         ^^^^^^^^^^^
6 | from core.config_reloader import initialize_config
  |
help: Remove unused import: `core.config.load_config`

E501 Line too long (138 > 100)
  --> mcp_server/server.py:21:101
   |
19 | …
20 | …
21 | …tem (Ubuntu). Command berjalan secara aman di dalam Sandbox (Workspace directory)."""
   |                                                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
22 | …ceived: {command}")
23 | …
   |

E501 Line too long (136 > 100)
  --> memory/memory_gate.py:15:101
   |
13 | …
14 | …
15 | …r harus mencantumkan instruksi eksplisit: 'SIMPAN KE MEMORI' atau 'SAVE TO MEMORY'."
   |                                                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
16 | …
   |

E501 Line too long (101 > 100)
  --> memory/memory_gate.py:24:101
   |
22 |             return {
23 |                 "status": "REJECTED",
24 |                 "reason": f"Penulisan memori ditolak. Ditemukan indikasi perintah berbahaya: '{kw}'."
   |                                                                                                     ^
25 |             }
   |

E501 Line too long (124 > 100)
   --> memory/sqlite_store.py:108:101
    |
106 |         await self.db.execute('''
107 |             CREATE TRIGGER IF NOT EXISTS messages_ai AFTER INSERT ON messages BEGIN
108 |                 INSERT INTO messages_fts(rowid, user_id, role, content) VALUES (new.id, new.user_id, new.role, new.content);
    |                                                                                                     ^^^^^^^^^^^^^^^^^^^^^^^^
109 |             END;
110 |         ''')
    |

E501 Line too long (124 > 100)
   --> memory/sqlite_store.py:121:101
    |
119 |                 INSERT INTO messages_fts(messages_fts, rowid, user_id, role, content) 
120 |                 VALUES('delete', old.id, old.user_id, old.role, old.content);
121 |                 INSERT INTO messages_fts(rowid, user_id, role, content) VALUES (new.id, new.user_id, new.role, new.content);
    |                                                                                                     ^^^^^^^^^^^^^^^^^^^^^^^^
122 |             END;
123 |         ''')
    |

E501 Line too long (124 > 100)
   --> memory/sqlite_store.py:224:101
    |
222 |         return history
223 |
224 |     async def save_fakta(self, user_id: str, entity: str, nilai: str, confidence: float = 0.9, source: str = "auto") -> int:
    |                                                                                                     ^^^^^^^^^^^^^^^^^^^^^^^^
225 |         """Menyimpan atau memperbarui fakta pengguna (EAV facts)."""
226 |         try:
    |

E501 Line too long (102 > 100)
   --> memory/sqlite_store.py:243:101
    |
241 |             return cursor.rowcount
242 |
243 |     async def get_fakta(self, user_id: str, entity: str | None = None, limit: int = 10) -> List[Dict]:
    |                                                                                                     ^^
244 |         """Mengambil daftar fakta pengguna."""
245 |         if entity:
    |

E501 Line too long (108 > 100)
   --> memory/sqlite_store.py:313:101
    |
311 |                 matches.match_content
312 |             FROM messages m
313 |             JOIN matches ON m.user_id = ? AND m.id BETWEEN (matches.match_id - ?) AND (matches.match_id + ?)
    |                                                                                                     ^^^^^^^^
314 |             ORDER BY matches.match_id ASC, m.id ASC
315 |         '''
    |

E501 Line too long (153 > 100)
   --> memory/sqlite_store.py:317:101
    |
315 | …
316 | …
317 | …tch_expr, limit, str(user_id), self.fts_context_window, self.fts_context_window)) as cursor:
    |                                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
318 | …
    |

E501 Line too long (103 > 100)
  --> plugins/loader.py:10:101
   |
 8 | logger = logging.getLogger("idolhub.plugins")
 9 |
10 | EVENTS = ["before_message", "after_message", "before_reply", "after_reply", "on_error", "on_tool_call"]
   |                                                                                                     ^^^
11 |
12 | def register_plugin_to_bus(plugin_instance, event_bus: EventBus):
   |

E501 Line too long (119 > 100)
  --> plugins/loader.py:17:101
   |
15 |         if method and callable(method):
16 |             event_bus.subscribe(event_name, method)
17 |             logger.info(f"Subscribed method '{method.__name__}' of {type(plugin_instance).__name__} to '{event_name}'")
   |                                                                                                     ^^^^^^^^^^^^^^^^^^^
18 |
19 | def load_plugins(plugins_dir: str, event_bus: EventBus, enabled: list = None):
   |

E501 Line too long (112 > 100)
  --> skills/loader.py:81:101
   |
79 |             return res["content"]
80 |         else:
81 |             return "Error: Skill execution generated tool calls, which is not supported in simple skill runner."
   |                                                                                                     ^^^^^^^^^^^^
82 |     return run_skill
   |

I001 [*] Import block is un-sorted or un-formatted
 --> tests/conftest.py:5:1
  |
3 |   """
4 |
5 | / import pytest
6 | | from core.config_schema import AppConfig
  | |________________________________________^
  |
help: Organize imports

E501 Line too long (122 > 100)
  --> tests/test_agent.py:17:101
   |
15 |         "llm": {"provider": "openai", "model": "gpt-4"},
16 |         "providers": {"openai": {"base_url": "dummy", "api_key": "dummy"}},
17 |         "memory": {"short_term": {"backend": "sqlite", "path": ":memory:"}, "long_term": {"backend": "none", "path": ""}},
   |                                                                                                     ^^^^^^^^^^^^^^^^^^^^^^
18 |         "skills": {"dir": "./skills"},
19 |         "tools": {"dir": "./tools"},
   |

E501 Line too long (122 > 100)
  --> tests/test_agent.py:61:101
   |
59 |         "llm": {"provider": "openai", "model": "gpt-4"},
60 |         "providers": {"openai": {"base_url": "dummy", "api_key": "dummy"}},
61 |         "memory": {"short_term": {"backend": "sqlite", "path": ":memory:"}, "long_term": {"backend": "none", "path": ""}},
   |                                                                                                     ^^^^^^^^^^^^^^^^^^^^^^
62 |         "skills": {"dir": "./skills"},
63 |         "tools": {"dir": "./tools"},
   |

E501 Line too long (115 > 100)
   --> tests/test_agent.py:100:101
    |
 98 |                             "id": "call_1",
 99 |                             "type": "function",
100 |                             "function": {"name": "save_fact", "arguments": '{"entity": "hobi", "nilai": "coding"}'}
    |                                                                                                     ^^^^^^^^^^^^^^^
101 |                         },
102 |                         {
    |

E501 Line too long (117 > 100)
   --> tests/test_agent.py:105:101
    |
103 |                             "id": "call_2",
104 |                             "type": "function",
105 |                             "function": {"name": "set_preference", "arguments": '{"kunci": "bahasa", "nilai": "id"}'}
    |                                                                                                     ^^^^^^^^^^^^^^^^^
106 |                         }
107 |                     ]
    |

E501 Line too long (137 > 100)
   --> tests/test_agent.py:118:101
    |
116 | …
117 | …
118 | …ser_input="SAVE TO MEMORY: Remember my hobby is coding and language is Indonesian.")
    |                                                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
119 | …
120 | …
    |

E501 Line too long (122 > 100)
   --> tests/test_agent.py:143:101
    |
141 |         "llm": {"provider": "openai", "model": "gpt-4"},
142 |         "providers": {"openai": {"base_url": "dummy", "api_key": "dummy"}},
143 |         "memory": {"short_term": {"backend": "sqlite", "path": ":memory:"}, "long_term": {"backend": "none", "path": ""}},
    |                                                                                                     ^^^^^^^^^^^^^^^^^^^^^^
144 |         "skills": {"dir": "./skills"},
145 |         "tools": {"dir": "./tools"},
    |

E501 Line too long (104 > 100)
   --> tests/test_agent.py:180:101
    |
178 |     assert "hobi" not in captured_messages[0]["content"]
179 |
180 |     # Act 2: query matching multiple entities ('riding' -> matches 'hobi', 'pizza' -> matches 'makanan')
    |                                                                                                     ^^^^
181 |     captured_messages.clear()
182 |     await agent.run(user_id=user_id, user_input="Apakah hobi riding makanan pizza?")
    |

E501 Line too long (127 > 100)
   --> tests/test_agent.py:197:101
    |
195 |     # Assert 3: no system message injected at index 0 starting with "Relevant context (RRF ranked):"
196 |     assert len(captured_messages) > 0
197 |     assert not any(msg["role"] == "system" and "Relevant context (RRF ranked):" in msg["content"] for msg in captured_messages)
    |                                                                                                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^
198 |
199 |     await agent.close()
    |

E501 Line too long (141 > 100)
   --> tests/test_agent.py:210:101
    |
208 | …,
209 | …api_key": "dummy"}},
210 | …"path": ":memory:", "max_messages": 2}, "long_term": {"backend": "none", "path": ""}},
    |                                               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
211 | …
212 | …
    |

E501 Line too long (152 > 100)
   --> tests/test_agent.py:241:101
    |
239 | …
240 | …
241 | … (RRF ranked):" in msg["content"] and "Koko" in msg["content"] for msg in captured_messages)
    |                                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
242 | …
243 | …
    |

E501 Line too long (122 > 100)
   --> tests/test_agent.py:254:101
    |
252 |         "llm": {"provider": "openai", "model": "gpt-4"},
253 |         "providers": {"openai": {"base_url": "dummy", "api_key": "dummy"}},
254 |         "memory": {"short_term": {"backend": "sqlite", "path": ":memory:"}, "long_term": {"backend": "none", "path": ""}},
    |                                                                                                     ^^^^^^^^^^^^^^^^^^^^^^
255 |         "skills": {"dir": "./skills"},
256 |         "tools": {"dir": "./tools"},
    |

E501 Line too long (144 > 100)
   --> tests/test_agent.py:287:101
    |
285 | …
286 | …
287 | …es if msg["role"] == "system" and "Relevant context (RRF ranked):" in msg["content"]][0]
    |                                              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
288 | …
289 | …word intersection and newest recency, or motor
    |

E501 Line too long (102 > 100)
   --> tests/test_agent.py:289:101
    |
287 |     sys_msg = [msg["content"] for msg in captured_messages if msg["role"] == "system" and "Relevant context (RRF ranked):" in msg["co…
288 |     
289 |     # Motor sport should be ranked high due to exact keyword intersection and newest recency, or motor
    |                                                                                                     ^^
290 |     assert "Fakta: motor sport -> kawasaki" in sys_msg
291 |     assert "Fakta: motor -> mioblack" in sys_msg
    |

E501 Line too long (122 > 100)
   --> tests/test_agent.py:304:101
    |
302 |         "llm": {"provider": "openai", "model": "gpt-4"},
303 |         "providers": {"openai": {"base_url": "dummy", "api_key": "dummy"}},
304 |         "memory": {"short_term": {"backend": "sqlite", "path": ":memory:"}, "long_term": {"backend": "none", "path": ""}},
    |                                                                                                     ^^^^^^^^^^^^^^^^^^^^^^
305 |         "skills": {"dir": "./skills"},
306 |         "tools": {"dir": "./tools"},
    |

E501 Line too long (122 > 100)
   --> tests/test_agent.py:327:101
    |
325 |         "llm": {"provider": "openai", "model": "gpt-4"},
326 |         "providers": {"openai": {"base_url": "dummy", "api_key": "dummy"}},
327 |         "memory": {"short_term": {"backend": "sqlite", "path": ":memory:"}, "long_term": {"backend": "none", "path": ""}},
    |                                                                                                     ^^^^^^^^^^^^^^^^^^^^^^
328 |         "skills": {"dir": "./skills"},
329 |         "tools": {"dir": "./tools"},
    |

E501 Line too long (122 > 100)
   --> tests/test_agent.py:380:101
    |
378 |         "llm": {"provider": "openai", "model": "gpt-4"},
379 |         "providers": {"openai": {"base_url": "dummy", "api_key": "dummy"}},
380 |         "memory": {"short_term": {"backend": "sqlite", "path": ":memory:"}, "long_term": {"backend": "none", "path": ""}},
    |                                                                                                     ^^^^^^^^^^^^^^^^^^^^^^
381 |         "skills": {"dir": "./skills"},
382 |         "tools": {"dir": "./tools"},
    |

E501 Line too long (131 > 100)
   --> tests/test_agent.py:394:101
    |
392 |     from tools.registry import save_fact
393 |     # Test save_fact directly with user_input lacking approval keyword
394 |     res = await save_fact(entity="kunci", nilai="nilai", user_id="user_test", memory=agent.memory, user_input="Tolong simpan ini.")
    |                                                                                                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
395 |     assert "REJECTED" in res
396 |     assert "SIMPAN KE MEMORI" in res
    |

E501 Line too long (152 > 100)
   --> tests/test_agent.py:399:101
    |
398 | …
399 | …user_id="user_test", memory=agent.memory, user_input="SIMPAN KE MEMORI: kunci adalah nilai")
    |                                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
400 | …
    |

E501 Line too long (163 > 100)
   --> tests/test_agent.py:403:101
    |
402 | …
403 | …, user_id="user_test", memory=agent.memory, user_input="SIMPAN KE MEMORI: kunci adalah rm -rf /")
    |                                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
404 | …
405 | …
    |

E501 Line too long (141 > 100)
   --> tests/test_agent.py:418:101
    |
416 | …,
417 | …api_key": "dummy"}},
418 | …"path": ":memory:", "max_messages": 2}, "long_term": {"backend": "none", "path": ""}},
    |                                               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
419 | …
420 | …
    |

E501 Line too long (122 > 100)
   --> tests/test_agent.py:466:101
    |
464 |         "llm": {"provider": "openai", "model": "gpt-4"},
465 |         "providers": {"openai": {"base_url": "dummy", "api_key": "dummy"}},
466 |         "memory": {"short_term": {"backend": "sqlite", "path": ":memory:"}, "long_term": {"backend": "none", "path": ""}},
    |                                                                                                     ^^^^^^^^^^^^^^^^^^^^^^
467 |         "skills": {"dir": "./skills"},
468 |         "tools": {"dir": "./tools", "enabled": ["search_web", "save_fact"]},
    |

E501 Line too long (122 > 100)
   --> tests/test_agent.py:495:101
    |
493 |         "llm": {"provider": "openai", "model": "gpt-4"},
494 |         "providers": {"openai": {"base_url": "dummy", "api_key": "dummy"}},
495 |         "memory": {"short_term": {"backend": "sqlite", "path": ":memory:"}, "long_term": {"backend": "none", "path": ""}},
    |                                                                                                     ^^^^^^^^^^^^^^^^^^^^^^
496 |         "skills": {"dir": "./skills"},
497 |         "tools": {"dir": "./tools"},
    |

E501 Line too long (122 > 100)
   --> tests/test_agent.py:528:101
    |
526 |         "llm": {"provider": "openai", "model": "gpt-4"},
527 |         "providers": {"openai": {"base_url": "dummy", "api_key": "dummy"}},
528 |         "memory": {"short_term": {"backend": "sqlite", "path": ":memory:"}, "long_term": {"backend": "none", "path": ""}},
    |                                                                                                     ^^^^^^^^^^^^^^^^^^^^^^
529 |         "skills": {"dir": "./skills"},
530 |         "tools": {"dir": "./tools"},
    |

E501 Line too long (122 > 100)
   --> tests/test_agent.py:558:101
    |
556 |         "llm": {"provider": "openai", "model": "gpt-4"},
557 |         "providers": {"openai": {"base_url": "dummy", "api_key": "dummy"}},
558 |         "memory": {"short_term": {"backend": "sqlite", "path": ":memory:"}, "long_term": {"backend": "none", "path": ""}},
    |                                                                                                     ^^^^^^^^^^^^^^^^^^^^^^
559 |         "skills": {"dir": "./skills"},
560 |         "tools": {"dir": "./tools"},
    |

E501 Line too long (160 > 100)
   --> tests/test_agent.py:585:101
    |
583 | …
584 | …
585 | …ion", "function": {"name": "save_fact", "arguments": '{"entity": "hobi", "nilai": "hacking"}'}}]
    |                                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
586 | …
587 | …
    |

E501 Line too long (136 > 100)
   --> tests/test_agent.py:647:101
    |
645 | …"Mau makan nasi goreng saja")
646 | …nt", "Nasi goreng adalah pilihan yang bagus.")
647 | …"Bagaimana cuaca hari ini?") # Distractor to move target message out of max_messages
    |                                                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
648 | …
649 | …
    |

E501 Line too long (156 > 100)
   --> tests/test_agent.py:655:101
    |
653 | …
654 | …
655 | …ages if msg["role"] == "system" and "Relevant context (RRF ranked):" in msg["content"]), None)
    |                                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
656 | …
657 | …
    |

E501 Line too long (122 > 100)
  --> tests/test_api.py:18:101
   |
16 |         "llm": {"provider": "openai", "model": "gpt-4"},
17 |         "providers": {"openai": {"base_url": "dummy", "api_key": "dummy"}},
18 |         "memory": {"short_term": {"backend": "sqlite", "path": ":memory:"}, "long_term": {"backend": "none", "path": ""}},
   |                                                                                                     ^^^^^^^^^^^^^^^^^^^^^^
19 |         "skills": {"dir": "./skills"},
20 |         "tools": {"dir": "./tools"},
   |

E501 Line too long (122 > 100)
   --> tests/test_api.py:103:101
    |
101 |         "llm": {"provider": "openai", "model": "gpt-4"},
102 |         "providers": {"openai": {"base_url": "dummy", "api_key": "dummy"}},
103 |         "memory": {"short_term": {"backend": "sqlite", "path": ":memory:"}, "long_term": {"backend": "none", "path": ""}},
    |                                                                                                     ^^^^^^^^^^^^^^^^^^^^^^
104 |         "skills": {"dir": "./skills"},
105 |         "tools": {"dir": "./tools"},
    |

E501 Line too long (107 > 100)
   --> tests/test_api.py:121:101
    |
119 |     monkeypatch.setattr("builtins.open", mock_open)
120 |     
121 |     # Patch load_config inside api.routes.config to load from temp_config using the unpatched core function
    |                                                                                                     ^^^^^^^
122 |     from core.config import AppConfig
    |

E501 Line too long (122 > 100)
   --> tests/test_api.py:151:101
    |
149 |         "llm": {"provider": "openai", "model": "gpt-4"},
150 |         "providers": {"openai": {"base_url": "dummy", "api_key": "dummy"}},
151 |         "memory": {"short_term": {"backend": "sqlite", "path": ":memory:"}, "long_term": {"backend": "none", "path": ""}},
    |                                                                                                     ^^^^^^^^^^^^^^^^^^^^^^
152 |         "skills": {"dir": "./skills"},
153 |         "tools": {"dir": "./tools"},
    |

E501 Line too long (122 > 100)
   --> tests/test_api.py:190:101
    |
188 |         "llm": {"provider": "openai", "model": "gpt-4"},
189 |         "providers": {"openai": {"base_url": "dummy", "api_key": "dummy"}},
190 |         "memory": {"short_term": {"backend": "sqlite", "path": ":memory:"}, "long_term": {"backend": "none", "path": ""}},
    |                                                                                                     ^^^^^^^^^^^^^^^^^^^^^^
191 |         "skills": {"dir": "./skills"},
192 |         "tools": {"dir": "./tools"},
    |

E501 Line too long (122 > 100)
  --> tests/test_api_server.py:16:101
   |
14 |         "llm": {"provider": "openai", "model": "gpt-4"},
15 |         "providers": {"openai": {"base_url": "dummy", "api_key": "dummy"}},
16 |         "memory": {"short_term": {"backend": "sqlite", "path": ":memory:"}, "long_term": {"backend": "none", "path": ""}},
   |                                                                                                     ^^^^^^^^^^^^^^^^^^^^^^
17 |         "skills": {"dir": "./skills"},
18 |         "tools": {"dir": "./tools"},
   |

E501 Line too long (107 > 100)
  --> tests/test_config.py:32:101
   |
30 |       "app": {"name": "test", "mode": "bot", "debug": false, "timezone": "UTC"},
31 |       "telegram": {"token": "$MY_KEY", "allowed_users": [], "parse_mode": "Markdown"},
32 |       "llm": {"provider": "openai", "model": "test", "temperature": 0.0, "max_tokens": 100, "timeout": 10},
   |                                                                                                     ^^^^^^^
33 |       "providers": {},
34 |       "memory": {
   |

E501 Line too long (109 > 100)
  --> tests/test_config.py:44:101
   |
42 |       "mcp": {"enabled": false, "port": 8001},
43 |       "logging": {"level": "INFO", "format": "text"},
44 |       "agent": {"system_prompt": "test", "max_iterations": 1, "tools_enabled": true, "memory_enabled": false}
   |                                                                                                     ^^^^^^^^^
45 |     }
46 |     ''')
   |

E501 Line too long (108 > 100)
  --> tests/test_config.py:64:101
   |
62 |         "memory": {
63 |             "short_term": {"backend": "sqlite", "path": "x"},
64 |             "long_term": {"backend": "sqlite_vec", "path": "y", "embedding_model": "text-embedding-3-small"}
   |                                                                                                     ^^^^^^^^
65 |         },
66 |         "skills": {"dir": "./skills"},
   |

I001 [*] Import block is un-sorted or un-formatted
  --> tests/test_config_reloader.py:5:1
   |
 3 |   """
 4 |
 5 | / import json
 6 | | import tempfile
 7 | | from pathlib import Path
 8 | |
 9 | | import pytest
10 | |
11 | | from core.config_reloader import (
12 | |     initialize_config,
13 | |     get_current_config,
14 | |     reload_config_sync,
15 | |     register_change_handler,
16 | |     unregister_change_handler,
17 | |     clear_change_handlers,
18 | | )
19 | | from core.config_schema import AppConfig
   | |________________________________________^
   |
help: Organize imports

F401 [*] `tempfile` imported but unused
 --> tests/test_config_reloader.py:6:8
  |
5 | import json
6 | import tempfile
  |        ^^^^^^^^
7 | from pathlib import Path
  |
help: Remove unused import: `tempfile`

F401 [*] `pathlib.Path` imported but unused
 --> tests/test_config_reloader.py:7:21
  |
5 | import json
6 | import tempfile
7 | from pathlib import Path
  |                     ^^^^
8 |
9 | import pytest
  |
help: Remove unused import: `pathlib.Path`

E501 Line too long (111 > 100)
  --> tests/test_config_reloader.py:36:101
   |
34 |         },
35 |         "telegram": {"token": "123:abc", "allowed_users": [], "parse_mode": "Markdown"},
36 |         "llm": {"provider": "openai", "model": "gpt-4", "temperature": 0.7, "max_tokens": 4096, "timeout": 30},
   |                                                                                                     ^^^^^^^^^^^
37 |         "providers": {
38 |             "openai": {"base_url": "https://api.openai.com/v1", "api_key": "sk-test"}
   |

E501 Line too long (175 > 100)
  --> tests/test_config_reloader.py:41:101
   |
39 | …
40 | …
41 | …db", "max_messages": 50, "fts_context_window": 2, "auto_prune_enabled": True, "auto_prune_limit": 1000},
   |                               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
42 | …", "embedding_model": "text-embedding-3-small"}
43 | …
   |

E501 Line too long (118 > 100)
  --> tests/test_config_reloader.py:42:101
   |
40 | …     "memory": {
41 | …         "short_term": {"backend": "sqlite", "path": "./data/memory.db", "max_messages": 50, "fts_context_window": 2, "auto_prune_ena…
42 | …         "long_term": {"backend": "none", "path": "./data/vectors.db", "embedding_model": "text-embedding-3-small"}
   |                                                                                                   ^^^^^^^^^^^^^^^^^^
43 | …     },
44 | …     "skills": {"dir": "./skills", "enabled": []},
   |

I001 [*] Import block is un-sorted or un-formatted
  --> tests/test_config_schema.py:5:1
   |
 3 |   """
 4 |
 5 | / import pytest
 6 | | from pydantic import ValidationError
 7 | |
 8 | | from core.config_schema import (
 9 | |     AppSection,
10 | |     AgentSection,
11 | |     TelegramSection,
12 | |     LlmSection,
13 | |     ProviderCredentials,
14 | |     ShortTermMemory,
15 | |     LongTermMemory,
16 | |     MemorySection,
17 | |     SkillsSection,
18 | |     ToolsSection,
19 | |     PluginsSection,
20 | |     ApiSection,
21 | |     McpSection,
22 | |     LoggingSection,
23 | |     AppConfig,
24 | | )
   | |_^
   |
help: Organize imports

I001 [*] Import block is un-sorted or un-formatted
  --> tests/test_config_validator.py:5:1
   |
 3 |   """
 4 |
 5 | / import json
 6 | | import os
 7 | | import tempfile
 8 | | from pathlib import Path
 9 | |
10 | | import pytest
11 | |
12 | | from core.config_validator import (
13 | |     load_config,
14 | |     resolve_env,
15 | |     validate_capability_whitelists,
16 | |     get_available_providers,
17 | |     get_enabled_capabilities,
18 | | )
19 | | from core.config_schema import AppConfig
   | |________________________________________^
   |
help: Organize imports

F401 [*] `tempfile` imported but unused
 --> tests/test_config_validator.py:7:8
  |
5 | import json
6 | import os
7 | import tempfile
  |        ^^^^^^^^
8 | from pathlib import Path
  |
help: Remove unused import: `tempfile`

F401 [*] `pathlib.Path` imported but unused
  --> tests/test_config_validator.py:8:21
   |
 6 | import os
 7 | import tempfile
 8 | from pathlib import Path
   |                     ^^^^
 9 |
10 | import pytest
   |
help: Remove unused import: `pathlib.Path`

E501 Line too long (115 > 100)
  --> tests/test_config_validator.py:66:101
   |
64 |             },
65 |             "telegram": {"token": "123:abc", "allowed_users": [], "parse_mode": "Markdown"},
66 |             "llm": {"provider": "openai", "model": "gpt-4", "temperature": 0.7, "max_tokens": 4096, "timeout": 30},
   |                                                                                                     ^^^^^^^^^^^^^^^
67 |             "providers": {
68 |                 "openai": {"base_url": "https://api.openai.com/v1", "api_key": "sk-test"}
   |

E501 Line too long (179 > 100)
  --> tests/test_config_validator.py:71:101
   |
69 | …
70 | …
71 | …y.db", "max_messages": 50, "fts_context_window": 2, "auto_prune_enabled": True, "auto_prune_limit": 1000},
   |                             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
72 | …db", "embedding_model": "text-embedding-3-small"}
73 | …
   |

E501 Line too long (122 > 100)
  --> tests/test_config_validator.py:72:101
   |
70 | …     "memory": {
71 | …         "short_term": {"backend": "sqlite", "path": "./data/memory.db", "max_messages": 50, "fts_context_window": 2, "auto_prune_ena…
72 | …         "long_term": {"backend": "none", "path": "./data/vectors.db", "embedding_model": "text-embedding-3-small"}
   |                                                                                               ^^^^^^^^^^^^^^^^^^^^^^
73 | …     },
74 | …     "skills": {"dir": "./skills", "enabled": []},
   |

E501 Line too long (115 > 100)
   --> tests/test_config_validator.py:105:101
    |
103 |             },
104 |             "telegram": {"token": "123:abc", "allowed_users": [], "parse_mode": "Markdown"},
105 |             "llm": {"provider": "openai", "model": "gpt-4", "temperature": 0.7, "max_tokens": 4096, "timeout": 30},
    |                                                                                                     ^^^^^^^^^^^^^^^
106 |             "providers": {
107 |                 "openai": {"base_url": "https://api.openai.com/v1", "api_key": "$TEST_API_KEY"}
    |

E501 Line too long (179 > 100)
   --> tests/test_config_validator.py:110:101
    |
108 | …
109 | …
110 | ….db", "max_messages": 50, "fts_context_window": 2, "auto_prune_enabled": True, "auto_prune_limit": 1000},
    |                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
111 | …b", "embedding_model": "text-embedding-3-small"}
112 | …
    |

E501 Line too long (122 > 100)
   --> tests/test_config_validator.py:111:101
    |
109 | …     "memory": {
110 | …         "short_term": {"backend": "sqlite", "path": "./data/memory.db", "max_messages": 50, "fts_context_window": 2, "auto_prune_en…
111 | …         "long_term": {"backend": "none", "path": "./data/vectors.db", "embedding_model": "text-embedding-3-small"}
    |                                                                                               ^^^^^^^^^^^^^^^^^^^^^^
112 | …     },
113 | …     "skills": {"dir": "./skills", "enabled": []},
    |

E501 Line too long (115 > 100)
   --> tests/test_config_validator.py:159:101
    |
157 |             },
158 |             "telegram": {"token": "123:abc", "allowed_users": [], "parse_mode": "Markdown"},
159 |             "llm": {"provider": "openai", "model": "gpt-4", "temperature": 0.7, "max_tokens": 4096, "timeout": 30},
    |                                                                                                     ^^^^^^^^^^^^^^^
160 |             "providers": {
161 |                 "openai": {"base_url": "https://api.openai.com/v1", "api_key": "$MISSING_VAR"}
    |

E501 Line too long (179 > 100)
   --> tests/test_config_validator.py:164:101
    |
162 | …
163 | …
164 | ….db", "max_messages": 50, "fts_context_window": 2, "auto_prune_enabled": True, "auto_prune_limit": 1000},
    |                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
165 | …b", "embedding_model": "text-embedding-3-small"}
166 | …
    |

E501 Line too long (122 > 100)
   --> tests/test_config_validator.py:165:101
    |
163 | …     "memory": {
164 | …         "short_term": {"backend": "sqlite", "path": "./data/memory.db", "max_messages": 50, "fts_context_window": 2, "auto_prune_en…
165 | …         "long_term": {"backend": "none", "path": "./data/vectors.db", "embedding_model": "text-embedding-3-small"}
    |                                                                                               ^^^^^^^^^^^^^^^^^^^^^^
166 | …     },
167 | …     "skills": {"dir": "./skills", "enabled": []},
    |

E501 Line too long (115 > 100)
   --> tests/test_config_validator.py:203:101
    |
201 |             },
202 |             "telegram": {"token": "123:abc", "allowed_users": [], "parse_mode": "Markdown"},
203 |             "llm": {"provider": "openai", "model": "gpt-4", "temperature": 0.7, "max_tokens": 4096, "timeout": 30},
    |                                                                                                     ^^^^^^^^^^^^^^^
204 |             "providers": {
205 |                 "openai": {"base_url": "https://api.openai.com/v1", "api_key": "sk-test"}
    |

E501 Line too long (179 > 100)
   --> tests/test_config_validator.py:208:101
    |
206 | …
207 | …
208 | ….db", "max_messages": 50, "fts_context_window": 2, "auto_prune_enabled": True, "auto_prune_limit": 1000},
    |                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
209 | …b", "embedding_model": "text-embedding-3-small"}
210 | …
    |

E501 Line too long (122 > 100)
   --> tests/test_config_validator.py:209:101
    |
207 | …     "memory": {
208 | …         "short_term": {"backend": "sqlite", "path": "./data/memory.db", "max_messages": 50, "fts_context_window": 2, "auto_prune_en…
209 | …         "long_term": {"backend": "none", "path": "./data/vectors.db", "embedding_model": "text-embedding-3-small"}
    |                                                                                               ^^^^^^^^^^^^^^^^^^^^^^
210 | …     },
211 | …     "skills": {"dir": str(skills_dir), "enabled": ["test"]},
    |

E501 Line too long (115 > 100)
   --> tests/test_config_validator.py:240:101
    |
238 |             },
239 |             "telegram": {"token": "123:abc", "allowed_users": [], "parse_mode": "Markdown"},
240 |             "llm": {"provider": "openai", "model": "gpt-4", "temperature": 0.7, "max_tokens": 4096, "timeout": 30},
    |                                                                                                     ^^^^^^^^^^^^^^^
241 |             "providers": {
242 |                 "openai": {"base_url": "https://api.openai.com/v1", "api_key": "sk-test"}
    |

E501 Line too long (179 > 100)
   --> tests/test_config_validator.py:245:101
    |
243 | …
244 | …
245 | ….db", "max_messages": 50, "fts_context_window": 2, "auto_prune_enabled": True, "auto_prune_limit": 1000},
    |                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
246 | …b", "embedding_model": "text-embedding-3-small"}
247 | …
    |

E501 Line too long (122 > 100)
   --> tests/test_config_validator.py:246:101
    |
244 | …     "memory": {
245 | …         "short_term": {"backend": "sqlite", "path": "./data/memory.db", "max_messages": 50, "fts_context_window": 2, "auto_prune_en…
246 | …         "long_term": {"backend": "none", "path": "./data/vectors.db", "embedding_model": "text-embedding-3-small"}
    |                                                                                               ^^^^^^^^^^^^^^^^^^^^^^
247 | …     },
248 | …     "skills": {"dir": "/nonexistent/skills", "enabled": ["test"]},
    |

E501 Line too long (115 > 100)
   --> tests/test_config_validator.py:280:101
    |
278 |             },
279 |             "telegram": {"token": "123:abc", "allowed_users": [], "parse_mode": "Markdown"},
280 |             "llm": {"provider": "openai", "model": "gpt-4", "temperature": 0.7, "max_tokens": 4096, "timeout": 30},
    |                                                                                                     ^^^^^^^^^^^^^^^
281 |             "providers": {
282 |                 "openai": {"base_url": "https://api.openai.com/v1", "api_key": "sk-test"},
    |

E501 Line too long (179 > 100)
   --> tests/test_config_validator.py:286:101
    |
284 | …
285 | …
286 | ….db", "max_messages": 50, "fts_context_window": 2, "auto_prune_enabled": True, "auto_prune_limit": 1000},
    |                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
287 | …b", "embedding_model": "text-embedding-3-small"}
288 | …
    |

E501 Line too long (122 > 100)
   --> tests/test_config_validator.py:287:101
    |
285 | …     "memory": {
286 | …         "short_term": {"backend": "sqlite", "path": "./data/memory.db", "max_messages": 50, "fts_context_window": 2, "auto_prune_en…
287 | …         "long_term": {"backend": "none", "path": "./data/vectors.db", "embedding_model": "text-embedding-3-small"}
    |                                                                                               ^^^^^^^^^^^^^^^^^^^^^^
288 | …     },
289 | …     "skills": {"dir": "./skills", "enabled": []},
    |

E501 Line too long (115 > 100)
   --> tests/test_config_validator.py:318:101
    |
316 |             },
317 |             "telegram": {"token": "123:abc", "allowed_users": [], "parse_mode": "Markdown"},
318 |             "llm": {"provider": "openai", "model": "gpt-4", "temperature": 0.7, "max_tokens": 4096, "timeout": 30},
    |                                                                                                     ^^^^^^^^^^^^^^^
319 |             "providers": {
320 |                 "openai": {"base_url": "https://api.openai.com/v1", "api_key": "sk-test"}
    |

E501 Line too long (179 > 100)
   --> tests/test_config_validator.py:323:101
    |
321 | …
322 | …
323 | ….db", "max_messages": 50, "fts_context_window": 2, "auto_prune_enabled": True, "auto_prune_limit": 1000},
    |                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
324 | …b", "embedding_model": "text-embedding-3-small"}
325 | …
    |

E501 Line too long (122 > 100)
   --> tests/test_config_validator.py:324:101
    |
322 | …     "memory": {
323 | …         "short_term": {"backend": "sqlite", "path": "./data/memory.db", "max_messages": 50, "fts_context_window": 2, "auto_prune_en…
324 | …         "long_term": {"backend": "none", "path": "./data/vectors.db", "embedding_model": "text-embedding-3-small"}
    |                                                                                               ^^^^^^^^^^^^^^^^^^^^^^
325 | …     },
326 | …     "skills": {"dir": "./skills", "enabled": ["skill1", "skill2"]},
    |

E501 Line too long (110 > 100)
  --> tests/test_llm.py:13:101
   |
11 |         "telegram": {"token": "test"},
12 |         "agent": {"system_prompt": "sys"},
13 |         "llm": {"provider": "openai", "model": "gpt-4", "temperature": 0.0, "max_tokens": 100, "timeout": 30},
   |                                                                                                     ^^^^^^^^^^
14 |         "providers": {
15 |             "openai": {"base_url": "https://api.openai.com/v1", "api_key": "sk-123"}
   |

E501 Line too long (122 > 100)
  --> tests/test_llm.py:17:101
   |
15 |             "openai": {"base_url": "https://api.openai.com/v1", "api_key": "sk-123"}
16 |         },
17 |         "memory": {"short_term": {"backend": "sqlite", "path": ":memory:"}, "long_term": {"backend": "none", "path": ""}},
   |                                                                                                     ^^^^^^^^^^^^^^^^^^^^^^
18 |         "skills": {"dir": "./skills"},
19 |         "tools": {"dir": "./tools"},
   |

E501 Line too long (122 > 100)
  --> tests/test_llm.py:42:101
   |
40 |             "github_copilot": {"base_url": "https://api.githubcopilot.com", "cli_token": "gho_123"}
41 |         },
42 |         "memory": {"short_term": {"backend": "sqlite", "path": ":memory:"}, "long_term": {"backend": "none", "path": ""}},
   |                                                                                                     ^^^^^^^^^^^^^^^^^^^^^^
43 |         "skills": {"dir": "./skills"},
44 |         "tools": {"dir": "./tools"},
   |

E501 Line too long (122 > 100)
  --> tests/test_llm.py:64:101
   |
62 |             "openai_codex": {"base_url": "https://api.openai.com/v1", "oauth_token": "oauth_123"}
63 |         },
64 |         "memory": {"short_term": {"backend": "sqlite", "path": ":memory:"}, "long_term": {"backend": "none", "path": ""}},
   |                                                                                                     ^^^^^^^^^^^^^^^^^^^^^^
65 |         "skills": {"dir": "./skills"},
66 |         "tools": {"dir": "./tools"},
   |

E501 Line too long (119 > 100)
  --> tests/test_llm.py:84:101
   |
82 |         "llm": {"provider": "gemini", "model": "gemma-4-31b-it"},
83 |         "providers": {
84 |             "gemini": {"base_url": "https://generativelanguage.googleapis.com/v1beta/openai/", "api_key": "AIzaSy_123"}
   |                                                                                                     ^^^^^^^^^^^^^^^^^^^
85 |         },
86 |         "memory": {"short_term": {"backend": "sqlite", "path": ":memory:"}, "long_term": {"backend": "none", "path": ""}},
   |

E501 Line too long (122 > 100)
  --> tests/test_llm.py:86:101
   |
84 |             "gemini": {"base_url": "https://generativelanguage.googleapis.com/v1beta/openai/", "api_key": "AIzaSy_123"}
85 |         },
86 |         "memory": {"short_term": {"backend": "sqlite", "path": ":memory:"}, "long_term": {"backend": "none", "path": ""}},
   |                                                                                                     ^^^^^^^^^^^^^^^^^^^^^^
87 |         "skills": {"dir": "./skills"},
88 |         "tools": {"dir": "./tools"},
   |

E501 Line too long (122 > 100)
   --> tests/test_llm.py:106:101
    |
104 |         "llm": {"provider": "unknown", "model": "gpt-4"},
105 |         "providers": {},
106 |         "memory": {"short_term": {"backend": "sqlite", "path": ":memory:"}, "long_term": {"backend": "none", "path": ""}},
    |                                                                                                     ^^^^^^^^^^^^^^^^^^^^^^
107 |         "skills": {"dir": "./skills"},
108 |         "tools": {"dir": "./tools"},
    |

E501 Line too long (105 > 100)
  --> tests/test_main.py:45:101
   |
43 |         main()
44 |         
45 |     mock_uvicorn_run.assert_called_once_with("api.server:app", host="127.0.0.1", port=8000, reload=False)
   |                                                                                                     ^^^^^
46 |
47 | @patch("main.load_config")
   |

E501 Line too long (122 > 100)
  --> tests/test_mcp.py:18:101
   |
16 |         "llm": {"provider": "openai", "model": "gpt-4"},
17 |         "providers": {"openai": {"base_url": "dummy", "api_key": "dummy"}},
18 |         "memory": {"short_term": {"backend": "sqlite", "path": ":memory:"}, "long_term": {"backend": "none", "path": ""}},
   |                                                                                                     ^^^^^^^^^^^^^^^^^^^^^^
19 |         "skills": {"dir": "./skills"},
20 |         "tools": {"dir": "./tools"},
   |

E501 Line too long (110 > 100)
   --> tests/test_memory.py:179:101
    |
178 |     # Update fakta yang sama (IntegrityError trigger update)
179 |     update_res = await memory_store.save_fakta(user_id, "motor", "mioblack", confidence=0.95, source="manual")
    |                                                                                                     ^^^^^^^^^^
180 |     assert update_res > 0
    |

E501 Line too long (137 > 100)
   --> tests/test_memory.py:219:101
    |
217 | …"},
218 | … "api_key": "dummy"}},
219 | …, "path": str(tmp_path / "test.db")}, "long_term": {"backend": "none", "path": ""}},
    |                                                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
220 | …
221 | …
    |

E501 Line too long (141 > 100)
   --> tests/test_memory.py:256:101
    |
254 | …,
255 | …api_key": "dummy"}},
256 | …"path": str(tmp_path / "test.fts.db")}, "long_term": {"backend": "none", "path": ""}},
    |                                               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
257 | …
258 | …
    |

E501 Line too long (120 > 100)
   --> tests/test_memory.py:364:101
    |
363 |     # Check that only the newest 3 messages remain in database
364 |     async with store.db.execute("SELECT content FROM messages WHERE user_id = ? ORDER BY id ASC", (user_id,)) as cursor:
    |                                                                                                     ^^^^^^^^^^^^^^^^^^^^
365 |         rows = await cursor.fetchall()
366 |     contents = [r[0] for r in rows]
    |

E501 Line too long (120 > 100)
   --> tests/test_memory.py:421:101
    |
420 |     # Check that all 5 messages remain in database
421 |     async with store.db.execute("SELECT content FROM messages WHERE user_id = ? ORDER BY id ASC", (user_id,)) as cursor:
    |                                                                                                     ^^^^^^^^^^^^^^^^^^^^
422 |         rows = await cursor.fetchall()
423 |     contents = [r[0] for r in rows]
    |

E501 Line too long (114 > 100)
   --> tests/test_memory.py:425:101
    |
423 |     contents = [r[0] for r in rows]
424 |     assert len(contents) == 5
425 |     assert contents == ["Message apple", "Message banana", "Message cherry", "Message date", "Message elderberry"]
    |                                                                                                     ^^^^^^^^^^^^^^
426 |     
427 |     await store.close()
    |

E501 Line too long (128 > 100)
   --> tests/test_memory.py:458:101
    |
456 |     assert store.vec_db is not None
457 |     # Verify tables exist
458 |     async with store.vec_db.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='semantic_messages'") as cursor:
    |                                                                                                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
459 |         row = await cursor.fetchone()
460 |         assert row is not None
    |

E501 Line too long (110 > 100)
   --> tests/test_memory.py:546:101
    |
545 |     # Verify message stored in semantic_messages
546 |     async with store.vec_db.execute("SELECT content FROM semantic_messages WHERE user_id='user_1'") as cursor:
    |                                                                                                     ^^^^^^^^^^
547 |         row = await cursor.fetchone()
548 |         assert row is not None
    |

E501 Line too long (102 > 100)
  --> tests/test_search.py:18:101
   |
16 |     mock_wiki_id.json.return_value = {
17 |         "query": {
18 |             "search": [{"title": "Python (bahasa pemrograman)", "snippet": "Python adalah bahasa..."}]
   |                                                                                                     ^^
19 |         }
20 |     }
   |

E501 Line too long (106 > 100)
  --> tests/test_search.py:26:101
   |
24 |     mock_wiki_en.json.return_value = {
25 |         "query": {
26 |             "search": [{"title": "Python (programming language)", "snippet": "Python is a high-level..."}]
   |                                                                                                     ^^^^^^
27 |         }
28 |     }
   |

E501 Line too long (125 > 100)
  --> tools/registry.py:39:101
   |
37 |         return f"ERROR Internal: {e}"
38 |
39 | async def save_fact(entity: str, nilai: str, user_id: str, memory, user_input: str = "", gating_enabled: bool = True) -> str:
   |                                                                                                     ^^^^^^^^^^^^^^^^^^^^^^^^^
40 |     """Menyimpan fakta pengguna dengan verifikasi keamanan."""
41 |     if gating_enabled:
   |

E501 Line too long (129 > 100)
  --> tools/registry.py:49:101
   |
47 |     return f"Fakta berhasil disimpan (ID: {fact_id})."
48 |
49 | async def set_preference(kunci: str, nilai: str, user_id: str, memory, user_input: str = "", gating_enabled: bool = True) -> str:
   |                                                                                                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
50 |     """Menyimpan preferensi pengguna dengan verifikasi keamanan."""
51 |     if gating_enabled:
   |

E501 Line too long (104 > 100)
   --> tools/registry.py:102:101
    |
100 |                     title = item.get("title", "")
101 |                     snippet = item.get("snippet", "")
102 |                     snippet = snippet.replace("<span class=\"searchmatch\">", "").replace("</span>", "")
    |                                                                                                     ^^^^
103 |                     wiki_text.append(f"- **{title}**: {snippet}")
104 |                 if wiki_text:
    |

E501 Line too long (104 > 100)
   --> tools/registry.py:121:101
    |
119 |                     title = item.get("title", "")
120 |                     snippet = item.get("snippet", "")
121 |                     snippet = snippet.replace("<span class=\"searchmatch\">", "").replace("</span>", "")
    |                                                                                                     ^^^^
122 |                     wiki_text.append(f"- **{title}**: {snippet}")
123 |                 if wiki_text:
    |

E501 Line too long (169 > 100)
   --> tools/registry.py:139:101
    |
137 | …
138 | …
139 | …ia untuk query/topik tertentu jika agent tidak mengetahui jawabannya atau butuh informasi terbaru.",
    |                                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
140 | …
141 | …
    |

E501 Line too long (118 > 100)
   --> tools/registry.py:145:101
    |
143 |                     "query": {
144 |                         "type": "string",
145 |                         "description": "Kata kunci pencarian (misal: 'perkembangan AI terbaru' atau 'kucing anggora')"
    |                                                                                                     ^^^^^^^^^^^^^^^^^^
146 |                     }
147 |                 },
    |

E501 Line too long (226 > 100)
   --> tools/registry.py:156:101
    |
154 | …
155 | …
156 | … membaca file (cat), listing folder (ls), membuat file, dsb. Command berjalan secara aman di dalam Sandbox (Workspace directory).",
    |       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
157 | …
158 | …
    |

E501 Line too long (103 > 100)
   --> tools/registry.py:179:101
    |
177 |                     "entity": {
178 |                         "type": "string",
179 |                         "description": "Entitas atau subjek fakta (misal: 'nama', 'pekerjaan', 'hobi')"
    |                                                                                                     ^^^
180 |                     },
181 |                     "nilai": {
    |

E501 Line too long (103 > 100)
   --> tools/registry.py:200:101
    |
198 |                     "kunci": {
199 |                         "type": "string",
200 |                         "description": "Kunci preferensi (misal: 'bahasa', 'tema', 'kecepatan_bicara')"
    |                                                                                                     ^^^
201 |                     },
202 |                     "nilai": {
    |

Found 121 errors.
[*] 12 fixable with the `--fix` option.
```

## 3. Security Scan (bandit)

```
[main]	INFO	profile include tests: None
[main]	INFO	profile exclude tests: None
[main]	INFO	cli include tests: None
[main]	INFO	cli exclude tests: None
[main]	INFO	running on Python 3.12.3
[manager]	WARNING	Test in comment: _lines is not a test name or id, ignoring
[manager]	WARNING	Test in comment: is is not a test name or id, ignoring
[manager]	WARNING	Test in comment: a is not a test name or id, ignoring
[manager]	WARNING	Test in comment: dict is not a test name or id, ignoring
[manager]	WARNING	Test in comment: of is not a test name or id, ignoring
[manager]	WARNING	Test in comment: line is not a test name or id, ignoring
[manager]	WARNING	Test in comment: number is not a test name or id, ignoring
[manager]	WARNING	Test in comment: set is not a test name or id, ignoring
[manager]	WARNING	Test in comment: of is not a test name or id, ignoring
[manager]	WARNING	Test in comment: tests is not a test name or id, ignoring
[manager]	WARNING	Test in comment: to is not a test name or id, ignoring
[manager]	WARNING	Test in comment: ignore is not a test name or id, ignoring
[manager]	WARNING	Test in comment: tkelsey is not a test name or id, ignoring
[manager]	WARNING	Test in comment: catching is not a test name or id, ignoring
[manager]	WARNING	Test in comment: expected is not a test name or id, ignoring
[manager]	WARNING	Test in comment: exception is not a test name or id, ignoring
[tester]	WARNING	nosec encountered (B108), but no failed test on file ./.audit-tools/pipx/venvs/bandit/lib/python3.12/site-packages/bandit/plugins/general_hardcoded_tmp.py:61
[manager]	WARNING	Test in comment: c is not a test name or id, ignoring
[manager]	WARNING	Test in comment: B410 is not a test name or id, ignoring
[manager]	WARNING	Test in comment: B320 is not a test name or id, ignoring
[manager]	WARNING	Test in comment: we is not a test name or id, ignoring
[manager]	WARNING	Test in comment: use is not a test name or id, ignoring
[manager]	WARNING	Test in comment: a is not a test name or id, ignoring
[manager]	WARNING	Test in comment: custom is not a test name or id, ignoring
[manager]	WARNING	Test in comment: prepared is not a test name or id, ignoring
[manager]	WARNING	Test in comment: safe is not a test name or id, ignoring
[manager]	WARNING	Test in comment: parser is not a test name or id, ignoring
[manager]	WARNING	Test in comment: nosem is not a test name or id, ignoring
[manager]	WARNING	Test in comment: nosem is not a test name or id, ignoring
Working... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:16:27
Run started:2026-06-07 04:40:23.586337+00:00

Test results:
>> Issue: [B604:any_other_function_with_shell_equals_true] Function call with shell=True parameter identified, possible security issue.
   Severity: Medium   Confidence: Low
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b604_any_other_function_with_shell_equals_true.html
   Location: ./.audit-tools/pipx/shared/lib/python3.12/site-packages/pip/_internal/commands/completion.py:124:18
123	            )
124	            print(BASE_COMPLETION.format(script=script, shell=options.shell))
125	            return SUCCESS

--------------------------------------------------
>> Issue: [B602:subprocess_popen_with_shell_equals_true] subprocess call with shell=True identified, security issue.
   Severity: High   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b602_subprocess_popen_with_shell_equals_true.html
   Location: ./.audit-tools/pipx/shared/lib/python3.12/site-packages/pip/_internal/commands/configuration.py:239:12
238	        try:
239	            subprocess.check_call(f'{editor} "{fname}"', shell=True)
240	        except FileNotFoundError as e:

--------------------------------------------------
>> Issue: [B411:blacklist] Using xmlrpc.client to parse untrusted XML data is known to be vulnerable to XML attacks. Use defusedxml.xmlrpc.monkey_patch() function to monkey-patch xmlrpclib and mitigate XML vulnerabilities.
   Severity: High   Confidence: High
   CWE: CWE-20 (https://cwe.mitre.org/data/definitions/20.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_imports.html#b411-import-xmlrpclib
   Location: ./.audit-tools/pipx/shared/lib/python3.12/site-packages/pip/_internal/commands/search.py:5:0
4	import textwrap
5	import xmlrpc.client
6	from collections import OrderedDict

--------------------------------------------------
>> Issue: [B411:blacklist] Using xmlrpc.client to parse untrusted XML data is known to be vulnerable to XML attacks. Use defusedxml.xmlrpc.monkey_patch() function to monkey-patch xmlrpclib and mitigate XML vulnerabilities.
   Severity: High   Confidence: High
   CWE: CWE-20 (https://cwe.mitre.org/data/definitions/20.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_imports.html#b411-import-xmlrpclib
   Location: ./.audit-tools/pipx/shared/lib/python3.12/site-packages/pip/_internal/network/xmlrpc.py:6:0
5	import urllib.parse
6	import xmlrpc.client
7	from typing import TYPE_CHECKING, Tuple

--------------------------------------------------
>> Issue: [B411:blacklist] Using _HostType to parse untrusted XML data is known to be vulnerable to XML attacks. Use defusedxml.xmlrpc.monkey_patch() function to monkey-patch xmlrpclib and mitigate XML vulnerabilities.
   Severity: High   Confidence: High
   CWE: CWE-20 (https://cwe.mitre.org/data/definitions/20.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_imports.html#b411-import-xmlrpclib
   Location: ./.audit-tools/pipx/shared/lib/python3.12/site-packages/pip/_internal/network/xmlrpc.py:14:4
13	if TYPE_CHECKING:
14	    from xmlrpc.client import _HostType, _Marshallable
15	

--------------------------------------------------
>> Issue: [B411:blacklist] Using xmlrpclib to parse untrusted XML data is known to be vulnerable to XML attacks. Use defusedxml.xmlrpc.monkey_patch() function to monkey-patch xmlrpclib and mitigate XML vulnerabilities.
   Severity: High   Confidence: High
   CWE: CWE-20 (https://cwe.mitre.org/data/definitions/20.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_imports.html#b411-import-xmlrpclib
   Location: ./.audit-tools/pipx/shared/lib/python3.12/site-packages/pip/_vendor/distlib/compat.py:42:4
41	    import httplib
42	    import xmlrpclib
43	    import Queue as queue

--------------------------------------------------
>> Issue: [B411:blacklist] Using xmlrpc.client to parse untrusted XML data is known to be vulnerable to XML attacks. Use defusedxml.xmlrpc.monkey_patch() function to monkey-patch xmlrpclib and mitigate XML vulnerabilities.
   Severity: High   Confidence: High
   CWE: CWE-20 (https://cwe.mitre.org/data/definitions/20.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_imports.html#b411-import-xmlrpclib
   Location: ./.audit-tools/pipx/shared/lib/python3.12/site-packages/pip/_vendor/distlib/compat.py:81:4
80	    import urllib.request as urllib2
81	    import xmlrpc.client as xmlrpclib
82	    import queue

--------------------------------------------------
>> Issue: [B324:hashlib] Use of weak MD5 hash for security. Consider usedforsecurity=False
   Severity: High   Confidence: High
   CWE: CWE-327 (https://cwe.mitre.org/data/definitions/327.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b324_hashlib.html
   Location: ./.audit-tools/pipx/shared/lib/python3.12/site-packages/pip/_vendor/distlib/database.py:1032:19
1031	                f.close()
1032	            return hashlib.md5(content).hexdigest()
1033	

--------------------------------------------------
>> Issue: [B324:hashlib] Use of weak MD5 hash for security. Consider usedforsecurity=False
   Severity: High   Confidence: High
   CWE: CWE-327 (https://cwe.mitre.org/data/definitions/327.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b324_hashlib.html
   Location: ./.audit-tools/pipx/shared/lib/python3.12/site-packages/pip/_vendor/distlib/index.py:269:21
268	            file_data = f.read()
269	        md5_digest = hashlib.md5(file_data).hexdigest()
270	        sha256_digest = hashlib.sha256(file_data).hexdigest()

--------------------------------------------------
>> Issue: [B202:tarfile_unsafe_members] tarfile.extractall used without any validation. Please check and discard dangerous members.
   Severity: High   Confidence: High
   CWE: CWE-22 (https://cwe.mitre.org/data/definitions/22.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b202_tarfile_unsafe_members.html
   Location: ./.audit-tools/pipx/shared/lib/python3.12/site-packages/pip/_vendor/distlib/util.py:1310:8
1309	
1310	        archive.extractall(dest_dir)
1311	

--------------------------------------------------
>> Issue: [B102:exec_used] Use of exec detected.
   Severity: Medium   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b102_exec_used.html
   Location: ./.audit-tools/pipx/shared/lib/python3.12/site-packages/pip/_vendor/pkg_resources/__init__.py:1561:12
1560	            code = compile(source, script_filename, 'exec')
1561	            exec(code, namespace, namespace)
1562	        else:

--------------------------------------------------
>> Issue: [B102:exec_used] Use of exec detected.
   Severity: Medium   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b102_exec_used.html
   Location: ./.audit-tools/pipx/shared/lib/python3.12/site-packages/pip/_vendor/pkg_resources/__init__.py:1572:12
1571	            script_code = compile(script_text, script_filename, 'exec')
1572	            exec(script_code, namespace, namespace)
1573	

--------------------------------------------------
>> Issue: [B108:hardcoded_tmp_directory] Probable insecure usage of temp file/directory.
   Severity: Medium   Confidence: Medium
   CWE: CWE-377 (https://cwe.mitre.org/data/definitions/377.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b108_hardcoded_tmp_directory.html
   Location: ./.audit-tools/pipx/shared/lib/python3.12/site-packages/pip/_vendor/platformdirs/unix.py:103:49
102	        """:return: cache directory shared by users, e.g. ``/var/tmp/$appname/$version``"""
103	        return self._append_app_name_and_version("/var/tmp")  # noqa: S108
104	

--------------------------------------------------
>> Issue: [B108:hardcoded_tmp_directory] Probable insecure usage of temp file/directory.
   Severity: Medium   Confidence: Medium
   CWE: CWE-377 (https://cwe.mitre.org/data/definitions/377.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b108_hardcoded_tmp_directory.html
   Location: ./.audit-tools/pipx/shared/lib/python3.12/site-packages/pip/_vendor/platformdirs/unix.py:164:29
163	                if not Path(path).exists():
164	                    path = f"/tmp/runtime-{getuid()}"  # noqa: S108
165	            else:

--------------------------------------------------
>> Issue: [B102:exec_used] Use of exec detected.
   Severity: Medium   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b102_exec_used.html
   Location: ./.audit-tools/pipx/shared/lib/python3.12/site-packages/pip/_vendor/pygments/formatters/__init__.py:103:12
102	        with open(filename, 'rb') as f:
103	            exec(f.read(), custom_namespace)
104	        # Retrieve the class `formattername` from that namespace

--------------------------------------------------
>> Issue: [B102:exec_used] Use of exec detected.
   Severity: Medium   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b102_exec_used.html
   Location: ./.audit-tools/pipx/shared/lib/python3.12/site-packages/pip/_vendor/pygments/lexers/__init__.py:153:12
152	        with open(filename, 'rb') as f:
153	            exec(f.read(), custom_namespace)
154	        # Retrieve the class `lexername` from that namespace

--------------------------------------------------
>> Issue: [B324:hashlib] Use of weak MD5 hash for security. Consider usedforsecurity=False
   Severity: High   Confidence: High
   CWE: CWE-327 (https://cwe.mitre.org/data/definitions/327.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b324_hashlib.html
   Location: ./.audit-tools/pipx/shared/lib/python3.12/site-packages/pip/_vendor/requests/auth.py:148:23
147	                    x = x.encode("utf-8")
148	                return hashlib.md5(x).hexdigest()
149	

--------------------------------------------------
>> Issue: [B324:hashlib] Use of weak SHA1 hash for security. Consider usedforsecurity=False
   Severity: High   Confidence: High
   CWE: CWE-327 (https://cwe.mitre.org/data/definitions/327.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b324_hashlib.html
   Location: ./.audit-tools/pipx/shared/lib/python3.12/site-packages/pip/_vendor/requests/auth.py:156:23
155	                    x = x.encode("utf-8")
156	                return hashlib.sha1(x).hexdigest()
157	

--------------------------------------------------
>> Issue: [B324:hashlib] Use of weak SHA1 hash for security. Consider usedforsecurity=False
   Severity: High   Confidence: High
   CWE: CWE-327 (https://cwe.mitre.org/data/definitions/327.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b324_hashlib.html
   Location: ./.audit-tools/pipx/shared/lib/python3.12/site-packages/pip/_vendor/requests/auth.py:205:17
204	
205	        cnonce = hashlib.sha1(s).hexdigest()[:16]
206	        if _algorithm == "MD5-SESS":

--------------------------------------------------
>> Issue: [B302:blacklist] Deserialization with the marshal module is possibly dangerous.
   Severity: Medium   Confidence: High
   CWE: CWE-502 (https://cwe.mitre.org/data/definitions/502.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b302-marshal
   Location: ./.audit-tools/pipx/shared/lib/python3.12/site-packages/pip/_vendor/rich/style.py:475:66
474	        """Get meta information (can not be changed after construction)."""
475	        return {} if self._meta is None else cast(Dict[str, Any], loads(self._meta))
476	

--------------------------------------------------
>> Issue: [B102:exec_used] Use of exec detected.
   Severity: Medium   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b102_exec_used.html
   Location: ./.audit-tools/pipx/shared/lib/python3.12/site-packages/pip/_vendor/six.py:735:8
734	            _locs_ = _globs_
735	        exec("""exec _code_ in _globs_, _locs_""")
736	

--------------------------------------------------
>> Issue: [B102:exec_used] Use of exec detected.
   Severity: Medium   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b102_exec_used.html
   Location: ./.audit-tools/pipx/shared/lib/python3.12/site-packages/pip/_vendor/urllib3/packages/six.py:787:8
786	            _locs_ = _globs_
787	        exec ("""exec _code_ in _globs_, _locs_""")
788	

--------------------------------------------------
>> Issue: [B310:blacklist] Audit url open for permitted schemes. Allowing use of file:/ or custom schemes is often unexpected.
   Severity: Medium   Confidence: High
   CWE: CWE-22 (https://cwe.mitre.org/data/definitions/22.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b310-urllib-urlopen
   Location: ./.audit-tools/pipx/shared/lib/python3.12/site-packages/pip/_vendor/webencodings/mklabels.py:47:35
46	         repr(encoding['name']).lstrip('u'))
47	        for category in json.loads(urlopen(url).read().decode('ascii'))
48	        for encoding in category['encodings']

--------------------------------------------------
>> Issue: [B613:trojansource] A Python source file contains bidirectional control characters ('\u202e').
   Severity: High   Confidence: Medium
   CWE: CWE-838 (https://cwe.mitre.org/data/definitions/838.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b613_trojansource.html
   Location: ./.audit-tools/pipx/venvs/bandit/lib/python3.12/site-packages/bandit/plugins/trojansource.py:22:36
21	     3  	access_level = "user"
22	     4	    if access_level != 'none‮⁦': # Check if admin ⁩⁦' and access_level != 'user
23	     5	        print("You are an admin.\n")

--------------------------------------------------
>> Issue: [B102:exec_used] Use of exec detected.
   Severity: Medium   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b102_exec_used.html
   Location: ./.audit-tools/pipx/venvs/bandit/lib/python3.12/site-packages/pygments/formatters/__init__.py:103:12
102	        with open(filename, 'rb') as f:
103	            exec(f.read(), custom_namespace)
104	        # Retrieve the class `formattername` from that namespace

--------------------------------------------------
>> Issue: [B102:exec_used] Use of exec detected.
   Severity: Medium   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b102_exec_used.html
   Location: ./.audit-tools/pipx/venvs/bandit/lib/python3.12/site-packages/pygments/lexers/__init__.py:154:12
153	        with open(filename, 'rb') as f:
154	            exec(f.read(), custom_namespace)
155	        # Retrieve the class `lexername` from that namespace

--------------------------------------------------
>> Issue: [B310:blacklist] Audit url open for permitted schemes. Allowing use of file:/ or custom schemes is often unexpected.
   Severity: Medium   Confidence: High
   CWE: CWE-22 (https://cwe.mitre.org/data/definitions/22.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b310-urllib-urlopen
   Location: ./.audit-tools/pipx/venvs/bandit/lib/python3.12/site-packages/pygments/lexers/_lua_builtins.py:225:12
224	    def get_newest_version():
225	        f = urlopen('http://www.lua.org/manual/')
226	        r = re.compile(r'^<A HREF="(\d\.\d)/">(Lua )?\1</A>')

--------------------------------------------------
>> Issue: [B310:blacklist] Audit url open for permitted schemes. Allowing use of file:/ or custom schemes is often unexpected.
   Severity: Medium   Confidence: High
   CWE: CWE-22 (https://cwe.mitre.org/data/definitions/22.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b310-urllib-urlopen
   Location: ./.audit-tools/pipx/venvs/bandit/lib/python3.12/site-packages/pygments/lexers/_lua_builtins.py:233:12
232	    def get_lua_functions(version):
233	        f = urlopen(f'http://www.lua.org/manual/{version}/')
234	        r = re.compile(r'^<A HREF="manual.html#pdf-(?!lua|LUA)([^:]+)">\1</A>')

--------------------------------------------------
>> Issue: [B310:blacklist] Audit url open for permitted schemes. Allowing use of file:/ or custom schemes is often unexpected.
   Severity: Medium   Confidence: High
   CWE: CWE-22 (https://cwe.mitre.org/data/definitions/22.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b310-urllib-urlopen
   Location: ./.audit-tools/pipx/venvs/bandit/lib/python3.12/site-packages/pygments/lexers/_mysql_builtins.py:1297:19
1296	        # Pull content from lex.h.
1297	        lex_file = urlopen(LEX_URL).read().decode('utf8', errors='ignore')
1298	        keywords = parse_lex_keywords(lex_file)

--------------------------------------------------
>> Issue: [B310:blacklist] Audit url open for permitted schemes. Allowing use of file:/ or custom schemes is often unexpected.
   Severity: Medium   Confidence: High
   CWE: CWE-22 (https://cwe.mitre.org/data/definitions/22.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b310-urllib-urlopen
   Location: ./.audit-tools/pipx/venvs/bandit/lib/python3.12/site-packages/pygments/lexers/_mysql_builtins.py:1303:27
1302	        # Parse content in item_create.cc.
1303	        item_create_file = urlopen(ITEM_CREATE_URL).read().decode('utf8', errors='ignore')
1304	        functions.update(parse_item_create_functions(item_create_file))

--------------------------------------------------
>> Issue: [B310:blacklist] Audit url open for permitted schemes. Allowing use of file:/ or custom schemes is often unexpected.
   Severity: Medium   Confidence: High
   CWE: CWE-22 (https://cwe.mitre.org/data/definitions/22.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b310-urllib-urlopen
   Location: ./.audit-tools/pipx/venvs/bandit/lib/python3.12/site-packages/pygments/lexers/_php_builtins.py:3299:19
3298	    def get_php_references():
3299	        download = urlretrieve(PHP_MANUAL_URL)
3300	        with tarfile.open(download[0]) as tar:

--------------------------------------------------
>> Issue: [B202:tarfile_unsafe_members] tarfile.extractall used without any validation. Please check and discard dangerous members.
   Severity: High   Confidence: High
   CWE: CWE-22 (https://cwe.mitre.org/data/definitions/22.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b202_tarfile_unsafe_members.html
   Location: ./.audit-tools/pipx/venvs/bandit/lib/python3.12/site-packages/pygments/lexers/_php_builtins.py:3304:16
3303	            else:
3304	                tar.extractall()
3305	        yield from glob.glob(f"{PHP_MANUAL_DIR}{PHP_REFERENCE_GLOB}")

--------------------------------------------------
>> Issue: [B310:blacklist] Audit url open for permitted schemes. Allowing use of file:/ or custom schemes is often unexpected.
   Severity: Medium   Confidence: High
   CWE: CWE-22 (https://cwe.mitre.org/data/definitions/22.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b310-urllib-urlopen
   Location: ./.audit-tools/pipx/venvs/bandit/lib/python3.12/site-packages/pygments/lexers/_postgres_builtins.py:642:18
641	    def update_myself():
642	        content = urlopen(DATATYPES_URL).read().decode('utf-8', errors='ignore')
643	        data_file = list(content.splitlines())

--------------------------------------------------
>> Issue: [B310:blacklist] Audit url open for permitted schemes. Allowing use of file:/ or custom schemes is often unexpected.
   Severity: Medium   Confidence: High
   CWE: CWE-22 (https://cwe.mitre.org/data/definitions/22.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b310-urllib-urlopen
   Location: ./.audit-tools/pipx/venvs/bandit/lib/python3.12/site-packages/pygments/lexers/_postgres_builtins.py:647:18
646	
647	        content = urlopen(KEYWORDS_URL).read().decode('utf-8', errors='ignore')
648	        keywords = parse_keywords(content)

--------------------------------------------------
>> Issue: [B301:blacklist] Pickle and modules that wrap it can be unsafe when used to deserialize untrusted data, possible security issue.
   Severity: Medium   Confidence: High
   CWE: CWE-502 (https://cwe.mitre.org/data/definitions/502.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b301-pickle
   Location: ./.audit-tools/pipx/venvs/bandit/lib/python3.12/site-packages/rich/style.py:475:66
474	        """Get meta information (can not be changed after construction)."""
475	        return {} if self._meta is None else cast(Dict[str, Any], loads(self._meta))
476	

--------------------------------------------------
>> Issue: [B108:hardcoded_tmp_directory] Probable insecure usage of temp file/directory.
   Severity: Medium   Confidence: Medium
   CWE: CWE-377 (https://cwe.mitre.org/data/definitions/377.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b108_hardcoded_tmp_directory.html
   Location: ./.audit-tools/pipx/venvs/bandit/lib/python3.12/site-packages/stevedore/_cache.py:153:39
152	                os.path.isfile(os.path.join(self._dir, '.disable')),
153	                sys.executable[0:4] == '/tmp',  # noqa: S108,
154	            ]

--------------------------------------------------
>> Issue: [B108:hardcoded_tmp_directory] Probable insecure usage of temp file/directory.
   Severity: Medium   Confidence: Medium
   CWE: CWE-377 (https://cwe.mitre.org/data/definitions/377.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b108_hardcoded_tmp_directory.html
   Location: ./.audit-tools/pipx/venvs/bandit/lib/python3.12/site-packages/stevedore/tests/test_cache.py:28:50
27	        """
28	        with mock.patch.object(sys, 'executable', '/tmp/fake'):
29	            sot = _cache.Cache()

--------------------------------------------------
>> Issue: [B411:blacklist] Using xmlrpc to parse untrusted XML data is known to be vulnerable to XML attacks. Use defusedxml.xmlrpc.monkey_patch() function to monkey-patch xmlrpclib and mitigate XML vulnerabilities.
   Severity: High   Confidence: High
   CWE: CWE-20 (https://cwe.mitre.org/data/definitions/20.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_imports.html#b411-import-xmlrpclib
   Location: ./.audit-tools/pipx/venvs/pip-audit/lib/python3.12/site-packages/defusedxml/__init__.py:37:4
36	    from . import expatreader
37	    from . import xmlrpc
38	

--------------------------------------------------
>> Issue: [B319:blacklist] Using xml.dom.pulldom.parse to parse untrusted XML data is known to be vulnerable to XML attacks. Replace xml.dom.pulldom.parse with its defusedxml equivalent function or make sure defusedxml.defuse_stdlib() is called
   Severity: Medium   Confidence: High
   CWE: CWE-20 (https://cwe.mitre.org/data/definitions/20.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b313-b320-xml-bad-pulldom
   Location: ./.audit-tools/pipx/venvs/pip-audit/lib/python3.12/site-packages/defusedxml/pulldom.py:30:11
29	        parser.forbid_external = forbid_external
30	    return _parse(stream_or_string, parser, bufsize)
31	

--------------------------------------------------
>> Issue: [B319:blacklist] Using xml.dom.pulldom.parseString to parse untrusted XML data is known to be vulnerable to XML attacks. Replace xml.dom.pulldom.parseString with its defusedxml equivalent function or make sure defusedxml.defuse_stdlib() is called
   Severity: Medium   Confidence: High
   CWE: CWE-20 (https://cwe.mitre.org/data/definitions/20.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b313-b320-xml-bad-pulldom
   Location: ./.audit-tools/pipx/venvs/pip-audit/lib/python3.12/site-packages/defusedxml/pulldom.py:41:11
40	        parser.forbid_external = forbid_external
41	    return _parseString(string, parser)

--------------------------------------------------
>> Issue: [B411:blacklist] Using ExpatParser to parse untrusted XML data is known to be vulnerable to XML attacks. Use defusedxml.xmlrpc.monkey_patch() function to monkey-patch xmlrpclib and mitigate XML vulnerabilities.
   Severity: High   Confidence: High
   CWE: CWE-20 (https://cwe.mitre.org/data/definitions/20.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_imports.html#b411-import-xmlrpclib
   Location: ./.audit-tools/pipx/venvs/pip-audit/lib/python3.12/site-packages/defusedxml/xmlrpc.py:18:4
17	    __origin__ = "xmlrpc.client"
18	    from xmlrpc.client import ExpatParser
19	    from xmlrpc import client as xmlrpc_client

--------------------------------------------------
>> Issue: [B411:blacklist] Using client to parse untrusted XML data is known to be vulnerable to XML attacks. Use defusedxml.xmlrpc.monkey_patch() function to monkey-patch xmlrpclib and mitigate XML vulnerabilities.
   Severity: High   Confidence: High
   CWE: CWE-20 (https://cwe.mitre.org/data/definitions/20.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_imports.html#b411-import-xmlrpclib
   Location: ./.audit-tools/pipx/venvs/pip-audit/lib/python3.12/site-packages/defusedxml/xmlrpc.py:19:4
18	    from xmlrpc.client import ExpatParser
19	    from xmlrpc import client as xmlrpc_client
20	    from xmlrpc import server as xmlrpc_server

--------------------------------------------------
>> Issue: [B411:blacklist] Using server to parse untrusted XML data is known to be vulnerable to XML attacks. Use defusedxml.xmlrpc.monkey_patch() function to monkey-patch xmlrpclib and mitigate XML vulnerabilities.
   Severity: High   Confidence: High
   CWE: CWE-20 (https://cwe.mitre.org/data/definitions/20.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_imports.html#b411-import-xmlrpclib
   Location: ./.audit-tools/pipx/venvs/pip-audit/lib/python3.12/site-packages/defusedxml/xmlrpc.py:20:4
19	    from xmlrpc import client as xmlrpc_client
20	    from xmlrpc import server as xmlrpc_server
21	    from xmlrpc.client import gzip_decode as _orig_gzip_decode

--------------------------------------------------
>> Issue: [B411:blacklist] Using gzip_decode to parse untrusted XML data is known to be vulnerable to XML attacks. Use defusedxml.xmlrpc.monkey_patch() function to monkey-patch xmlrpclib and mitigate XML vulnerabilities.
   Severity: High   Confidence: High
   CWE: CWE-20 (https://cwe.mitre.org/data/definitions/20.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_imports.html#b411-import-xmlrpclib
   Location: ./.audit-tools/pipx/venvs/pip-audit/lib/python3.12/site-packages/defusedxml/xmlrpc.py:21:4
20	    from xmlrpc import server as xmlrpc_server
21	    from xmlrpc.client import gzip_decode as _orig_gzip_decode
22	    from xmlrpc.client import GzipDecodedResponse as _OrigGzipDecodedResponse

--------------------------------------------------
>> Issue: [B411:blacklist] Using GzipDecodedResponse to parse untrusted XML data is known to be vulnerable to XML attacks. Use defusedxml.xmlrpc.monkey_patch() function to monkey-patch xmlrpclib and mitigate XML vulnerabilities.
   Severity: High   Confidence: High
   CWE: CWE-20 (https://cwe.mitre.org/data/definitions/20.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_imports.html#b411-import-xmlrpclib
   Location: ./.audit-tools/pipx/venvs/pip-audit/lib/python3.12/site-packages/defusedxml/xmlrpc.py:22:4
21	    from xmlrpc.client import gzip_decode as _orig_gzip_decode
22	    from xmlrpc.client import GzipDecodedResponse as _OrigGzipDecodedResponse
23	else:

--------------------------------------------------
>> Issue: [B411:blacklist] Using ExpatParser to parse untrusted XML data is known to be vulnerable to XML attacks. Use defusedxml.xmlrpc.monkey_patch() function to monkey-patch xmlrpclib and mitigate XML vulnerabilities.
   Severity: High   Confidence: High
   CWE: CWE-20 (https://cwe.mitre.org/data/definitions/20.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_imports.html#b411-import-xmlrpclib
   Location: ./.audit-tools/pipx/venvs/pip-audit/lib/python3.12/site-packages/defusedxml/xmlrpc.py:25:4
24	    __origin__ = "xmlrpclib"
25	    from xmlrpclib import ExpatParser
26	    import xmlrpclib as xmlrpc_client

--------------------------------------------------
>> Issue: [B411:blacklist] Using xmlrpclib to parse untrusted XML data is known to be vulnerable to XML attacks. Use defusedxml.xmlrpc.monkey_patch() function to monkey-patch xmlrpclib and mitigate XML vulnerabilities.
   Severity: High   Confidence: High
   CWE: CWE-20 (https://cwe.mitre.org/data/definitions/20.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_imports.html#b411-import-xmlrpclib
   Location: ./.audit-tools/pipx/venvs/pip-audit/lib/python3.12/site-packages/defusedxml/xmlrpc.py:26:4
25	    from xmlrpclib import ExpatParser
26	    import xmlrpclib as xmlrpc_client
27	

--------------------------------------------------
>> Issue: [B411:blacklist] Using gzip_decode to parse untrusted XML data is known to be vulnerable to XML attacks. Use defusedxml.xmlrpc.monkey_patch() function to monkey-patch xmlrpclib and mitigate XML vulnerabilities.
   Severity: High   Confidence: High
   CWE: CWE-20 (https://cwe.mitre.org/data/definitions/20.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_imports.html#b411-import-xmlrpclib
   Location: ./.audit-tools/pipx/venvs/pip-audit/lib/python3.12/site-packages/defusedxml/xmlrpc.py:29:4
28	    xmlrpc_server = None
29	    from xmlrpclib import gzip_decode as _orig_gzip_decode
30	    from xmlrpclib import GzipDecodedResponse as _OrigGzipDecodedResponse

--------------------------------------------------
>> Issue: [B411:blacklist] Using GzipDecodedResponse to parse untrusted XML data is known to be vulnerable to XML attacks. Use defusedxml.xmlrpc.monkey_patch() function to monkey-patch xmlrpclib and mitigate XML vulnerabilities.
   Severity: High   Confidence: High
   CWE: CWE-20 (https://cwe.mitre.org/data/definitions/20.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_imports.html#b411-import-xmlrpclib
   Location: ./.audit-tools/pipx/venvs/pip-audit/lib/python3.12/site-packages/defusedxml/xmlrpc.py:30:4
29	    from xmlrpclib import gzip_decode as _orig_gzip_decode
30	    from xmlrpclib import GzipDecodedResponse as _OrigGzipDecodedResponse
31	

--------------------------------------------------
>> Issue: [B108:hardcoded_tmp_directory] Probable insecure usage of temp file/directory.
   Severity: Medium   Confidence: Medium
   CWE: CWE-377 (https://cwe.mitre.org/data/definitions/377.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b108_hardcoded_tmp_directory.html
   Location: ./.audit-tools/pipx/venvs/pip-audit/lib/python3.12/site-packages/platformdirs/unix.py:184:21
183	        if sys.platform.startswith("openbsd"):
184	            path = f"/tmp/run/user/{getuid()}"  # noqa: S108
185	        elif sys.platform.startswith(("freebsd", "netbsd")):

--------------------------------------------------
>> Issue: [B307:blacklist] Use of possibly insecure function - consider using safer ast.literal_eval.
   Severity: Medium   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b307-eval
   Location: ./.audit-tools/pipx/venvs/pip-audit/lib/python3.12/site-packages/py_serializable/__init__.py:974:42
973	                            # Will load any class already loaded assuming fully qualified name
974	                            self._type_ = eval(f'{mapped_array_type}[{results.get("array_of")}]')
975	                            self._concrete_type = eval(str(results.get('array_of')))

--------------------------------------------------
>> Issue: [B307:blacklist] Use of possibly insecure function - consider using safer ast.literal_eval.
   Severity: Medium   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b307-eval
   Location: ./.audit-tools/pipx/venvs/pip-audit/lib/python3.12/site-packages/py_serializable/__init__.py:975:50
974	                            self._type_ = eval(f'{mapped_array_type}[{results.get("array_of")}]')
975	                            self._concrete_type = eval(str(results.get('array_of')))
976	                        except NameError:

--------------------------------------------------
>> Issue: [B307:blacklist] Use of possibly insecure function - consider using safer ast.literal_eval.
   Severity: Medium   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b307-eval
   Location: ./.audit-tools/pipx/venvs/pip-audit/lib/python3.12/site-packages/py_serializable/__init__.py:1007:42
1006	                            # Will load any class already loaded assuming fully qualified name
1007	                            self._type_ = eval(f'{mapped_array_type}[{results.get("array_of")}]')
1008	                            self._concrete_type = eval(str(results.get('array_of')))

--------------------------------------------------
>> Issue: [B307:blacklist] Use of possibly insecure function - consider using safer ast.literal_eval.
   Severity: Medium   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b307-eval
   Location: ./.audit-tools/pipx/venvs/pip-audit/lib/python3.12/site-packages/py_serializable/__init__.py:1008:50
1007	                            self._type_ = eval(f'{mapped_array_type}[{results.get("array_of")}]')
1008	                            self._concrete_type = eval(str(results.get('array_of')))
1009	                        except NameError:

--------------------------------------------------
>> Issue: [B102:exec_used] Use of exec detected.
   Severity: Medium   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b102_exec_used.html
   Location: ./.audit-tools/pipx/venvs/pip-audit/lib/python3.12/site-packages/pygments/formatters/__init__.py:103:12
102	        with open(filename, 'rb') as f:
103	            exec(f.read(), custom_namespace)
104	        # Retrieve the class `formattername` from that namespace

--------------------------------------------------
>> Issue: [B102:exec_used] Use of exec detected.
   Severity: Medium   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b102_exec_used.html
   Location: ./.audit-tools/pipx/venvs/pip-audit/lib/python3.12/site-packages/pygments/lexers/__init__.py:154:12
153	        with open(filename, 'rb') as f:
154	            exec(f.read(), custom_namespace)
155	        # Retrieve the class `lexername` from that namespace

--------------------------------------------------
>> Issue: [B310:blacklist] Audit url open for permitted schemes. Allowing use of file:/ or custom schemes is often unexpected.
   Severity: Medium   Confidence: High
   CWE: CWE-22 (https://cwe.mitre.org/data/definitions/22.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b310-urllib-urlopen
   Location: ./.audit-tools/pipx/venvs/pip-audit/lib/python3.12/site-packages/pygments/lexers/_lua_builtins.py:225:12
224	    def get_newest_version():
225	        f = urlopen('http://www.lua.org/manual/')
226	        r = re.compile(r'^<A HREF="(\d\.\d)/">(Lua )?\1</A>')

--------------------------------------------------
>> Issue: [B310:blacklist] Audit url open for permitted schemes. Allowing use of file:/ or custom schemes is often unexpected.
   Severity: Medium   Confidence: High
   CWE: CWE-22 (https://cwe.mitre.org/data/definitions/22.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b310-urllib-urlopen
   Location: ./.audit-tools/pipx/venvs/pip-audit/lib/python3.12/site-packages/pygments/lexers/_lua_builtins.py:233:12
232	    def get_lua_functions(version):
233	        f = urlopen(f'http://www.lua.org/manual/{version}/')
234	        r = re.compile(r'^<A HREF="manual.html#pdf-(?!lua|LUA)([^:]+)">\1</A>')

--------------------------------------------------
>> Issue: [B310:blacklist] Audit url open for permitted schemes. Allowing use of file:/ or custom schemes is often unexpected.
   Severity: Medium   Confidence: High
   CWE: CWE-22 (https://cwe.mitre.org/data/definitions/22.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b310-urllib-urlopen
   Location: ./.audit-tools/pipx/venvs/pip-audit/lib/python3.12/site-packages/pygments/lexers/_mysql_builtins.py:1297:19
1296	        # Pull content from lex.h.
1297	        lex_file = urlopen(LEX_URL).read().decode('utf8', errors='ignore')
1298	        keywords = parse_lex_keywords(lex_file)

--------------------------------------------------
>> Issue: [B310:blacklist] Audit url open for permitted schemes. Allowing use of file:/ or custom schemes is often unexpected.
   Severity: Medium   Confidence: High
   CWE: CWE-22 (https://cwe.mitre.org/data/definitions/22.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b310-urllib-urlopen
   Location: ./.audit-tools/pipx/venvs/pip-audit/lib/python3.12/site-packages/pygments/lexers/_mysql_builtins.py:1303:27
1302	        # Parse content in item_create.cc.
1303	        item_create_file = urlopen(ITEM_CREATE_URL).read().decode('utf8', errors='ignore')
1304	        functions.update(parse_item_create_functions(item_create_file))

--------------------------------------------------
>> Issue: [B310:blacklist] Audit url open for permitted schemes. Allowing use of file:/ or custom schemes is often unexpected.
   Severity: Medium   Confidence: High
   CWE: CWE-22 (https://cwe.mitre.org/data/definitions/22.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b310-urllib-urlopen
   Location: ./.audit-tools/pipx/venvs/pip-audit/lib/python3.12/site-packages/pygments/lexers/_php_builtins.py:3299:19
3298	    def get_php_references():
3299	        download = urlretrieve(PHP_MANUAL_URL)
3300	        with tarfile.open(download[0]) as tar:

--------------------------------------------------
>> Issue: [B202:tarfile_unsafe_members] tarfile.extractall used without any validation. Please check and discard dangerous members.
   Severity: High   Confidence: High
   CWE: CWE-22 (https://cwe.mitre.org/data/definitions/22.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b202_tarfile_unsafe_members.html
   Location: ./.audit-tools/pipx/venvs/pip-audit/lib/python3.12/site-packages/pygments/lexers/_php_builtins.py:3304:16
3303	            else:
3304	                tar.extractall()
3305	        yield from glob.glob(f"{PHP_MANUAL_DIR}{PHP_REFERENCE_GLOB}")

--------------------------------------------------
>> Issue: [B310:blacklist] Audit url open for permitted schemes. Allowing use of file:/ or custom schemes is often unexpected.
   Severity: Medium   Confidence: High
   CWE: CWE-22 (https://cwe.mitre.org/data/definitions/22.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b310-urllib-urlopen
   Location: ./.audit-tools/pipx/venvs/pip-audit/lib/python3.12/site-packages/pygments/lexers/_postgres_builtins.py:642:18
641	    def update_myself():
642	        content = urlopen(DATATYPES_URL).read().decode('utf-8', errors='ignore')
643	        data_file = list(content.splitlines())

--------------------------------------------------
>> Issue: [B310:blacklist] Audit url open for permitted schemes. Allowing use of file:/ or custom schemes is often unexpected.
   Severity: Medium   Confidence: High
   CWE: CWE-22 (https://cwe.mitre.org/data/definitions/22.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b310-urllib-urlopen
   Location: ./.audit-tools/pipx/venvs/pip-audit/lib/python3.12/site-packages/pygments/lexers/_postgres_builtins.py:647:18
646	
647	        content = urlopen(KEYWORDS_URL).read().decode('utf-8', errors='ignore')
648	        keywords = parse_keywords(content)

--------------------------------------------------
>> Issue: [B301:blacklist] Pickle and modules that wrap it can be unsafe when used to deserialize untrusted data, possible security issue.
   Severity: Medium   Confidence: High
   CWE: CWE-502 (https://cwe.mitre.org/data/definitions/502.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b301-pickle
   Location: ./.audit-tools/pipx/venvs/pip-audit/lib/python3.12/site-packages/rich/style.py:475:66
474	        """Get meta information (can not be changed after construction)."""
475	        return {} if self._meta is None else cast(Dict[str, Any], loads(self._meta))
476	

--------------------------------------------------
>> Issue: [B307:blacklist] Use of possibly insecure function - consider using safer ast.literal_eval.
   Severity: Medium   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b307-eval
   Location: ./.audit-tools/pipx/venvs/pip-audit/lib/python3.12/site-packages/typing_extensions.py:4034:53
4033	        return_value = {key:
4034	            value if not isinstance(value, str) else eval(value, globals, locals)
4035	            for key, value in ann.items() }

--------------------------------------------------
>> Issue: [B307:blacklist] Use of possibly insecure function - consider using safer ast.literal_eval.
   Severity: Medium   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b307-eval
   Location: ./.audit-tools/pipx/venvs/pip-audit/lib/python3.12/site-packages/typing_extensions.py:4116:20
4115	            code = forward_ref.__forward_code__
4116	            value = eval(code, globals, locals)
4117	        forward_ref.__forward_evaluated__ = True

--------------------------------------------------
>> Issue: [B604:any_other_function_with_shell_equals_true] Function call with shell=True parameter identified, possible security issue.
   Severity: Medium   Confidence: Low
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b604_any_other_function_with_shell_equals_true.html
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/anyio/_backends/_trio.py:1103:28
1102	                stderr=stderr,
1103	                shell=True,
1104	                **kwargs,
1105	            )
1106	        else:
1107	            process = await trio.lowlevel.open_process(
1108	                [convert_item(item) for item in command],
1109	                stdin=stdin,
1110	                stdout=stdout,
1111	                stderr=stderr,

--------------------------------------------------
>> Issue: [B104:hardcoded_bind_all_interfaces] Possible binding to all interfaces.
   Severity: Medium   Confidence: Medium
   CWE: CWE-605 (https://cwe.mitre.org/data/definitions/605.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b104_hardcoded_bind_all_interfaces.html
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/anyio/_core/_sockets.py:490:25
489	    else:
490	        local_address = ("0.0.0.0", 0)
491	

--------------------------------------------------
>> Issue: [B610:django_extra_used] Use of extra potential SQL attack vector.
   Severity: Medium   Confidence: Medium
   CWE: CWE-89 (https://cwe.mitre.org/data/definitions/89.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b610_django_extra_used.html
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/anyio/streams/tls.py:249:22
248	    async def send_eof(self) -> None:
249	        tls_version = self.extra(TLSAttribute.tls_version)
250	        match = re.match(r"TLSv(\d+)(?:\.(\d+))?", tls_version)

--------------------------------------------------
>> Issue: [B301:blacklist] Pickle and modules that wrap it can be unsafe when used to deserialize untrusted data, possible security issue.
   Severity: Medium   Confidence: High
   CWE: CWE-502 (https://cwe.mitre.org/data/definitions/502.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b301-pickle
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/anyio/to_interpreter.py:130:22
129	            if fmt == FMT_PICKLED:
130	                res = pickle.loads(res)
131	

--------------------------------------------------
>> Issue: [B301:blacklist] Pickle and modules that wrap it can be unsafe when used to deserialize untrusted data, possible security issue.
   Severity: Medium   Confidence: High
   CWE: CWE-502 (https://cwe.mitre.org/data/definitions/502.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b301-pickle
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/anyio/to_process.py:94:17
93	
94	        retval = pickle.loads(pickled_response)
95	        if status == b"EXCEPTION":

--------------------------------------------------
>> Issue: [B301:blacklist] Pickle and modules that wrap it can be unsafe when used to deserialize untrusted data, possible security issue.
   Severity: Medium   Confidence: High
   CWE: CWE-502 (https://cwe.mitre.org/data/definitions/502.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b301-pickle
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/anyio/to_process.py:218:29
217	        try:
218	            command, *args = pickle.load(stdin.buffer)
219	        except EOFError:

--------------------------------------------------
>> Issue: [B303:blacklist] Use of insecure MD2, MD4, MD5, or SHA1 hash function.
   Severity: Medium   Confidence: High
   CWE: CWE-327 (https://cwe.mitre.org/data/definitions/327.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b303-md5
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/authlib/jose/rfc7518/jwe_algs.py:329:34
328	        "RSAES OAEP using default parameters",
329	        padding.OAEP(padding.MGF1(hashes.SHA1()), hashes.SHA1(), None),
330	    ),

--------------------------------------------------
>> Issue: [B303:blacklist] Use of insecure MD2, MD4, MD5, or SHA1 hash function.
   Severity: Medium   Confidence: High
   CWE: CWE-327 (https://cwe.mitre.org/data/definitions/327.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b303-md5
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/authlib/jose/rfc7518/jwe_algs.py:329:50
328	        "RSAES OAEP using default parameters",
329	        padding.OAEP(padding.MGF1(hashes.SHA1()), hashes.SHA1(), None),
330	    ),

--------------------------------------------------
>> Issue: [B324:hashlib] Use of weak SHA1 hash for security. Consider usedforsecurity=False
   Severity: High   Confidence: High
   CWE: CWE-327 (https://cwe.mitre.org/data/definitions/327.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b324_hashlib.html
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/authlib/oauth1/rfc5849/client_auth.py:150:47
149	        if body and headers.get("Content-Type") != CONTENT_TYPE_FORM_URLENCODED:
150	            oauth_body_hash = base64.b64encode(hashlib.sha1(body).digest())
151	            oauth_params.append(("oauth_body_hash", oauth_body_hash.decode("utf-8")))

--------------------------------------------------
>> Issue: [B303:blacklist] Use of insecure MD2, MD4, MD5, or SHA1 hash function.
   Severity: Medium   Confidence: High
   CWE: CWE-327 (https://cwe.mitre.org/data/definitions/327.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b303-md5
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/authlib/oauth1/rfc5849/rsa.py:15:45
14	    )
15	    return key.sign(msg, padding.PKCS1v15(), hashes.SHA1())
16	

--------------------------------------------------
>> Issue: [B303:blacklist] Use of insecure MD2, MD4, MD5, or SHA1 hash function.
   Severity: Medium   Confidence: High
   CWE: CWE-327 (https://cwe.mitre.org/data/definitions/327.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b303-md5
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/authlib/oauth1/rfc5849/rsa.py:21:49
20	    try:
21	        key.verify(sig, msg, padding.PKCS1v15(), hashes.SHA1())
22	        return True

--------------------------------------------------
>> Issue: [B307:blacklist] Use of possibly insecure function - consider using safer ast.literal_eval.
   Severity: Medium   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b307-eval
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/cffi/recompiler.py:78:16
77	    def as_python_expr(self):
78	        flags = eval(self.flags, G_FLAGS)
79	        fields_expr = [c_field.as_field_python_expr()

--------------------------------------------------
>> Issue: [B102:exec_used] Use of exec detected.
   Severity: Medium   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b102_exec_used.html
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/cffi/setuptools_ext.py:26:4
25	    code = compile(src, filename, 'exec')
26	    exec(code, glob, glob)
27	

--------------------------------------------------
>> Issue: [B303:blacklist] Use of insecure MD2, MD4, MD5, or SHA1 hash function.
   Severity: Medium   Confidence: High
   CWE: CWE-327 (https://cwe.mitre.org/data/definitions/327.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b303-md5
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/cryptography/hazmat/_oid.py:128:40
127	_SIG_OIDS_TO_HASH: dict[ObjectIdentifier, hashes.HashAlgorithm | None] = {
128	    SignatureAlgorithmOID.RSA_WITH_MD5: hashes.MD5(),
129	    SignatureAlgorithmOID.RSA_WITH_SHA1: hashes.SHA1(),

--------------------------------------------------
>> Issue: [B303:blacklist] Use of insecure MD2, MD4, MD5, or SHA1 hash function.
   Severity: Medium   Confidence: High
   CWE: CWE-327 (https://cwe.mitre.org/data/definitions/327.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b303-md5
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/cryptography/hazmat/_oid.py:129:41
128	    SignatureAlgorithmOID.RSA_WITH_MD5: hashes.MD5(),
129	    SignatureAlgorithmOID.RSA_WITH_SHA1: hashes.SHA1(),
130	    SignatureAlgorithmOID._RSA_WITH_SHA1: hashes.SHA1(),

--------------------------------------------------
>> Issue: [B303:blacklist] Use of insecure MD2, MD4, MD5, or SHA1 hash function.
   Severity: Medium   Confidence: High
   CWE: CWE-327 (https://cwe.mitre.org/data/definitions/327.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b303-md5
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/cryptography/hazmat/_oid.py:130:42
129	    SignatureAlgorithmOID.RSA_WITH_SHA1: hashes.SHA1(),
130	    SignatureAlgorithmOID._RSA_WITH_SHA1: hashes.SHA1(),
131	    SignatureAlgorithmOID.RSA_WITH_SHA224: hashes.SHA224(),

--------------------------------------------------
>> Issue: [B303:blacklist] Use of insecure MD2, MD4, MD5, or SHA1 hash function.
   Severity: Medium   Confidence: High
   CWE: CWE-327 (https://cwe.mitre.org/data/definitions/327.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b303-md5
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/cryptography/hazmat/_oid.py:139:43
138	    SignatureAlgorithmOID.RSA_WITH_SHA3_512: hashes.SHA3_512(),
139	    SignatureAlgorithmOID.ECDSA_WITH_SHA1: hashes.SHA1(),
140	    SignatureAlgorithmOID.ECDSA_WITH_SHA224: hashes.SHA224(),

--------------------------------------------------
>> Issue: [B303:blacklist] Use of insecure MD2, MD4, MD5, or SHA1 hash function.
   Severity: Medium   Confidence: High
   CWE: CWE-327 (https://cwe.mitre.org/data/definitions/327.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b303-md5
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/cryptography/hazmat/_oid.py:148:41
147	    SignatureAlgorithmOID.ECDSA_WITH_SHA3_512: hashes.SHA3_512(),
148	    SignatureAlgorithmOID.DSA_WITH_SHA1: hashes.SHA1(),
149	    SignatureAlgorithmOID.DSA_WITH_SHA224: hashes.SHA224(),

--------------------------------------------------
>> Issue: [B305:blacklist] Use of insecure cipher mode cryptography.hazmat.primitives.ciphers.modes.ECB.
   Severity: Medium   Confidence: High
   CWE: CWE-327 (https://cwe.mitre.org/data/definitions/327.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b304-b305-ciphers-and-modes
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/cryptography/hazmat/primitives/keywrap.py:21:42
20	    # RFC 3394 Key Wrap - 2.2.1 (index method)
21	    encryptor = Cipher(AES(wrapping_key), ECB()).encryptor()
22	    n = len(r)

--------------------------------------------------
>> Issue: [B305:blacklist] Use of insecure cipher mode cryptography.hazmat.primitives.ciphers.modes.ECB.
   Severity: Medium   Confidence: High
   CWE: CWE-327 (https://cwe.mitre.org/data/definitions/327.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b304-b305-ciphers-and-modes
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/cryptography/hazmat/primitives/keywrap.py:64:42
63	    # Implement RFC 3394 Key Unwrap - 2.2.2 (index method)
64	    decryptor = Cipher(AES(wrapping_key), ECB()).decryptor()
65	    n = len(r)

--------------------------------------------------
>> Issue: [B305:blacklist] Use of insecure cipher mode cryptography.hazmat.primitives.ciphers.modes.ECB.
   Severity: Medium   Confidence: High
   CWE: CWE-327 (https://cwe.mitre.org/data/definitions/327.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b304-b305-ciphers-and-modes
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/cryptography/hazmat/primitives/keywrap.py:100:46
99	        # RFC 5649 - 4.1 - exactly 8 octets after padding
100	        encryptor = Cipher(AES(wrapping_key), ECB()).encryptor()
101	        b = encryptor.update(aiv + key_to_wrap)

--------------------------------------------------
>> Issue: [B305:blacklist] Use of insecure cipher mode cryptography.hazmat.primitives.ciphers.modes.ECB.
   Severity: Medium   Confidence: High
   CWE: CWE-327 (https://cwe.mitre.org/data/definitions/327.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b304-b305-ciphers-and-modes
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/cryptography/hazmat/primitives/keywrap.py:122:46
121	        # RFC 5649 - 4.2 - exactly two 64-bit blocks
122	        decryptor = Cipher(AES(wrapping_key), ECB()).decryptor()
123	        out = decryptor.update(wrapped_key)

--------------------------------------------------
>> Issue: [B303:blacklist] Use of insecure MD2, MD4, MD5, or SHA1 hash function.
   Severity: Medium   Confidence: High
   CWE: CWE-327 (https://cwe.mitre.org/data/definitions/327.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b303-md5
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/cryptography/hazmat/primitives/serialization/ssh.py:1009:27
1008	            if self._inner_sig_type == _SSH_RSA:
1009	                hash_alg = hashes.SHA1()
1010	            elif self._inner_sig_type == _SSH_RSA_SHA256:

--------------------------------------------------
>> Issue: [B324:hashlib] Use of weak SHA1 hash for security. Consider usedforsecurity=False
   Severity: High   Confidence: High
   CWE: CWE-327 (https://cwe.mitre.org/data/definitions/327.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b324_hashlib.html
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/cryptography/x509/extensions.py:72:11
71	
72	    return hashlib.sha1(data).digest()
73	

--------------------------------------------------
>> Issue: [B610:django_extra_used] Use of extra potential SQL attack vector.
   Severity: Medium   Confidence: Medium
   CWE: CWE-89 (https://cwe.mitre.org/data/definitions/89.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b610_django_extra_used.html
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/httpcore/_backends/anyio.py:84:19
83	        if info == "ssl_object":
84	            return self._stream.extra(anyio.streams.tls.TLSAttribute.ssl_object, None)
85	        if info == "client_addr":

--------------------------------------------------
>> Issue: [B610:django_extra_used] Use of extra potential SQL attack vector.
   Severity: Medium   Confidence: Medium
   CWE: CWE-89 (https://cwe.mitre.org/data/definitions/89.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b610_django_extra_used.html
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/httpcore/_backends/anyio.py:86:19
85	        if info == "client_addr":
86	            return self._stream.extra(anyio.abc.SocketAttribute.local_address, None)
87	        if info == "server_addr":

--------------------------------------------------
>> Issue: [B610:django_extra_used] Use of extra potential SQL attack vector.
   Severity: Medium   Confidence: Medium
   CWE: CWE-89 (https://cwe.mitre.org/data/definitions/89.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b610_django_extra_used.html
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/httpcore/_backends/anyio.py:88:19
87	        if info == "server_addr":
88	            return self._stream.extra(anyio.abc.SocketAttribute.remote_address, None)
89	        if info == "socket":

--------------------------------------------------
>> Issue: [B610:django_extra_used] Use of extra potential SQL attack vector.
   Severity: Medium   Confidence: Medium
   CWE: CWE-89 (https://cwe.mitre.org/data/definitions/89.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b610_django_extra_used.html
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/httpcore/_backends/anyio.py:90:19
89	        if info == "socket":
90	            return self._stream.extra(anyio.abc.SocketAttribute.raw_socket, None)
91	        if info == "is_readable":

--------------------------------------------------
>> Issue: [B610:django_extra_used] Use of extra potential SQL attack vector.
   Severity: Medium   Confidence: Medium
   CWE: CWE-89 (https://cwe.mitre.org/data/definitions/89.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b610_django_extra_used.html
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/httpcore/_backends/anyio.py:92:19
91	        if info == "is_readable":
92	            sock = self._stream.extra(anyio.abc.SocketAttribute.raw_socket, None)
93	            return is_socket_readable(sock)

--------------------------------------------------
>> Issue: [B324:hashlib] Use of weak SHA1 hash for security. Consider usedforsecurity=False
   Severity: High   Confidence: High
   CWE: CWE-327 (https://cwe.mitre.org/data/definitions/327.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b324_hashlib.html
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/httpx/_auth.py:309:15
308	
309	        return hashlib.sha1(s).hexdigest()[:16].encode()
310	

--------------------------------------------------
>> Issue: [B301:blacklist] Pickle and modules that wrap it can be unsafe when used to deserialize untrusted data, possible security issue.
   Severity: Medium   Confidence: High
   CWE: CWE-502 (https://cwe.mitre.org/data/definitions/502.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b301-pickle
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/jinja2/bccache.py:73:19
72	        # the source code of the file changed, we need to reload
73	        checksum = pickle.load(f)
74	        if self.checksum != checksum:

--------------------------------------------------
>> Issue: [B302:blacklist] Deserialization with the marshal module is possibly dangerous.
   Severity: Medium   Confidence: High
   CWE: CWE-502 (https://cwe.mitre.org/data/definitions/502.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b302-marshal
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/jinja2/bccache.py:79:24
78	        try:
79	            self.code = marshal.load(f)
80	        except (EOFError, ValueError, TypeError):

--------------------------------------------------
>> Issue: [B324:hashlib] Use of weak SHA1 hash for security. Consider usedforsecurity=False
   Severity: High   Confidence: High
   CWE: CWE-327 (https://cwe.mitre.org/data/definitions/327.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b324_hashlib.html
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/jinja2/bccache.py:156:15
155	        """Returns the unique hash key for this template name."""
156	        hash = sha1(name.encode("utf-8"))
157	

--------------------------------------------------
>> Issue: [B324:hashlib] Use of weak SHA1 hash for security. Consider usedforsecurity=False
   Severity: High   Confidence: High
   CWE: CWE-327 (https://cwe.mitre.org/data/definitions/327.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b324_hashlib.html
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/jinja2/bccache.py:165:15
164	        """Returns a checksum for the source."""
165	        return sha1(source.encode("utf-8")).hexdigest()
166	

--------------------------------------------------
>> Issue: [B102:exec_used] Use of exec detected.
   Severity: Medium   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b102_exec_used.html
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/jinja2/debug.py:145:8
144	    try:
145	        exec(code, globals, locals)
146	    except BaseException:

--------------------------------------------------
>> Issue: [B102:exec_used] Use of exec detected.
   Severity: Medium   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b102_exec_used.html
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/jinja2/environment.py:1228:8
1227	        namespace = {"environment": environment, "__file__": code.co_filename}
1228	        exec(code, namespace)
1229	        rv = cls._from_namespace(environment, namespace, globals)

--------------------------------------------------
>> Issue: [B704:markupsafe_markup_xss] Potential XSS with ``markupsafe.Markup`` detected. Do not use ``Markup`` on untrusted data.
   Severity: Medium   Confidence: High
   CWE: CWE-79 (https://cwe.mitre.org/data/definitions/79.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b704_markupsafe_markup_xss.html
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/jinja2/environment.py:1544:15
1543	    def __html__(self) -> Markup:
1544	        return Markup(concat(self._body_stream))
1545	

--------------------------------------------------
>> Issue: [B704:markupsafe_markup_xss] Potential XSS with ``markupsafe.Markup`` detected. Do not use ``Markup`` on untrusted data.
   Severity: Medium   Confidence: High
   CWE: CWE-79 (https://cwe.mitre.org/data/definitions/79.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b704_markupsafe_markup_xss.html
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/jinja2/ext.py:176:17
175	        if __context.eval_ctx.autoescape:
176	            rv = Markup(rv)
177	        # Always treat as a format string, even if there are no

--------------------------------------------------
>> Issue: [B704:markupsafe_markup_xss] Potential XSS with ``markupsafe.Markup`` detected. Do not use ``Markup`` on untrusted data.
   Severity: Medium   Confidence: High
   CWE: CWE-79 (https://cwe.mitre.org/data/definitions/79.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b704_markupsafe_markup_xss.html
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/jinja2/ext.py:197:17
196	        if __context.eval_ctx.autoescape:
197	            rv = Markup(rv)
198	        # Always treat as a format string, see gettext comment above.

--------------------------------------------------
>> Issue: [B704:markupsafe_markup_xss] Potential XSS with ``markupsafe.Markup`` detected. Do not use ``Markup`` on untrusted data.
   Severity: Medium   Confidence: High
   CWE: CWE-79 (https://cwe.mitre.org/data/definitions/79.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b704_markupsafe_markup_xss.html
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/jinja2/ext.py:213:17
212	        if __context.eval_ctx.autoescape:
213	            rv = Markup(rv)
214	

--------------------------------------------------
>> Issue: [B704:markupsafe_markup_xss] Potential XSS with ``markupsafe.Markup`` detected. Do not use ``Markup`` on untrusted data.
   Severity: Medium   Confidence: High
   CWE: CWE-79 (https://cwe.mitre.org/data/definitions/79.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b704_markupsafe_markup_xss.html
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/jinja2/ext.py:238:17
237	        if __context.eval_ctx.autoescape:
238	            rv = Markup(rv)
239	

--------------------------------------------------
>> Issue: [B704:markupsafe_markup_xss] Potential XSS with ``markupsafe.Markup`` detected. Do not use ``Markup`` on untrusted data.
   Severity: Medium   Confidence: High
   CWE: CWE-79 (https://cwe.mitre.org/data/definitions/79.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b704_markupsafe_markup_xss.html
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/jinja2/filters.py:316:13
315	    if eval_ctx.autoescape:
316	        rv = Markup(rv)
317	

--------------------------------------------------
>> Issue: [B704:markupsafe_markup_xss] Potential XSS with ``markupsafe.Markup`` detected. Do not use ``Markup`` on untrusted data.
   Severity: Medium   Confidence: High
   CWE: CWE-79 (https://cwe.mitre.org/data/definitions/79.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b704_markupsafe_markup_xss.html
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/jinja2/filters.py:820:13
819	    if eval_ctx.autoescape:
820	        rv = Markup(rv)
821	

--------------------------------------------------
>> Issue: [B704:markupsafe_markup_xss] Potential XSS with ``markupsafe.Markup`` detected. Do not use ``Markup`` on untrusted data.
   Severity: Medium   Confidence: High
   CWE: CWE-79 (https://cwe.mitre.org/data/definitions/79.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b704_markupsafe_markup_xss.html
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/jinja2/filters.py:851:20
850	    if isinstance(s, Markup):
851	        indention = Markup(indention)
852	        newline = Markup(newline)

--------------------------------------------------
>> Issue: [B704:markupsafe_markup_xss] Potential XSS with ``markupsafe.Markup`` detected. Do not use ``Markup`` on untrusted data.
   Severity: Medium   Confidence: High
   CWE: CWE-79 (https://cwe.mitre.org/data/definitions/79.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b704_markupsafe_markup_xss.html
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/jinja2/filters.py:852:18
851	        indention = Markup(indention)
852	        newline = Markup(newline)
853	

--------------------------------------------------
>> Issue: [B704:markupsafe_markup_xss] Potential XSS with ``markupsafe.Markup`` detected. Do not use ``Markup`` on untrusted data.
   Severity: Medium   Confidence: High
   CWE: CWE-79 (https://cwe.mitre.org/data/definitions/79.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b704_markupsafe_markup_xss.html
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/jinja2/filters.py:1056:11
1055	
1056	    return Markup(str(value)).striptags()
1057	

--------------------------------------------------
>> Issue: [B704:markupsafe_markup_xss] Potential XSS with ``markupsafe.Markup`` detected. Do not use ``Markup`` on untrusted data.
   Severity: Medium   Confidence: High
   CWE: CWE-79 (https://cwe.mitre.org/data/definitions/79.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b704_markupsafe_markup_xss.html
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/jinja2/filters.py:1377:11
1376	    """
1377	    return Markup(value)
1378	

--------------------------------------------------
>> Issue: [B324:hashlib] Use of weak SHA1 hash for security. Consider usedforsecurity=False
   Severity: High   Confidence: High
   CWE: CWE-327 (https://cwe.mitre.org/data/definitions/327.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b324_hashlib.html
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/jinja2/loaders.py:661:25
660	    def get_template_key(name: str) -> str:
661	        return "tmpl_" + sha1(name.encode("utf-8")).hexdigest()
662	

--------------------------------------------------
>> Issue: [B704:markupsafe_markup_xss] Potential XSS with ``markupsafe.Markup`` detected. Do not use ``Markup`` on untrusted data.
   Severity: Medium   Confidence: High
   CWE: CWE-79 (https://cwe.mitre.org/data/definitions/79.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b704_markupsafe_markup_xss.html
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/jinja2/nodes.py:619:19
618	        if eval_ctx.autoescape:
619	            return Markup(self.data)
620	        return self.data

--------------------------------------------------
>> Issue: [B704:markupsafe_markup_xss] Potential XSS with ``markupsafe.Markup`` detected. Do not use ``Markup`` on untrusted data.
   Severity: Medium   Confidence: High
   CWE: CWE-79 (https://cwe.mitre.org/data/definitions/79.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b704_markupsafe_markup_xss.html
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/jinja2/nodes.py:1091:15
1090	        eval_ctx = get_eval_context(self, eval_ctx)
1091	        return Markup(self.expr.as_const(eval_ctx))
1092	

--------------------------------------------------
>> Issue: [B704:markupsafe_markup_xss] Potential XSS with ``markupsafe.Markup`` detected. Do not use ``Markup`` on untrusted data.
   Severity: Medium   Confidence: High
   CWE: CWE-79 (https://cwe.mitre.org/data/definitions/79.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b704_markupsafe_markup_xss.html
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/jinja2/nodes.py:1112:19
1111	        if eval_ctx.autoescape:
1112	            return Markup(expr)
1113	        return expr

--------------------------------------------------
>> Issue: [B704:markupsafe_markup_xss] Potential XSS with ``markupsafe.Markup`` detected. Do not use ``Markup`` on untrusted data.
   Severity: Medium   Confidence: High
   CWE: CWE-79 (https://cwe.mitre.org/data/definitions/79.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b704_markupsafe_markup_xss.html
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/jinja2/runtime.py:375:19
374	        if self._context.eval_ctx.autoescape:
375	            return Markup(rv)
376	

--------------------------------------------------
>> Issue: [B704:markupsafe_markup_xss] Potential XSS with ``markupsafe.Markup`` detected. Do not use ``Markup`` on untrusted data.
   Severity: Medium   Confidence: High
   CWE: CWE-79 (https://cwe.mitre.org/data/definitions/79.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b704_markupsafe_markup_xss.html
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/jinja2/runtime.py:389:19
388	        if self._context.eval_ctx.autoescape:
389	            return Markup(rv)
390	

--------------------------------------------------
>> Issue: [B704:markupsafe_markup_xss] Potential XSS with ``markupsafe.Markup`` detected. Do not use ``Markup`` on untrusted data.
   Severity: Medium   Confidence: High
   CWE: CWE-79 (https://cwe.mitre.org/data/definitions/79.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b704_markupsafe_markup_xss.html
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/jinja2/runtime.py:776:19
775	        if autoescape:
776	            return Markup(rv)
777	

--------------------------------------------------
>> Issue: [B704:markupsafe_markup_xss] Potential XSS with ``markupsafe.Markup`` detected. Do not use ``Markup`` on untrusted data.
   Severity: Medium   Confidence: High
   CWE: CWE-79 (https://cwe.mitre.org/data/definitions/79.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b704_markupsafe_markup_xss.html
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/jinja2/runtime.py:787:17
786	        if autoescape:
787	            rv = Markup(rv)
788	

--------------------------------------------------
>> Issue: [B704:markupsafe_markup_xss] Potential XSS with ``markupsafe.Markup`` detected. Do not use ``Markup`` on untrusted data.
   Severity: Medium   Confidence: High
   CWE: CWE-79 (https://cwe.mitre.org/data/definitions/79.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b704_markupsafe_markup_xss.html
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/jinja2/utils.py:403:11
402	        return "\n\n".join(result)
403	    return markupsafe.Markup(
404	        "\n".join(f"<p>{markupsafe.escape(x)}</p>" for x in result)
405	    )
406	

--------------------------------------------------
>> Issue: [B704:markupsafe_markup_xss] Potential XSS with ``markupsafe.Markup`` detected. Do not use ``Markup`` on untrusted data.
   Severity: Medium   Confidence: High
   CWE: CWE-79 (https://cwe.mitre.org/data/definitions/79.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b704_markupsafe_markup_xss.html
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/jinja2/utils.py:668:11
667	
668	    return markupsafe.Markup(
669	        dumps(obj, **kwargs)
670	        .replace("<", "\\u003c")
671	        .replace(">", "\\u003e")
672	        .replace("&", "\\u0026")
673	        .replace("'", "\\u0027")
674	    )
675	

--------------------------------------------------
>> Issue: [B108:hardcoded_tmp_directory] Probable insecure usage of temp file/directory.
   Severity: Medium   Confidence: Medium
   CWE: CWE-377 (https://cwe.mitre.org/data/definitions/377.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b108_hardcoded_tmp_directory.html
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/joblib/_memmapping_reducer.py:40:23
39	# as the default folder to dump big arrays to share with subprocesses.
40	SYSTEM_SHARED_MEM_FS = "/dev/shm"
41	

--------------------------------------------------
>> Issue: [B301:blacklist] Pickle and modules that wrap it can be unsafe when used to deserialize untrusted data, possible security issue.
   Severity: Medium   Confidence: High
   CWE: CWE-502 (https://cwe.mitre.org/data/definitions/502.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b301-pickle
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/joblib/externals/loky/backend/popen_loky_posix.py:174:28
173	            try:
174	                prep_data = pickle.load(from_parent)
175	                spawn.prepare(prep_data)

--------------------------------------------------
>> Issue: [B301:blacklist] Pickle and modules that wrap it can be unsafe when used to deserialize untrusted data, possible security issue.
   Severity: Medium   Confidence: High
   CWE: CWE-502 (https://cwe.mitre.org/data/definitions/502.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b301-pickle
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/joblib/externals/loky/backend/popen_loky_posix.py:176:30
175	                spawn.prepare(prep_data)
176	                process_obj = pickle.load(from_parent)
177	            finally:

--------------------------------------------------
>> Issue: [B301:blacklist] Pickle and modules that wrap it can be unsafe when used to deserialize untrusted data, possible security issue.
   Severity: Medium   Confidence: High
   CWE: CWE-502 (https://cwe.mitre.org/data/definitions/502.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b301-pickle
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/joblib/externals/loky/backend/popen_loky_win32.py:166:31
165	        try:
166	            preparation_data = load(from_parent)
167	            spawn.prepare(preparation_data, parent_sentinel)

--------------------------------------------------
>> Issue: [B301:blacklist] Pickle and modules that wrap it can be unsafe when used to deserialize untrusted data, possible security issue.
   Severity: Medium   Confidence: High
   CWE: CWE-502 (https://cwe.mitre.org/data/definitions/502.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b301-pickle
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/joblib/externals/loky/backend/popen_loky_win32.py:168:19
167	            spawn.prepare(preparation_data, parent_sentinel)
168	            self = load(from_parent)
169	        finally:

--------------------------------------------------
>> Issue: [B301:blacklist] Pickle and modules that wrap it can be unsafe when used to deserialize untrusted data, possible security issue.
   Severity: Medium   Confidence: High
   CWE: CWE-502 (https://cwe.mitre.org/data/definitions/502.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b301-pickle
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/joblib/numpy_pickle.py:175:20
174	            # The array contained Python objects. We need to unpickle the data.
175	            array = pickle.load(unpickler.file_handle)
176	        else:

--------------------------------------------------
>> Issue: [B108:hardcoded_tmp_directory] Probable insecure usage of temp file/directory.
   Severity: Medium   Confidence: Medium
   CWE: CWE-377 (https://cwe.mitre.org/data/definitions/377.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b108_hardcoded_tmp_directory.html
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/joblib/test/common.py:78:23
77	with_dev_shm = skipif(
78	    not os.path.exists("/dev/shm"),
79	    reason="This test requires a large /dev/shm shared memory fs.",

--------------------------------------------------
>> Issue: [B324:hashlib] Use of weak MD5 hash for security. Consider usedforsecurity=False
   Severity: High   Confidence: High
   CWE: CWE-327 (https://cwe.mitre.org/data/definitions/327.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b324_hashlib.html
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/joblib/test/test_hashing.py:228:15
227	    def md5_hash(x):
228	        return hashlib.md5(memoryview(x)).hexdigest()
229	

--------------------------------------------------
>> Issue: [B301:blacklist] Pickle and modules that wrap it can be unsafe when used to deserialize untrusted data, possible security issue.
   Severity: Medium   Confidence: High
   CWE: CWE-502 (https://cwe.mitre.org/data/definitions/502.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b301-pickle
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/joblib/test/test_hashing.py:350:8
349	    b = {string: "bar"}
350	    c = pickle.loads(pickle.dumps(b))
351	    assert hash([a, b]) == hash([a, c])

--------------------------------------------------
>> Issue: [B301:blacklist] Pickle and modules that wrap it can be unsafe when used to deserialize untrusted data, possible security issue.
   Severity: Medium   Confidence: High
   CWE: CWE-502 (https://cwe.mitre.org/data/definitions/502.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b301-pickle
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/joblib/test/test_hashing.py:370:23
369	
370	    dt1_roundtripped = pickle.loads(pickle.dumps(dt1))
371	    assert dt1 is not dt1_roundtripped

--------------------------------------------------
>> Issue: [B301:blacklist] Pickle and modules that wrap it can be unsafe when used to deserialize untrusted data, possible security issue.
   Severity: Medium   Confidence: High
   CWE: CWE-502 (https://cwe.mitre.org/data/definitions/502.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b301-pickle
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/joblib/test/test_hashing.py:383:31
382	
383	    complex_dt1_roundtripped = pickle.loads(pickle.dumps(complex_dt1))
384	    assert complex_dt1_roundtripped is not complex_dt1

--------------------------------------------------
>> Issue: [B108:hardcoded_tmp_directory] Probable insecure usage of temp file/directory.
   Severity: Medium   Confidence: Medium
   CWE: CWE-377 (https://cwe.mitre.org/data/definitions/377.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b108_hardcoded_tmp_directory.html
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/joblib/test/test_memmapping.py:937:28
936	            pool_temp_folder = p._temp_folder
937	            folder_prefix = "/dev/shm/joblib_memmapping_folder_"
938	            assert pool_temp_folder.startswith(folder_prefix)

--------------------------------------------------
>> Issue: [B108:hardcoded_tmp_directory] Probable insecure usage of temp file/directory.
   Severity: Medium   Confidence: Medium
   CWE: CWE-377 (https://cwe.mitre.org/data/definitions/377.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b108_hardcoded_tmp_directory.html
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/joblib/test/test_memmapping.py:993:51
992	            pool_temp_folder = p._temp_folder
993	            assert not pool_temp_folder.startswith("/dev/shm")
994	        finally:

--------------------------------------------------
>> Issue: [B102:exec_used] Use of exec detected.
   Severity: Medium   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b102_exec_used.html
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/joblib/test/test_memory.py:164:8
163	        my_locals = {}
164	        exec(
165	            compile(
166	                textwrap.dedent(ipython_cell_source),
167	                filename=ipython_cell_id,
168	                mode="exec",
169	            ),
170	            # TODO when Python 3.11 is the minimum supported version, use
171	            # locals=my_locals instead of passing globals and locals in the
172	            # next two lines as positional arguments
173	            None,
174	            my_locals,
175	        )
176	        f = my_locals["f"]

--------------------------------------------------
>> Issue: [B307:blacklist] Use of possibly insecure function - consider using safer ast.literal_eval.
   Severity: Medium   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b307-eval
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/joblib/test/test_memory.py:334:9
333	    memory = Memory(location=tmpdir.strpath, verbose=0)
334	    a1 = eval("lambda x: x")
335	    a1 = memory.cache(a1)

--------------------------------------------------
>> Issue: [B307:blacklist] Use of possibly insecure function - consider using safer ast.literal_eval.
   Severity: Medium   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b307-eval
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/joblib/test/test_memory.py:336:9
335	    a1 = memory.cache(a1)
336	    b1 = eval("lambda x: x+1")
337	    b1 = memory.cache(b1)

--------------------------------------------------
>> Issue: [B307:blacklist] Use of possibly insecure function - consider using safer ast.literal_eval.
   Severity: Medium   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b307-eval
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/joblib/test/test_memory.py:368:8
367	
368	    m = eval("lambda x: x")
369	    mm = memory.cache(m)

--------------------------------------------------
>> Issue: [B301:blacklist] Pickle and modules that wrap it can be unsafe when used to deserialize untrusted data, possible security issue.
   Severity: Medium   Confidence: High
   CWE: CWE-502 (https://cwe.mitre.org/data/definitions/502.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b301-pickle
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/joblib/test/test_memory.py:598:8
597	
598	    h = pickle.loads(pickle.dumps(g))
599	

--------------------------------------------------
>> Issue: [B301:blacklist] Pickle and modules that wrap it can be unsafe when used to deserialize untrusted data, possible security issue.
   Severity: Medium   Confidence: High
   CWE: CWE-502 (https://cwe.mitre.org/data/definitions/502.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b301-pickle
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/joblib/test/test_memory.py:604:14
603	    assert output == h.store_backend.load_item([h.func_id, args_id])
604	    memory2 = pickle.loads(pickle.dumps(memory))
605	    assert memory.store_backend.location == memory2.store_backend.location

--------------------------------------------------
>> Issue: [B301:blacklist] Pickle and modules that wrap it can be unsafe when used to deserialize untrusted data, possible security issue.
   Severity: Medium   Confidence: High
   CWE: CWE-502 (https://cwe.mitre.org/data/definitions/502.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b301-pickle
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/joblib/test/test_memory.py:609:4
608	    memory = Memory(location=None, verbose=0)
609	    pickle.loads(pickle.dumps(memory))
610	    g = memory.cache(f)

--------------------------------------------------
>> Issue: [B301:blacklist] Pickle and modules that wrap it can be unsafe when used to deserialize untrusted data, possible security issue.
   Severity: Medium   Confidence: High
   CWE: CWE-502 (https://cwe.mitre.org/data/definitions/502.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b301-pickle
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/joblib/test/test_memory.py:611:9
610	    g = memory.cache(f)
611	    gp = pickle.loads(pickle.dumps(g))
612	    gp(1)

--------------------------------------------------
>> Issue: [B301:blacklist] Pickle and modules that wrap it can be unsafe when used to deserialize untrusted data, possible security issue.
   Severity: Medium   Confidence: High
   CWE: CWE-502 (https://cwe.mitre.org/data/definitions/502.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b301-pickle
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/joblib/test/test_memory.py:704:22
703	        with open(filename, "rb") as fp:
704	            result2 = pickle.load(fp)
705	        assert result2.get() == result.get()

--------------------------------------------------
>> Issue: [B108:hardcoded_tmp_directory] Probable insecure usage of temp file/directory.
   Severity: Medium   Confidence: Medium
   CWE: CWE-377 (https://cwe.mitre.org/data/definitions/377.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b108_hardcoded_tmp_directory.html
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/joblib/test/test_memory.py:1219:24
1218	    with raises(TypeError) as excinfo:
1219	        Memory(location="/tmp/joblib", backend="unknown")
1220	    excinfo.match(r"Unknown location*")

--------------------------------------------------
>> Issue: [B301:blacklist] Pickle and modules that wrap it can be unsafe when used to deserialize untrusted data, possible security issue.
   Severity: Medium   Confidence: High
   CWE: CWE-502 (https://cwe.mitre.org/data/definitions/502.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b301-pickle
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/joblib/test/test_memory.py:1340:29
1339	    memorized_result_pickle = pickle.dumps(memorized_result)
1340	    memorized_result_loads = pickle.loads(memorized_result_pickle)
1341	

--------------------------------------------------
>> Issue: [B301:blacklist] Pickle and modules that wrap it can be unsafe when used to deserialize untrusted data, possible security issue.
   Severity: Medium   Confidence: High
   CWE: CWE-502 (https://cwe.mitre.org/data/definitions/502.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b301-pickle
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/joblib/test/test_memory.py:1374:22
1373	
1374	    memory_reloaded = pickle.loads(pickle.dumps(memory))
1375	

--------------------------------------------------
>> Issue: [B301:blacklist] Pickle and modules that wrap it can be unsafe when used to deserialize untrusted data, possible security issue.
   Severity: Medium   Confidence: High
   CWE: CWE-502 (https://cwe.mitre.org/data/definitions/502.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b301-pickle
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/joblib/test/test_memory.py:1387:27
1386	
1387	    func_cached_reloaded = pickle.loads(pickle.dumps(func_cached))
1388	

--------------------------------------------------
>> Issue: [B301:blacklist] Pickle and modules that wrap it can be unsafe when used to deserialize untrusted data, possible security issue.
   Severity: Medium   Confidence: High
   CWE: CWE-502 (https://cwe.mitre.org/data/definitions/502.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b301-pickle
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/joblib/test/test_memory.py:1400:32
1399	    memorized_result = func_cached.call_and_shelve(1)
1400	    memorized_result_reloaded = pickle.loads(pickle.dumps(memorized_result))
1401	

--------------------------------------------------
>> Issue: [B301:blacklist] Pickle and modules that wrap it can be unsafe when used to deserialize untrusted data, possible security issue.
   Severity: Medium   Confidence: High
   CWE: CWE-502 (https://cwe.mitre.org/data/definitions/502.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b301-pickle
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/joblib/test/test_store_backends.py:33:27
32	            with open(filename, "rb") as f:
33	                reloaded = cpickle.load(f)
34	            break

--------------------------------------------------
>> Issue: [B303:blacklist] Use of insecure MD2, MD4, MD5, or SHA1 hash function.
   Severity: Medium   Confidence: High
   CWE: CWE-327 (https://cwe.mitre.org/data/definitions/327.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b303-md5
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/joserfc/_rfc7518/jwe_algs.py:322:34
321	        "RSAES OAEP using default parameters",
322	        padding.OAEP(padding.MGF1(hashes.SHA1()), hashes.SHA1(), None),
323	        True,

--------------------------------------------------
>> Issue: [B303:blacklist] Use of insecure MD2, MD4, MD5, or SHA1 hash function.
   Severity: Medium   Confidence: High
   CWE: CWE-327 (https://cwe.mitre.org/data/definitions/327.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b303-md5
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/joserfc/_rfc7518/jwe_algs.py:322:50
321	        "RSAES OAEP using default parameters",
322	        padding.OAEP(padding.MGF1(hashes.SHA1()), hashes.SHA1(), None),
323	        True,

--------------------------------------------------
>> Issue: [B413:blacklist] The pyCrypto library and its module ChaCha20_Poly1305 are no longer actively maintained and have been deprecated. Consider using pyca/cryptography library.
   Severity: High   Confidence: High
   CWE: CWE-327 (https://cwe.mitre.org/data/definitions/327.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_imports.html#b413-import-pycrypto
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/joserfc/drafts/jwe_chacha20.py:1:0
1	from Crypto.Cipher import ChaCha20_Poly1305
2	from .._rfc7516.registry import JWERegistry
3	from .._rfc7516.models import JWEEncModel

--------------------------------------------------
>> Issue: [B314:blacklist] Using xml.etree.ElementTree.parse to parse untrusted XML data is known to be vulnerable to XML attacks. Replace xml.etree.ElementTree.parse with its defusedxml equivalent function or make sure defusedxml.defuse_stdlib() is called
   Severity: Medium   Confidence: High
   CWE: CWE-20 (https://cwe.mitre.org/data/definitions/20.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b313-b320-xml-bad-elementtree
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/nltk/chunk/named_entity.py:236:14
235	    with open(annfile) as infile:
236	        xml = ET.parse(infile).getroot()
237	    for entity in xml.findall("document/entity"):

--------------------------------------------------
>> Issue: [B108:hardcoded_tmp_directory] Probable insecure usage of temp file/directory.
   Severity: Medium   Confidence: Medium
   CWE: CWE-377 (https://cwe.mitre.org/data/definitions/377.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b108_hardcoded_tmp_directory.html
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/nltk/chunk/named_entity.py:350:57
349	        fmt = self._fmt
350	        save_maxent_params(wgt, mpg, lab, aon, tab_dir=f"/tmp/english_ace_{fmt}/")
351	

--------------------------------------------------
>> Issue: [B108:hardcoded_tmp_directory] Probable insecure usage of temp file/directory.
   Severity: Medium   Confidence: Medium
   CWE: CWE-377 (https://cwe.mitre.org/data/definitions/377.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b108_hardcoded_tmp_directory.html
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/nltk/classify/maxent.py:1583:51
1582	
1583	def save_maxent_params(wgt, mpg, lab, aon, tab_dir="/tmp"):
1584	

--------------------------------------------------
>> Issue: [B108:hardcoded_tmp_directory] Probable insecure usage of temp file/directory.
   Severity: Medium   Confidence: Medium
   CWE: CWE-377 (https://cwe.mitre.org/data/definitions/377.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b108_hardcoded_tmp_directory.html
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/nltk/classify/weka.py:375:36
374	    def make_classifier(featuresets):
375	        return WekaClassifier.train("/tmp/name.model", featuresets, "C4.5")
376	

--------------------------------------------------
>> Issue: [B314:blacklist] Using xml.etree.ElementTree.parse to parse untrusted XML data is known to be vulnerable to XML attacks. Replace xml.etree.ElementTree.parse with its defusedxml equivalent function or make sure defusedxml.defuse_stdlib() is called
   Severity: Medium   Confidence: High
   CWE: CWE-20 (https://cwe.mitre.org/data/definitions/20.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b313-b320-xml-bad-elementtree
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/nltk/corpus/reader/bcp47.py:40:16
39	            self.subdiv = self.subdiv_dict(
40	                et.parse(fp).iterfind("localeDisplayNames/subdivisions/subdivision")
41	            )

--------------------------------------------------
>> Issue: [B314:blacklist] Using xml.etree.ElementTree.parse to parse untrusted XML data is known to be vulnerable to XML attacks. Replace xml.etree.ElementTree.parse with its defusedxml equivalent function or make sure defusedxml.defuse_stdlib() is called
   Severity: Medium   Confidence: High
   CWE: CWE-20 (https://cwe.mitre.org/data/definitions/20.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b313-b320-xml-bad-elementtree
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/nltk/corpus/reader/nombank.py:111:20
110	        with self.abspath(framefile).open() as fp:
111	            etree = ElementTree.parse(fp).getroot()
112	        for roleset in etree.findall("predicate/roleset"):

--------------------------------------------------
>> Issue: [B314:blacklist] Using xml.etree.ElementTree.parse to parse untrusted XML data is known to be vulnerable to XML attacks. Replace xml.etree.ElementTree.parse with its defusedxml equivalent function or make sure defusedxml.defuse_stdlib() is called
   Severity: Medium   Confidence: High
   CWE: CWE-20 (https://cwe.mitre.org/data/definitions/20.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b313-b320-xml-bad-elementtree
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/nltk/corpus/reader/nombank.py:134:24
133	            with self.abspath(framefile).open() as fp:
134	                etree = ElementTree.parse(fp).getroot()
135	            rsets.append(etree.findall("predicate/roleset"))

--------------------------------------------------
>> Issue: [B314:blacklist] Using xml.etree.ElementTree.parse to parse untrusted XML data is known to be vulnerable to XML attacks. Replace xml.etree.ElementTree.parse with its defusedxml equivalent function or make sure defusedxml.defuse_stdlib() is called
   Severity: Medium   Confidence: High
   CWE: CWE-20 (https://cwe.mitre.org/data/definitions/20.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b313-b320-xml-bad-elementtree
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/nltk/corpus/reader/propbank.py:107:20
106	        with self.abspath(framefile).open() as fp:
107	            etree = ElementTree.parse(fp).getroot()
108	        for roleset in etree.findall("predicate/roleset"):

--------------------------------------------------
>> Issue: [B314:blacklist] Using xml.etree.ElementTree.parse to parse untrusted XML data is known to be vulnerable to XML attacks. Replace xml.etree.ElementTree.parse with its defusedxml equivalent function or make sure defusedxml.defuse_stdlib() is called
   Severity: Medium   Confidence: High
   CWE: CWE-20 (https://cwe.mitre.org/data/definitions/20.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b313-b320-xml-bad-elementtree
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/nltk/corpus/reader/propbank.py:130:24
129	            with self.abspath(framefile).open() as fp:
130	                etree = ElementTree.parse(fp).getroot()
131	            rsets.append(etree.findall("predicate/roleset"))

--------------------------------------------------
>> Issue: [B314:blacklist] Using xml.etree.ElementTree.fromstring to parse untrusted XML data is known to be vulnerable to XML attacks. Replace xml.etree.ElementTree.fromstring with its defusedxml equivalent function or make sure defusedxml.defuse_stdlib() is called
   Severity: Medium   Confidence: High
   CWE: CWE-20 (https://cwe.mitre.org/data/definitions/20.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b313-b320-xml-bad-elementtree
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/nltk/corpus/reader/senseval.py:114:23
113	                xml_block = _fixXML(xml_block)
114	                inst = ElementTree.fromstring(xml_block)
115	                return [self._parse_instance(inst, lexelt)]

--------------------------------------------------
>> Issue: [B314:blacklist] Using xml.etree.ElementTree.parse to parse untrusted XML data is known to be vulnerable to XML attacks. Replace xml.etree.ElementTree.parse with its defusedxml equivalent function or make sure defusedxml.defuse_stdlib() is called
   Severity: Medium   Confidence: High
   CWE: CWE-20 (https://cwe.mitre.org/data/definitions/20.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b313-b320-xml-bad-elementtree
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/nltk/corpus/reader/xmldocs.py:45:18
44	        with self.abspath(fileid).open() as fp:
45	            elt = ElementTree.parse(fp).getroot()
46	        # If requested, wrap it.

--------------------------------------------------
>> Issue: [B314:blacklist] Using xml.etree.ElementTree.fromstring to parse untrusted XML data is known to be vulnerable to XML attacks. Replace xml.etree.ElementTree.fromstring with its defusedxml equivalent function or make sure defusedxml.defuse_stdlib() is called
   Severity: Medium   Confidence: High
   CWE: CWE-20 (https://cwe.mitre.org/data/definitions/20.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b313-b320-xml-bad-elementtree
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/nltk/corpus/reader/xmldocs.py:393:16
392	            elt_handler(
393	                ElementTree.fromstring(elt.encode("ascii", "xmlcharrefreplace")),
394	                context,

--------------------------------------------------
>> Issue: [B307:blacklist] Use of possibly insecure function - consider using safer ast.literal_eval.
   Severity: Medium   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b307-eval
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/nltk/decorators.py:136:14
135	    src = "lambda %(signature)s: _wrapper_(%(signature)s)" % infodict
136	    funcopy = eval(src, dict(_wrapper_=wrapper))
137	    return update_wrapper(funcopy, model, infodict)

--------------------------------------------------
>> Issue: [B307:blacklist] Use of possibly insecure function - consider using safer ast.literal_eval.
   Severity: Medium   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b307-eval
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/nltk/decorators.py:204:19
203	        # import sys; print >> sys.stderr, src # for debugging purposes
204	        dec_func = eval(src, dict(_func_=func, _call_=caller))
205	        return update_wrapper(dec_func, func, infodict)

--------------------------------------------------
>> Issue: [B314:blacklist] Using xml.etree.ElementTree.parse to parse untrusted XML data is known to be vulnerable to XML attacks. Replace xml.etree.ElementTree.parse with its defusedxml equivalent function or make sure defusedxml.defuse_stdlib() is called
   Severity: Medium   Confidence: High
   CWE: CWE-20 (https://cwe.mitre.org/data/definitions/20.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b313-b320-xml-bad-elementtree
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/nltk/downloader.py:280:18
279	        if isinstance(xml, str):
280	            xml = ElementTree.parse(xml)
281	        for key in xml.attrib:

--------------------------------------------------
>> Issue: [B314:blacklist] Using xml.etree.ElementTree.parse to parse untrusted XML data is known to be vulnerable to XML attacks. Replace xml.etree.ElementTree.parse with its defusedxml equivalent function or make sure defusedxml.defuse_stdlib() is called
   Severity: Medium   Confidence: High
   CWE: CWE-20 (https://cwe.mitre.org/data/definitions/20.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b313-b320-xml-bad-elementtree
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/nltk/downloader.py:320:18
319	        if isinstance(xml, str):
320	            xml = ElementTree.parse(xml)
321	        for key in xml.attrib:

--------------------------------------------------
>> Issue: [B314:blacklist] Using xml.etree.ElementTree.parse to parse untrusted XML data is known to be vulnerable to XML attacks. Replace xml.etree.ElementTree.parse with its defusedxml equivalent function or make sure defusedxml.defuse_stdlib() is called
   Severity: Medium   Confidence: High
   CWE: CWE-20 (https://cwe.mitre.org/data/definitions/20.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b313-b320-xml-bad-elementtree
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/nltk/downloader.py:980:12
979	        self._index = nltk.internals.ElementWrapper(
980	            ElementTree.parse(urlopen(self._url)).getroot()
981	        )

--------------------------------------------------
>> Issue: [B324:hashlib] Use of weak MD5 hash for security. Consider usedforsecurity=False
   Severity: High   Confidence: High
   CWE: CWE-327 (https://cwe.mitre.org/data/definitions/327.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b324_hashlib.html
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/nltk/downloader.py:2288:17
2287	def _md5_hexdigest(fp):
2288	    md5_digest = md5()
2289	    while True:

--------------------------------------------------
>> Issue: [B314:blacklist] Using xml.etree.ElementTree.parse to parse untrusted XML data is known to be vulnerable to XML attacks. Replace xml.etree.ElementTree.parse with its defusedxml equivalent function or make sure defusedxml.defuse_stdlib() is called
   Severity: Medium   Confidence: High
   CWE: CWE-20 (https://cwe.mitre.org/data/definitions/20.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b313-b320-xml-bad-elementtree
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/nltk/downloader.py:2587:22
2586	                xmlfile = os.path.join(dirname, filename)
2587	                yield ElementTree.parse(xmlfile).getroot()
2588	

--------------------------------------------------
>> Issue: [B314:blacklist] Using xml.etree.ElementTree.parse to parse untrusted XML data is known to be vulnerable to XML attacks. Replace xml.etree.ElementTree.parse with its defusedxml equivalent function or make sure defusedxml.defuse_stdlib() is called
   Severity: Medium   Confidence: High
   CWE: CWE-20 (https://cwe.mitre.org/data/definitions/20.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b313-b320-xml-bad-elementtree
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/nltk/downloader.py:2615:30
2614	                try:
2615	                    pkg_xml = ElementTree.parse(xmlfilename).getroot()
2616	                except Exception as e:

--------------------------------------------------
>> Issue: [B307:blacklist] Use of possibly insecure function - consider using safer ast.literal_eval.
   Severity: Medium   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b307-eval
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/nltk/internals.py:231:15
230	    try:
231	        return eval(s[start_position : match.end()]), match.end()
232	    except ValueError as e:

--------------------------------------------------
>> Issue: [B314:blacklist] Using xml.etree.ElementTree.fromstring to parse untrusted XML data is known to be vulnerable to XML attacks. Replace xml.etree.ElementTree.fromstring with its defusedxml equivalent function or make sure defusedxml.defuse_stdlib() is called
   Severity: Medium   Confidence: High
   CWE: CWE-20 (https://cwe.mitre.org/data/definitions/20.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b313-b320-xml-bad-elementtree
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/nltk/internals.py:924:20
923	        if isinstance(etree, str):
924	            etree = ElementTree.fromstring(etree)
925	        self.__dict__["_etree"] = etree

--------------------------------------------------
>> Issue: [B113:request_without_timeout] Call to requests without timeout
   Severity: Medium   Confidence: Low
   CWE: CWE-400 (https://cwe.mitre.org/data/definitions/400.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b113_request_without_timeout.html
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/nltk/parse/corenlp.py:151:27
150	            try:
151	                response = requests.get(requests.compat.urljoin(self.url, "live"))
152	            except requests.exceptions.ConnectionError:

--------------------------------------------------
>> Issue: [B113:request_without_timeout] Call to requests without timeout
   Severity: Medium   Confidence: Low
   CWE: CWE-400 (https://cwe.mitre.org/data/definitions/400.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b113_request_without_timeout.html
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/nltk/parse/corenlp.py:162:27
161	            try:
162	                response = requests.get(requests.compat.urljoin(self.url, "ready"))
163	            except requests.exceptions.ConnectionError:

--------------------------------------------------
>> Issue: [B108:hardcoded_tmp_directory] Probable insecure usage of temp file/directory.
   Severity: Medium   Confidence: Medium
   CWE: CWE-377 (https://cwe.mitre.org/data/definitions/377.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b108_hardcoded_tmp_directory.html
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/nltk/parse/featurechart.py:655:45
654	
655	    profile.run("for i in range(1): demo()", "/tmp/profile.out")
656	    import pstats

--------------------------------------------------
>> Issue: [B108:hardcoded_tmp_directory] Probable insecure usage of temp file/directory.
   Severity: Medium   Confidence: Medium
   CWE: CWE-377 (https://cwe.mitre.org/data/definitions/377.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b108_hardcoded_tmp_directory.html
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/nltk/parse/featurechart.py:658:21
657	
658	    p = pstats.Stats("/tmp/profile.out")
659	    p.strip_dirs().sort_stats("time", "cum").print_stats(60)

--------------------------------------------------
>> Issue: [B608:hardcoded_sql_expressions] Possible SQL injection vector through string-based query construction.
   Severity: Medium   Confidence: Medium
   CWE: CWE-89 (https://cwe.mitre.org/data/definitions/89.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b608_hardcoded_sql_expressions.html
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/nltk/sem/chat80.py:435:20
434	    for t in records:
435	        cur.execute("insert into %s values (?,?,?)" % table_name, t)
436	        if verbose:

--------------------------------------------------
>> Issue: [B301:blacklist] Pickle and modules that wrap it can be unsafe when used to deserialize untrusted data, possible security issue.
   Severity: Medium   Confidence: High
   CWE: CWE-502 (https://cwe.mitre.org/data/definitions/502.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b301-pickle
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/nltk/sem/chat80.py:615:13
614	    valuation = make_valuation(concepts, read=True)
615	    db_out = shelve.open(db, "n")
616	

--------------------------------------------------
>> Issue: [B301:blacklist] Pickle and modules that wrap it can be unsafe when used to deserialize untrusted data, possible security issue.
   Severity: Medium   Confidence: High
   CWE: CWE-502 (https://cwe.mitre.org/data/definitions/502.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b301-pickle
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/nltk/sem/chat80.py:635:16
634	    else:
635	        db_in = shelve.open(db)
636	        from nltk.sem import Valuation

--------------------------------------------------
>> Issue: [B102:exec_used] Use of exec detected.
   Severity: Medium   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b102_exec_used.html
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/nltk/sem/util.py:274:8
273	    if options.model:
274	        exec("import %s as model" % options.model)
275	

--------------------------------------------------
>> Issue: [B108:hardcoded_tmp_directory] Probable insecure usage of temp file/directory.
   Severity: Medium   Confidence: Medium
   CWE: CWE-377 (https://cwe.mitre.org/data/definitions/377.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b108_hardcoded_tmp_directory.html
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/nltk/test/unit/test_downloader_unzip.py:116:31
115	
116	        absolute_target = Path("/tmp") / f"nltk_zip_slip_test_{os.getpid()}"
117	

--------------------------------------------------
>> Issue: [B108:hardcoded_tmp_directory] Probable insecure usage of temp file/directory.
   Severity: Medium   Confidence: Medium
   CWE: CWE-377 (https://cwe.mitre.org/data/definitions/377.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b108_hardcoded_tmp_directory.html
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/nltk/test/unit/test_downloader_unzip.py:243:31
242	
243	        absolute_target = Path("/tmp") / f"nltk_multi_viol_test_{os.getpid()}"
244	

--------------------------------------------------
>> Issue: [B108:hardcoded_tmp_directory] Probable insecure usage of temp file/directory.
   Severity: Medium   Confidence: Medium
   CWE: CWE-377 (https://cwe.mitre.org/data/definitions/377.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b108_hardcoded_tmp_directory.html
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/nltk/test/unit/test_verbnet.py:214:32
213	        with pytest.raises(ValueError, match="not supported"):
214	            VerbnetCorpusReader("/tmp", ".*", version="4.0")
215	

--------------------------------------------------
>> Issue: [B108:hardcoded_tmp_directory] Probable insecure usage of temp file/directory.
   Severity: Medium   Confidence: Medium
   CWE: CWE-377 (https://cwe.mitre.org/data/definitions/377.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b108_hardcoded_tmp_directory.html
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/nltk/tokenize/punkt.py:1593:18
1592	        print("writing to /tmp/punkt.new...")
1593	        with open("/tmp/punkt.new", "w") as outfile:
1594	            for aug_tok in tokens:

--------------------------------------------------
>> Issue: [B108:hardcoded_tmp_directory] Probable insecure usage of temp file/directory.
   Severity: Medium   Confidence: Medium
   CWE: CWE-377 (https://cwe.mitre.org/data/definitions/377.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b108_hardcoded_tmp_directory.html
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/nltk/tokenize/punkt.py:1756:46
1755	    def save_params(self):
1756	        save_punkt_params(self._params, dir=f"/tmp/{self._lang}")
1757	

--------------------------------------------------
>> Issue: [B108:hardcoded_tmp_directory] Probable insecure usage of temp file/directory.
   Severity: Medium   Confidence: Medium
   CWE: CWE-377 (https://cwe.mitre.org/data/definitions/377.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b108_hardcoded_tmp_directory.html
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/nltk/tokenize/punkt.py:1779:34
1778	
1779	def save_punkt_params(params, dir="/tmp/punkt_tab"):
1780	    from os import mkdir

--------------------------------------------------
>> Issue: [B307:blacklist] Use of possibly insecure function - consider using safer ast.literal_eval.
   Severity: Medium   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b307-eval
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/nltk/tokenize/texttiling.py:531:12
530	    else:
531	        w = eval("numpy." + window + "(window_len)")
532	

--------------------------------------------------
>> Issue: [B301:blacklist] Pickle and modules that wrap it can be unsafe when used to deserialize untrusted data, possible security issue.
   Severity: Medium   Confidence: High
   CWE: CWE-502 (https://cwe.mitre.org/data/definitions/502.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b301-pickle
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/pydantic/deprecated/parse.py:54:15
53	        bb = b if isinstance(b, bytes) else b.encode()  # type: ignore
54	        return pickle.loads(bb)
55	    else:

--------------------------------------------------
>> Issue: [B301:blacklist] Pickle and modules that wrap it can be unsafe when used to deserialize untrusted data, possible security issue.
   Severity: Medium   Confidence: High
   CWE: CWE-502 (https://cwe.mitre.org/data/definitions/502.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b301-pickle
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/pydantic/v1/parse.py:42:15
41	        bb = b if isinstance(b, bytes) else b.encode()
42	        return pickle.loads(bb)
43	    else:

--------------------------------------------------
>> Issue: [B307:blacklist] Use of possibly insecure function - consider using safer ast.literal_eval.
   Severity: Medium   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b307-eval
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/pydantic/v1/utils.py:195:8
194	    try:
195	        eval('__IPYTHON__')
196	    except NameError:

--------------------------------------------------
>> Issue: [B102:exec_used] Use of exec detected.
   Severity: Medium   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b102_exec_used.html
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/pygments/formatters/__init__.py:103:12
102	        with open(filename, 'rb') as f:
103	            exec(f.read(), custom_namespace)
104	        # Retrieve the class `formattername` from that namespace

--------------------------------------------------
>> Issue: [B102:exec_used] Use of exec detected.
   Severity: Medium   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b102_exec_used.html
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/pygments/lexers/__init__.py:154:12
153	        with open(filename, 'rb') as f:
154	            exec(f.read(), custom_namespace)
155	        # Retrieve the class `lexername` from that namespace

--------------------------------------------------
>> Issue: [B310:blacklist] Audit url open for permitted schemes. Allowing use of file:/ or custom schemes is often unexpected.
   Severity: Medium   Confidence: High
   CWE: CWE-22 (https://cwe.mitre.org/data/definitions/22.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b310-urllib-urlopen
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/pygments/lexers/_lua_builtins.py:225:12
224	    def get_newest_version():
225	        f = urlopen('http://www.lua.org/manual/')
226	        r = re.compile(r'^<A HREF="(\d\.\d)/">(Lua )?\1</A>')

--------------------------------------------------
>> Issue: [B310:blacklist] Audit url open for permitted schemes. Allowing use of file:/ or custom schemes is often unexpected.
   Severity: Medium   Confidence: High
   CWE: CWE-22 (https://cwe.mitre.org/data/definitions/22.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b310-urllib-urlopen
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/pygments/lexers/_lua_builtins.py:233:12
232	    def get_lua_functions(version):
233	        f = urlopen(f'http://www.lua.org/manual/{version}/')
234	        r = re.compile(r'^<A HREF="manual.html#pdf-(?!lua|LUA)([^:]+)">\1</A>')

--------------------------------------------------
>> Issue: [B310:blacklist] Audit url open for permitted schemes. Allowing use of file:/ or custom schemes is often unexpected.
   Severity: Medium   Confidence: High
   CWE: CWE-22 (https://cwe.mitre.org/data/definitions/22.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b310-urllib-urlopen
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/pygments/lexers/_mysql_builtins.py:1297:19
1296	        # Pull content from lex.h.
1297	        lex_file = urlopen(LEX_URL).read().decode('utf8', errors='ignore')
1298	        keywords = parse_lex_keywords(lex_file)

--------------------------------------------------
>> Issue: [B310:blacklist] Audit url open for permitted schemes. Allowing use of file:/ or custom schemes is often unexpected.
   Severity: Medium   Confidence: High
   CWE: CWE-22 (https://cwe.mitre.org/data/definitions/22.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b310-urllib-urlopen
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/pygments/lexers/_mysql_builtins.py:1303:27
1302	        # Parse content in item_create.cc.
1303	        item_create_file = urlopen(ITEM_CREATE_URL).read().decode('utf8', errors='ignore')
1304	        functions.update(parse_item_create_functions(item_create_file))

--------------------------------------------------
>> Issue: [B310:blacklist] Audit url open for permitted schemes. Allowing use of file:/ or custom schemes is often unexpected.
   Severity: Medium   Confidence: High
   CWE: CWE-22 (https://cwe.mitre.org/data/definitions/22.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b310-urllib-urlopen
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/pygments/lexers/_php_builtins.py:3299:19
3298	    def get_php_references():
3299	        download = urlretrieve(PHP_MANUAL_URL)
3300	        with tarfile.open(download[0]) as tar:

--------------------------------------------------
>> Issue: [B202:tarfile_unsafe_members] tarfile.extractall used without any validation. Please check and discard dangerous members.
   Severity: High   Confidence: High
   CWE: CWE-22 (https://cwe.mitre.org/data/definitions/22.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b202_tarfile_unsafe_members.html
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/pygments/lexers/_php_builtins.py:3304:16
3303	            else:
3304	                tar.extractall()
3305	        yield from glob.glob(f"{PHP_MANUAL_DIR}{PHP_REFERENCE_GLOB}")

--------------------------------------------------
>> Issue: [B310:blacklist] Audit url open for permitted schemes. Allowing use of file:/ or custom schemes is often unexpected.
   Severity: Medium   Confidence: High
   CWE: CWE-22 (https://cwe.mitre.org/data/definitions/22.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b310-urllib-urlopen
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/pygments/lexers/_postgres_builtins.py:642:18
641	    def update_myself():
642	        content = urlopen(DATATYPES_URL).read().decode('utf-8', errors='ignore')
643	        data_file = list(content.splitlines())

--------------------------------------------------
>> Issue: [B310:blacklist] Audit url open for permitted schemes. Allowing use of file:/ or custom schemes is often unexpected.
   Severity: Medium   Confidence: High
   CWE: CWE-22 (https://cwe.mitre.org/data/definitions/22.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b310-urllib-urlopen
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/pygments/lexers/_postgres_builtins.py:647:18
646	
647	        content = urlopen(KEYWORDS_URL).read().decode('utf-8', errors='ignore')
648	        keywords = parse_keywords(content)

--------------------------------------------------
>> Issue: [B301:blacklist] Pickle and modules that wrap it can be unsafe when used to deserialize untrusted data, possible security issue.
   Severity: Medium   Confidence: High
   CWE: CWE-502 (https://cwe.mitre.org/data/definitions/502.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b301-pickle
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/regex/tests/test_regex.py:3775:12
3774	        p = pickle.dumps(r)
3775	        r = pickle.loads(p)
3776	        self.assertEqual(r.match('foo').span(), (0, 3))

--------------------------------------------------
>> Issue: [B301:blacklist] Pickle and modules that wrap it can be unsafe when used to deserialize untrusted data, possible security issue.
   Severity: Medium   Confidence: High
   CWE: CWE-502 (https://cwe.mitre.org/data/definitions/502.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b301-pickle
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/rich/style.py:475:66
474	        """Get meta information (can not be changed after construction)."""
475	        return {} if self._meta is None else cast(Dict[str, Any], loads(self._meta))
476	

--------------------------------------------------
>> Issue: [B108:hardcoded_tmp_directory] Probable insecure usage of temp file/directory.
   Severity: Medium   Confidence: Medium
   CWE: CWE-377 (https://cwe.mitre.org/data/definitions/377.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b108_hardcoded_tmp_directory.html
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/ruamel/yaml/compat.py:151:17
150	nprint = Nprint()
151	nprintf = Nprint('/var/tmp/ruamel.yaml.log')
152	

--------------------------------------------------
>> Issue: [B701:jinja2_autoescape_false] By default, jinja2 sets autoescape to False. Consider using autoescape=True or use the select_autoescape function to mitigate XSS vulnerabilities.
   Severity: High   Confidence: High
   CWE: CWE-94 (https://cwe.mitre.org/data/definitions/94.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b701_jinja2_autoescape_false.html
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/safety/alerts/utils.py:154:10
153	    p = Path(__file__).parent / "templates"
154	    env = jinja2.Environment(loader=jinja2.FileSystemLoader(Path(p)))  # type: ignore
155	    template = env.get_template("pr.jinja2")

--------------------------------------------------
>> Issue: [B701:jinja2_autoescape_false] By default, jinja2 sets autoescape to False. Consider using autoescape=True or use the select_autoescape function to mitigate XSS vulnerabilities.
   Severity: High   Confidence: High
   CWE: CWE-94 (https://cwe.mitre.org/data/definitions/94.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b701_jinja2_autoescape_false.html
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/safety/alerts/utils.py:204:10
203	    p = Path(__file__).parent / "templates"
204	    env = jinja2.Environment(loader=jinja2.FileSystemLoader(Path(p)))  # type: ignore
205	    template = env.get_template("issue.jinja2")

--------------------------------------------------
>> Issue: [B324:hashlib] Use of weak SHA1 hash for security. Consider usedforsecurity=False
   Severity: High   Confidence: High
   CWE: CWE-327 (https://cwe.mitre.org/data/definitions/327.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b324_hashlib.html
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/safety/alerts/utils.py:262:11
261	    """
262	    return hashlib.sha1(
263	        b"blob " + str(len(raw_contents)).encode("ascii") + b"\0" + raw_contents
264	    ).hexdigest()
265	

--------------------------------------------------
>> Issue: [B701:jinja2_autoescape_false] By default, jinja2 sets autoescape to False. Consider using autoescape=True or use the select_autoescape function to mitigate XSS vulnerabilities.
   Severity: High   Confidence: High
   CWE: CWE-94 (https://cwe.mitre.org/data/definitions/94.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b701_jinja2_autoescape_false.html
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/safety/output_utils.py:1655:10
1654	    file_loader = PackageLoader("safety", "templates")
1655	    env = Environment(loader=file_loader)
1656	    tmpl = env.get_template(template)

--------------------------------------------------
>> Issue: [B307:blacklist] Use of possibly insecure function - consider using safer ast.literal_eval.
   Severity: Medium   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b307-eval
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/tqdm/cli.py:38:19
37	        if re.match(r"^\\\w+$", val):
38	            return eval(f'"{val}"').encode()
39	        raise TqdmTypeError(f"{val} : {typ}")

--------------------------------------------------
>> Issue: [B604:any_other_function_with_shell_equals_true] Function call with shell=True parameter identified, possible security issue.
   Severity: Medium   Confidence: Low
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b604_any_other_function_with_shell_equals_true.html
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/typer/_completion_shared.py:113:21
112	    script_content = get_completion_script(
113	        prog_name=prog_name, complete_var=complete_var, shell=shell
114	    )
115	    completion_path.write_text(script_content)
116	    return completion_path

--------------------------------------------------
>> Issue: [B604:any_other_function_with_shell_equals_true] Function call with shell=True parameter identified, possible security issue.
   Severity: Medium   Confidence: Low
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b604_any_other_function_with_shell_equals_true.html
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/typer/_completion_shared.py:141:21
140	    script_content = get_completion_script(
141	        prog_name=prog_name, complete_var=complete_var, shell=shell
142	    )
143	    path_obj.write_text(script_content)
144	    return path_obj

--------------------------------------------------
>> Issue: [B604:any_other_function_with_shell_equals_true] Function call with shell=True parameter identified, possible security issue.
   Severity: Medium   Confidence: Low
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b604_any_other_function_with_shell_equals_true.html
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/typer/_completion_shared.py:152:21
151	    script_content = get_completion_script(
152	        prog_name=prog_name, complete_var=complete_var, shell=shell
153	    )
154	    path_obj.write_text(f"{script_content}\n")
155	    return path_obj

--------------------------------------------------
>> Issue: [B604:any_other_function_with_shell_equals_true] Function call with shell=True parameter identified, possible security issue.
   Severity: Medium   Confidence: Low
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b604_any_other_function_with_shell_equals_true.html
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/typer/_completion_shared.py:194:21
193	    script_content = get_completion_script(
194	        prog_name=prog_name, complete_var=complete_var, shell=shell
195	    )
196	    with path_obj.open(mode="a") as f:
197	        f.write(f"{script_content}\n")

--------------------------------------------------
>> Issue: [B604:any_other_function_with_shell_equals_true] Function call with shell=True parameter identified, possible security issue.
   Severity: Medium   Confidence: Low
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b604_any_other_function_with_shell_equals_true.html
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/typer/_completion_shared.py:215:25
214	        installed_path = install_bash(
215	            prog_name=prog_name, complete_var=complete_var, shell=shell
216	        )
217	        return shell, installed_path
218	    elif shell == "zsh":

--------------------------------------------------
>> Issue: [B604:any_other_function_with_shell_equals_true] Function call with shell=True parameter identified, possible security issue.
   Severity: Medium   Confidence: Low
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b604_any_other_function_with_shell_equals_true.html
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/typer/_completion_shared.py:220:25
219	        installed_path = install_zsh(
220	            prog_name=prog_name, complete_var=complete_var, shell=shell
221	        )
222	        return shell, installed_path
223	    elif shell == "fish":

--------------------------------------------------
>> Issue: [B604:any_other_function_with_shell_equals_true] Function call with shell=True parameter identified, possible security issue.
   Severity: Medium   Confidence: Low
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b604_any_other_function_with_shell_equals_true.html
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/typer/_completion_shared.py:225:25
224	        installed_path = install_fish(
225	            prog_name=prog_name, complete_var=complete_var, shell=shell
226	        )
227	        return shell, installed_path
228	    elif shell in {"powershell", "pwsh"}:

--------------------------------------------------
>> Issue: [B604:any_other_function_with_shell_equals_true] Function call with shell=True parameter identified, possible security issue.
   Severity: Medium   Confidence: Low
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b604_any_other_function_with_shell_equals_true.html
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/typer/_completion_shared.py:230:25
229	        installed_path = install_powershell(
230	            prog_name=prog_name, complete_var=complete_var, shell=shell
231	        )
232	        return shell, installed_path
233	    else:

--------------------------------------------------
>> Issue: [B604:any_other_function_with_shell_equals_true] Function call with shell=True parameter identified, possible security issue.
   Severity: Medium   Confidence: Low
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b604_any_other_function_with_shell_equals_true.html
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/typer/completion.py:34:22
33	    if isinstance(value, str):
34	        shell, path = install(shell=value)
35	    else:

--------------------------------------------------
>> Issue: [B604:any_other_function_with_shell_equals_true] Function call with shell=True parameter identified, possible security issue.
   Severity: Medium   Confidence: Low
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b604_any_other_function_with_shell_equals_true.html
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/typer/completion.py:57:21
56	    script_content = get_completion_script(
57	        prog_name=prog_name, complete_var=complete_var, shell=shell
58	    )
59	    click.echo(script_content)
60	    sys.exit(0)

--------------------------------------------------
>> Issue: [B307:blacklist] Use of possibly insecure function - consider using safer ast.literal_eval.
   Severity: Medium   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b307-eval
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/typing_extensions.py:4034:53
4033	        return_value = {key:
4034	            value if not isinstance(value, str) else eval(value, globals, locals)
4035	            for key, value in ann.items() }

--------------------------------------------------
>> Issue: [B307:blacklist] Use of possibly insecure function - consider using safer ast.literal_eval.
   Severity: Medium   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b307-eval
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/typing_extensions.py:4116:20
4115	            code = forward_ref.__forward_code__
4116	            value = eval(code, globals, locals)
4117	        forward_ref.__forward_evaluated__ = True

--------------------------------------------------
>> Issue: [B102:exec_used] Use of exec detected.
   Severity: Medium   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b102_exec_used.html
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/typing_inspection/typing_objects.py:101:4
100	    globals_: dict[str, Any] = {'Any': Any, 'typing': typing, 'typing_extensions': typing_extensions}
101	    exec(func_code, globals_, locals_)
102	    return locals_[function_name]

--------------------------------------------------
>> Issue: [B102:exec_used] Use of exec detected.
   Severity: Medium   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b102_exec_used.html
   Location: ./.audit-tools/pipx/venvs/safety/lib/python3.12/site-packages/typing_inspection/typing_objects.py:133:4
132	    globals_: dict[str, Any] = {'Any': Any, 'typing': typing, 'typing_extensions': typing_extensions}
133	    exec(func_code, globals_, locals_)
134	    return locals_[function_name]

--------------------------------------------------
>> Issue: [B604:any_other_function_with_shell_equals_true] Function call with shell=True parameter identified, possible security issue.
   Severity: Medium   Confidence: Low
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b604_any_other_function_with_shell_equals_true.html
   Location: ./.audit-tools/pipx/venvs/semgrep/lib/python3.12/site-packages/anyio/_backends/_trio.py:1103:28
1102	                stderr=stderr,
1103	                shell=True,
1104	                **kwargs,
1105	            )
1106	        else:
1107	            process = await trio.lowlevel.open_process(
1108	                [convert_item(item) for item in command],
1109	                stdin=stdin,
1110	                stdout=stdout,
1111	                stderr=stderr,

--------------------------------------------------
>> Issue: [B104:hardcoded_bind_all_interfaces] Possible binding to all interfaces.
   Severity: Medium   Confidence: Medium
   CWE: CWE-605 (https://cwe.mitre.org/data/definitions/605.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b104_hardcoded_bind_all_interfaces.html
   Location: ./.audit-tools/pipx/venvs/semgrep/lib/python3.12/site-packages/anyio/_core/_sockets.py:490:25
489	    else:
490	        local_address = ("0.0.0.0", 0)
491	

--------------------------------------------------
>> Issue: [B610:django_extra_used] Use of extra potential SQL attack vector.
   Severity: Medium   Confidence: Medium
   CWE: CWE-89 (https://cwe.mitre.org/data/definitions/89.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b610_django_extra_used.html
   Location: ./.audit-tools/pipx/venvs/semgrep/lib/python3.12/site-packages/anyio/streams/tls.py:249:22
248	    async def send_eof(self) -> None:
249	        tls_version = self.extra(TLSAttribute.tls_version)
250	        match = re.match(r"TLSv(\d+)(?:\.(\d+))?", tls_version)

--------------------------------------------------
>> Issue: [B301:blacklist] Pickle and modules that wrap it can be unsafe when used to deserialize untrusted data, possible security issue.
   Severity: Medium   Confidence: High
   CWE: CWE-502 (https://cwe.mitre.org/data/definitions/502.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b301-pickle
   Location: ./.audit-tools/pipx/venvs/semgrep/lib/python3.12/site-packages/anyio/to_interpreter.py:130:22
129	            if fmt == FMT_PICKLED:
130	                res = pickle.loads(res)
131	

--------------------------------------------------
>> Issue: [B301:blacklist] Pickle and modules that wrap it can be unsafe when used to deserialize untrusted data, possible security issue.
   Severity: Medium   Confidence: High
   CWE: CWE-502 (https://cwe.mitre.org/data/definitions/502.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b301-pickle
   Location: ./.audit-tools/pipx/venvs/semgrep/lib/python3.12/site-packages/anyio/to_process.py:94:17
93	
94	        retval = pickle.loads(pickled_response)
95	        if status == b"EXCEPTION":

--------------------------------------------------
>> Issue: [B301:blacklist] Pickle and modules that wrap it can be unsafe when used to deserialize untrusted data, possible security issue.
   Severity: Medium   Confidence: High
   CWE: CWE-502 (https://cwe.mitre.org/data/definitions/502.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b301-pickle
   Location: ./.audit-tools/pipx/venvs/semgrep/lib/python3.12/site-packages/anyio/to_process.py:218:29
217	        try:
218	            command, *args = pickle.load(stdin.buffer)
219	        except EOFError:

--------------------------------------------------
>> Issue: [B307:blacklist] Use of possibly insecure function - consider using safer ast.literal_eval.
   Severity: Medium   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b307-eval
   Location: ./.audit-tools/pipx/venvs/semgrep/lib/python3.12/site-packages/attr/_make.py:227:4
226	    bytecode = compile(script, filename, "exec")
227	    eval(bytecode, globs, locs)
228	

--------------------------------------------------
>> Issue: [B108:hardcoded_tmp_directory] Probable insecure usage of temp file/directory.
   Severity: Medium   Confidence: Medium
   CWE: CWE-377 (https://cwe.mitre.org/data/definitions/377.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b108_hardcoded_tmp_directory.html
   Location: ./.audit-tools/pipx/venvs/semgrep/lib/python3.12/site-packages/boltons/fileutils.py:703:21
702	if __name__ == '__main__':
703	    with atomic_save('/tmp/final.txt') as f:
704	        f.write('rofl')

--------------------------------------------------
>> Issue: [B102:exec_used] Use of exec detected.
   Severity: Medium   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b102_exec_used.html
   Location: ./.audit-tools/pipx/venvs/semgrep/lib/python3.12/site-packages/boltons/funcutils.py:1035:12
1034	            code = compile(src, filename, 'single')
1035	            exec(code, execdict)
1036	        except Exception:

--------------------------------------------------
>> Issue: [B102:exec_used] Use of exec detected.
   Severity: Medium   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b102_exec_used.html
   Location: ./.audit-tools/pipx/venvs/semgrep/lib/python3.12/site-packages/boltons/namedutils.py:64:8
63	    def exec_(code, global_env):
64	        exec("exec code in global_env")
65	except NameError:

--------------------------------------------------
>> Issue: [B102:exec_used] Use of exec detected.
   Severity: Medium   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b102_exec_used.html
   Location: ./.audit-tools/pipx/venvs/semgrep/lib/python3.12/site-packages/boltons/namedutils.py:68:8
67	    def exec_(code, global_env):
68	        exec(code, global_env)
69	

--------------------------------------------------
>> Issue: [B307:blacklist] Use of possibly insecure function - consider using safer ast.literal_eval.
   Severity: Medium   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b307-eval
   Location: ./.audit-tools/pipx/venvs/semgrep/lib/python3.12/site-packages/cffi/recompiler.py:78:16
77	    def as_python_expr(self):
78	        flags = eval(self.flags, G_FLAGS)
79	        fields_expr = [c_field.as_field_python_expr()

--------------------------------------------------
>> Issue: [B102:exec_used] Use of exec detected.
   Severity: Medium   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b102_exec_used.html
   Location: ./.audit-tools/pipx/venvs/semgrep/lib/python3.12/site-packages/cffi/setuptools_ext.py:26:4
25	    code = compile(src, filename, 'exec')
26	    exec(code, glob, glob)
27	

--------------------------------------------------
>> Issue: [B602:subprocess_popen_with_shell_equals_true] subprocess call with shell=True identified, security issue.
   Severity: High   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b602_subprocess_popen_with_shell_equals_true.html
   Location: ./.audit-tools/pipx/venvs/semgrep/lib/python3.12/site-packages/click/_termui_impl.py:429:8
428	        [cmd_absolute],
429	        shell=True,
430	        stdin=subprocess.PIPE,
431	        env=env,
432	        errors="replace",
433	        text=True,
434	    )
435	    assert c.stdin is not None
436	    try:
437	        for text in generator:

--------------------------------------------------
>> Issue: [B602:subprocess_popen_with_shell_equals_true] subprocess call with shell=True identified, security issue.
   Severity: High   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b602_subprocess_popen_with_shell_equals_true.html
   Location: ./.audit-tools/pipx/venvs/semgrep/lib/python3.12/site-packages/click/_termui_impl.py:552:16
551	        try:
552	            c = subprocess.Popen(f'{editor} "{filename}"', env=environ, shell=True)
553	            exit_code = c.wait()

--------------------------------------------------
>> Issue: [B303:blacklist] Use of insecure MD2, MD4, MD5, or SHA1 hash function.
   Severity: Medium   Confidence: High
   CWE: CWE-327 (https://cwe.mitre.org/data/definitions/327.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b303-md5
   Location: ./.audit-tools/pipx/venvs/semgrep/lib/python3.12/site-packages/cryptography/hazmat/_oid.py:128:40
127	_SIG_OIDS_TO_HASH: dict[ObjectIdentifier, hashes.HashAlgorithm | None] = {
128	    SignatureAlgorithmOID.RSA_WITH_MD5: hashes.MD5(),
129	    SignatureAlgorithmOID.RSA_WITH_SHA1: hashes.SHA1(),

--------------------------------------------------
>> Issue: [B303:blacklist] Use of insecure MD2, MD4, MD5, or SHA1 hash function.
   Severity: Medium   Confidence: High
   CWE: CWE-327 (https://cwe.mitre.org/data/definitions/327.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b303-md5
   Location: ./.audit-tools/pipx/venvs/semgrep/lib/python3.12/site-packages/cryptography/hazmat/_oid.py:129:41
128	    SignatureAlgorithmOID.RSA_WITH_MD5: hashes.MD5(),
129	    SignatureAlgorithmOID.RSA_WITH_SHA1: hashes.SHA1(),
130	    SignatureAlgorithmOID._RSA_WITH_SHA1: hashes.SHA1(),

--------------------------------------------------
>> Issue: [B303:blacklist] Use of insecure MD2, MD4, MD5, or SHA1 hash function.
   Severity: Medium   Confidence: High
   CWE: CWE-327 (https://cwe.mitre.org/data/definitions/327.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b303-md5
   Location: ./.audit-tools/pipx/venvs/semgrep/lib/python3.12/site-packages/cryptography/hazmat/_oid.py:130:42
129	    SignatureAlgorithmOID.RSA_WITH_SHA1: hashes.SHA1(),
130	    SignatureAlgorithmOID._RSA_WITH_SHA1: hashes.SHA1(),
131	    SignatureAlgorithmOID.RSA_WITH_SHA224: hashes.SHA224(),

--------------------------------------------------
>> Issue: [B303:blacklist] Use of insecure MD2, MD4, MD5, or SHA1 hash function.
   Severity: Medium   Confidence: High
   CWE: CWE-327 (https://cwe.mitre.org/data/definitions/327.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b303-md5
   Location: ./.audit-tools/pipx/venvs/semgrep/lib/python3.12/site-packages/cryptography/hazmat/_oid.py:139:43
138	    SignatureAlgorithmOID.RSA_WITH_SHA3_512: hashes.SHA3_512(),
139	    SignatureAlgorithmOID.ECDSA_WITH_SHA1: hashes.SHA1(),
140	    SignatureAlgorithmOID.ECDSA_WITH_SHA224: hashes.SHA224(),

--------------------------------------------------
>> Issue: [B303:blacklist] Use of insecure MD2, MD4, MD5, or SHA1 hash function.
   Severity: Medium   Confidence: High
   CWE: CWE-327 (https://cwe.mitre.org/data/definitions/327.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b303-md5
   Location: ./.audit-tools/pipx/venvs/semgrep/lib/python3.12/site-packages/cryptography/hazmat/_oid.py:148:41
147	    SignatureAlgorithmOID.ECDSA_WITH_SHA3_512: hashes.SHA3_512(),
148	    SignatureAlgorithmOID.DSA_WITH_SHA1: hashes.SHA1(),
149	    SignatureAlgorithmOID.DSA_WITH_SHA224: hashes.SHA224(),

--------------------------------------------------
>> Issue: [B305:blacklist] Use of insecure cipher mode cryptography.hazmat.primitives.ciphers.modes.ECB.
   Severity: Medium   Confidence: High
   CWE: CWE-327 (https://cwe.mitre.org/data/definitions/327.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b304-b305-ciphers-and-modes
   Location: ./.audit-tools/pipx/venvs/semgrep/lib/python3.12/site-packages/cryptography/hazmat/primitives/keywrap.py:21:42
20	    # RFC 3394 Key Wrap - 2.2.1 (index method)
21	    encryptor = Cipher(AES(wrapping_key), ECB()).encryptor()
22	    n = len(r)

--------------------------------------------------
>> Issue: [B305:blacklist] Use of insecure cipher mode cryptography.hazmat.primitives.ciphers.modes.ECB.
   Severity: Medium   Confidence: High
   CWE: CWE-327 (https://cwe.mitre.org/data/definitions/327.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b304-b305-ciphers-and-modes
   Location: ./.audit-tools/pipx/venvs/semgrep/lib/python3.12/site-packages/cryptography/hazmat/primitives/keywrap.py:64:42
63	    # Implement RFC 3394 Key Unwrap - 2.2.2 (index method)
64	    decryptor = Cipher(AES(wrapping_key), ECB()).decryptor()
65	    n = len(r)

--------------------------------------------------
>> Issue: [B305:blacklist] Use of insecure cipher mode cryptography.hazmat.primitives.ciphers.modes.ECB.
   Severity: Medium   Confidence: High
   CWE: CWE-327 (https://cwe.mitre.org/data/definitions/327.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b304-b305-ciphers-and-modes
   Location: ./.audit-tools/pipx/venvs/semgrep/lib/python3.12/site-packages/cryptography/hazmat/primitives/keywrap.py:100:46
99	        # RFC 5649 - 4.1 - exactly 8 octets after padding
100	        encryptor = Cipher(AES(wrapping_key), ECB()).encryptor()
101	        b = encryptor.update(aiv + key_to_wrap)

--------------------------------------------------
>> Issue: [B305:blacklist] Use of insecure cipher mode cryptography.hazmat.primitives.ciphers.modes.ECB.
   Severity: Medium   Confidence: High
   CWE: CWE-327 (https://cwe.mitre.org/data/definitions/327.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b304-b305-ciphers-and-modes
   Location: ./.audit-tools/pipx/venvs/semgrep/lib/python3.12/site-packages/cryptography/hazmat/primitives/keywrap.py:122:46
121	        # RFC 5649 - 4.2 - exactly two 64-bit blocks
122	        decryptor = Cipher(AES(wrapping_key), ECB()).decryptor()
123	        out = decryptor.update(wrapped_key)

--------------------------------------------------
>> Issue: [B303:blacklist] Use of insecure MD2, MD4, MD5, or SHA1 hash function.
   Severity: Medium   Confidence: High
   CWE: CWE-327 (https://cwe.mitre.org/data/definitions/327.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b303-md5
   Location: ./.audit-tools/pipx/venvs/semgrep/lib/python3.12/site-packages/cryptography/hazmat/primitives/serialization/ssh.py:1009:27
1008	            if self._inner_sig_type == _SSH_RSA:
1009	                hash_alg = hashes.SHA1()
1010	            elif self._inner_sig_type == _SSH_RSA_SHA256:

--------------------------------------------------
>> Issue: [B324:hashlib] Use of weak SHA1 hash for security. Consider usedforsecurity=False
   Severity: High   Confidence: High
   CWE: CWE-327 (https://cwe.mitre.org/data/definitions/327.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b324_hashlib.html
   Location: ./.audit-tools/pipx/venvs/semgrep/lib/python3.12/site-packages/cryptography/x509/extensions.py:72:11
71	
72	    return hashlib.sha1(data).digest()
73	

--------------------------------------------------
>> Issue: [B324:hashlib] Use of weak SHA1 hash for security. Consider usedforsecurity=False
   Severity: High   Confidence: High
   CWE: CWE-327 (https://cwe.mitre.org/data/definitions/327.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b324_hashlib.html
   Location: ./.audit-tools/pipx/venvs/semgrep/lib/python3.12/site-packages/face/sinter.py:136:16
135	    env = {} if env is None else env
136	    code_hash = hashlib.sha1(code_str.encode('utf8')).hexdigest()[:16]
137	    unique_filename = f"<sinter generated {name} {code_hash}>"

--------------------------------------------------
>> Issue: [B102:exec_used] Use of exec detected.
   Severity: Medium   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b102_exec_used.html
   Location: ./.audit-tools/pipx/venvs/semgrep/lib/python3.12/site-packages/face/sinter.py:142:4
141	
142	    exec(code, env)
143	

--------------------------------------------------
>> Issue: [B102:exec_used] Use of exec detected.
   Severity: Medium   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b102_exec_used.html
   Location: ./.audit-tools/pipx/venvs/semgrep/lib/python3.12/site-packages/glom/cli.py:239:4
238	        env = {}
239	    exec(code, env)
240	

--------------------------------------------------
>> Issue: [B307:blacklist] Use of possibly insecure function - consider using safer ast.literal_eval.
   Severity: Medium   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b307-eval
   Location: ./.audit-tools/pipx/venvs/semgrep/lib/python3.12/site-packages/glom/test/test_basic.py:250:16
249	        ).star(args='args2', kwargs='kwargs')
250	    assert repr(eval(repr(repr_spec), locals(), globals())) == repr(repr_spec)
251	

--------------------------------------------------
>> Issue: [B314:blacklist] Using xml.etree.ElementTree.fromstring to parse untrusted XML data is known to be vulnerable to XML attacks. Replace xml.etree.ElementTree.fromstring with its defusedxml equivalent function or make sure defusedxml.defuse_stdlib() is called
   Severity: Medium   Confidence: High
   CWE: CWE-20 (https://cwe.mitre.org/data/definitions/20.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b313-b320-xml-bad-elementtree
   Location: ./.audit-tools/pipx/venvs/semgrep/lib/python3.12/site-packages/glom/test/test_basic.py:413:12
412	    etree2tuples = Fill(Ref('ElementTree', (T.tag, (Iter(Ref('ElementTree')), list) )))
413	    etree = ElementTree.fromstring('''
414	    <html>
415	      <head>
416	        <title>the title</title>
417	      </head>
418	      <body id="the-body">
419	        <p>A paragraph</p>
420	      </body>
421	    </html>''')
422	    glom(etree, etree2dicts)

--------------------------------------------------
>> Issue: [B307:blacklist] Use of possibly insecure function - consider using safer ast.literal_eval.
   Severity: Medium   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b307-eval
   Location: ./.audit-tools/pipx/venvs/semgrep/lib/python3.12/site-packages/glom/test/test_match.py:237:16
236	    assert repr(And(M == 1, float)) == "(M == 1) & float"
237	    assert repr(eval(repr(And(M == 1, float)))) == "(M == 1) & float"
238	

--------------------------------------------------
>> Issue: [B307:blacklist] Use of possibly insecure function - consider using safer ast.literal_eval.
   Severity: Medium   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b307-eval
   Location: ./.audit-tools/pipx/venvs/semgrep/lib/python3.12/site-packages/glom/test/test_mutation.py:36:37
35	    assert repr(assign_spec) == "Assign(T.a, 1, missing=dict)"
36	    assert repr(assign_spec) == repr(eval(repr(assign_spec)))
37	

--------------------------------------------------
>> Issue: [B301:blacklist] Pickle and modules that wrap it can be unsafe when used to deserialize untrusted data, possible security issue.
   Severity: Medium   Confidence: High
   CWE: CWE-502 (https://cwe.mitre.org/data/definitions/502.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b301-pickle
   Location: ./.audit-tools/pipx/venvs/semgrep/lib/python3.12/site-packages/glom/test/test_path_and_t.py:97:14
96	
97	    rt_spec = pickle.loads(pickle.dumps(spec))
98	    assert repr(spec) == repr(rt_spec)

--------------------------------------------------
>> Issue: [B301:blacklist] Pickle and modules that wrap it can be unsafe when used to deserialize untrusted data, possible security issue.
   Severity: Medium   Confidence: High
   CWE: CWE-502 (https://cwe.mitre.org/data/definitions/502.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b301-pickle
   Location: ./.audit-tools/pipx/venvs/semgrep/lib/python3.12/site-packages/glom/test/test_path_and_t.py:103:32
102	    s_spec = S.attribute
103	    assert repr(s_spec) == repr(pickle.loads(pickle.dumps(s_spec)))
104	

--------------------------------------------------
>> Issue: [B307:blacklist] Use of possibly insecure function - consider using safer ast.literal_eval.
   Severity: Medium   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b307-eval
   Location: ./.audit-tools/pipx/venvs/semgrep/lib/python3.12/site-packages/glom/test/test_snippets.py:58:4
57	        return  # maybe in the future
58	    eval(code, SNIPPETS_GLOBALS)
59	

--------------------------------------------------
>> Issue: [B324:hashlib] Use of weak SHA1 hash for security. Consider usedforsecurity=False
   Severity: High   Confidence: High
   CWE: CWE-327 (https://cwe.mitre.org/data/definitions/327.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b324_hashlib.html
   Location: ./.audit-tools/pipx/venvs/semgrep/lib/python3.12/site-packages/google/protobuf/proto_builder.py:68:16
67	  # proto files.
68	  fields_hash = hashlib.sha1()
69	  for f_name, f_type in field_items:

--------------------------------------------------
>> Issue: [B610:django_extra_used] Use of extra potential SQL attack vector.
   Severity: Medium   Confidence: Medium
   CWE: CWE-89 (https://cwe.mitre.org/data/definitions/89.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b610_django_extra_used.html
   Location: ./.audit-tools/pipx/venvs/semgrep/lib/python3.12/site-packages/httpcore/_backends/anyio.py:84:19
83	        if info == "ssl_object":
84	            return self._stream.extra(anyio.streams.tls.TLSAttribute.ssl_object, None)
85	        if info == "client_addr":

--------------------------------------------------
>> Issue: [B610:django_extra_used] Use of extra potential SQL attack vector.
   Severity: Medium   Confidence: Medium
   CWE: CWE-89 (https://cwe.mitre.org/data/definitions/89.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b610_django_extra_used.html
   Location: ./.audit-tools/pipx/venvs/semgrep/lib/python3.12/site-packages/httpcore/_backends/anyio.py:86:19
85	        if info == "client_addr":
86	            return self._stream.extra(anyio.abc.SocketAttribute.local_address, None)
87	        if info == "server_addr":

--------------------------------------------------
>> Issue: [B610:django_extra_used] Use of extra potential SQL attack vector.
   Severity: Medium   Confidence: Medium
   CWE: CWE-89 (https://cwe.mitre.org/data/definitions/89.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b610_django_extra_used.html
   Location: ./.audit-tools/pipx/venvs/semgrep/lib/python3.12/site-packages/httpcore/_backends/anyio.py:88:19
87	        if info == "server_addr":
88	            return self._stream.extra(anyio.abc.SocketAttribute.remote_address, None)
89	        if info == "socket":

--------------------------------------------------
>> Issue: [B610:django_extra_used] Use of extra potential SQL attack vector.
   Severity: Medium   Confidence: Medium
   CWE: CWE-89 (https://cwe.mitre.org/data/definitions/89.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b610_django_extra_used.html
   Location: ./.audit-tools/pipx/venvs/semgrep/lib/python3.12/site-packages/httpcore/_backends/anyio.py:90:19
89	        if info == "socket":
90	            return self._stream.extra(anyio.abc.SocketAttribute.raw_socket, None)
91	        if info == "is_readable":

--------------------------------------------------
>> Issue: [B610:django_extra_used] Use of extra potential SQL attack vector.
   Severity: Medium   Confidence: Medium
   CWE: CWE-89 (https://cwe.mitre.org/data/definitions/89.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b610_django_extra_used.html
   Location: ./.audit-tools/pipx/venvs/semgrep/lib/python3.12/site-packages/httpcore/_backends/anyio.py:92:19
91	        if info == "is_readable":
92	            sock = self._stream.extra(anyio.abc.SocketAttribute.raw_socket, None)
93	            return is_socket_readable(sock)

--------------------------------------------------
>> Issue: [B324:hashlib] Use of weak SHA1 hash for security. Consider usedforsecurity=False
   Severity: High   Confidence: High
   CWE: CWE-327 (https://cwe.mitre.org/data/definitions/327.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b324_hashlib.html
   Location: ./.audit-tools/pipx/venvs/semgrep/lib/python3.12/site-packages/httpx/_auth.py:309:15
308	
309	        return hashlib.sha1(s).hexdigest()[:16].encode()
310	

--------------------------------------------------
>> Issue: [B310:blacklist] Audit url open for permitted schemes. Allowing use of file:/ or custom schemes is often unexpected.
   Severity: Medium   Confidence: High
   CWE: CWE-22 (https://cwe.mitre.org/data/definitions/22.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b310-urllib-urlopen
   Location: ./.audit-tools/pipx/venvs/semgrep/lib/python3.12/site-packages/jsonschema/validators.py:113:9
112	    request = Request(uri, headers=headers)  # noqa: S310
113	    with urlopen(request) as response:  # noqa: S310
114	        warnings.warn(

--------------------------------------------------
>> Issue: [B113:request_without_timeout] Call to requests without timeout
   Severity: Medium   Confidence: Low
   CWE: CWE-400 (https://cwe.mitre.org/data/definitions/400.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b113_request_without_timeout.html
   Location: ./.audit-tools/pipx/venvs/semgrep/lib/python3.12/site-packages/jsonschema/validators.py:1225:21
1224	            # json over http
1225	            result = requests.get(uri).json()
1226	        else:

--------------------------------------------------
>> Issue: [B310:blacklist] Audit url open for permitted schemes. Allowing use of file:/ or custom schemes is often unexpected.
   Severity: Medium   Confidence: High
   CWE: CWE-22 (https://cwe.mitre.org/data/definitions/22.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b310-urllib-urlopen
   Location: ./.audit-tools/pipx/venvs/semgrep/lib/python3.12/site-packages/jsonschema/validators.py:1228:17
1227	            # Otherwise, pass off to urllib and assume utf-8
1228	            with urlopen(uri) as url:  # noqa: S310
1229	                result = json.loads(url.read().decode("utf-8"))

--------------------------------------------------
>> Issue: [B310:blacklist] Audit url open for permitted schemes. Allowing use of file:/ or custom schemes is often unexpected.
   Severity: Medium   Confidence: High
   CWE: CWE-22 (https://cwe.mitre.org/data/definitions/22.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b310-urllib-urlopen
   Location: ./.audit-tools/pipx/venvs/semgrep/lib/python3.12/site-packages/jwt/jwks_client.py:108:17
107	            r = urllib.request.Request(url=self.uri, headers=self.headers)
108	            with urllib.request.urlopen(
109	                r, timeout=self.timeout, context=self.ssl_context
110	            ) as response:
111	                jwk_set = json.load(response)

--------------------------------------------------
>> Issue: [B602:subprocess_popen_with_shell_equals_true] subprocess call with shell=True identified, security issue.
   Severity: High   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b602_subprocess_popen_with_shell_equals_true.html
   Location: ./.audit-tools/pipx/venvs/semgrep/lib/python3.12/site-packages/mcp/cli/cli.py:48:16
47	            try:
48	                subprocess.run([cmd, "--version"], check=True, capture_output=True, shell=True)
49	                return cmd

--------------------------------------------------
>> Issue: [B602:subprocess_popen_with_shell_equals_true] subprocess call with shell=True identified, security issue.
   Severity: High   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b602_subprocess_popen_with_shell_equals_true.html
   Location: ./.audit-tools/pipx/venvs/semgrep/lib/python3.12/site-packages/mcp/cli/cli.py:281:18
280	            check=True,
281	            shell=shell,
282	            env=dict(os.environ.items()),  # Convert to list of tuples for env update
283	        )
284	        sys.exit(process.returncode)
285	    except subprocess.CalledProcessError as e:
286	        logger.error(
287	            "Dev server failed",

--------------------------------------------------
>> Issue: [B102:exec_used] Use of exec detected.
   Severity: Medium   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b102_exec_used.html
   Location: ./.audit-tools/pipx/venvs/semgrep/lib/python3.12/site-packages/peewee.py:174:4
173	    multi_types = (list, tuple, frozenset, set)
174	    exec('def reraise(tp, value, tb=None): raise tp, value, tb')
175	    def print_(s):

--------------------------------------------------
>> Issue: [B324:hashlib] Use of weak MD5 hash for security. Consider usedforsecurity=False
   Severity: High   Confidence: High
   CWE: CWE-327 (https://cwe.mitre.org/data/definitions/327.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b324_hashlib.html
   Location: ./.audit-tools/pipx/venvs/semgrep/lib/python3.12/site-packages/peewee.py:3045:20
3044	    if len(constraint) > maxlen:
3045	        name_hash = hashlib.md5(constraint.encode('utf-8')).hexdigest()
3046	        constraint = '%s_%s' % (constraint[:(maxlen - 8)], name_hash[:7])

--------------------------------------------------
>> Issue: [B608:hardcoded_sql_expressions] Possible SQL injection vector through string-based query construction.
   Severity: Medium   Confidence: Low
   CWE: CWE-89 (https://cwe.mitre.org/data/definitions/89.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b608_hardcoded_sql_expressions.html
   Location: ./.audit-tools/pipx/venvs/semgrep/lib/python3.12/site-packages/peewee.py:3852:34
3851	        schema = schema or 'main'
3852	        cursor = self.execute_sql('SELECT name FROM "%s".sqlite_master WHERE '
3853	                                  'type=? ORDER BY name' % schema, ('table',))
3854	        return [row for row, in cursor.fetchall()]

--------------------------------------------------
>> Issue: [B608:hardcoded_sql_expressions] Possible SQL injection vector through string-based query construction.
   Severity: Medium   Confidence: Low
   CWE: CWE-89 (https://cwe.mitre.org/data/definitions/89.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b608_hardcoded_sql_expressions.html
   Location: ./.audit-tools/pipx/venvs/semgrep/lib/python3.12/site-packages/peewee.py:3857:15
3856	    def get_views(self, schema=None):
3857	        sql = ('SELECT name, sql FROM "%s".sqlite_master WHERE type=? '
3858	               'ORDER BY name') % (schema or 'main')
3859	        return [ViewMetadata(*row) for row in self.execute_sql(sql, ('view',))]

--------------------------------------------------
>> Issue: [B608:hardcoded_sql_expressions] Possible SQL injection vector through string-based query construction.
   Severity: Medium   Confidence: Low
   CWE: CWE-89 (https://cwe.mitre.org/data/definitions/89.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b608_hardcoded_sql_expressions.html
   Location: ./.audit-tools/pipx/venvs/semgrep/lib/python3.12/site-packages/peewee.py:3863:17
3862	        schema = schema or 'main'
3863	        query = ('SELECT name, sql FROM "%s".sqlite_master '
3864	                 'WHERE tbl_name = ? AND type = ? ORDER BY name') % schema
3865	        cursor = self.execute_sql(query, (table, 'index'))

--------------------------------------------------
>> Issue: [B324:hashlib] Use of weak MD5 hash for security. Consider usedforsecurity=False
   Severity: High   Confidence: High
   CWE: CWE-327 (https://cwe.mitre.org/data/definitions/327.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b324_hashlib.html
   Location: ./.audit-tools/pipx/venvs/semgrep/lib/python3.12/site-packages/playhouse/migrate.py:178:21
177	    if len(index_name) > 64:
178	        index_hash = hashlib.md5(index_name.encode('utf-8')).hexdigest()
179	        index_name = '%s_%s' % (index_name[:56], index_hash[:7])

--------------------------------------------------
>> Issue: [B608:hardcoded_sql_expressions] Possible SQL injection vector through string-based query construction.
   Severity: Medium   Confidence: Low
   CWE: CWE-89 (https://cwe.mitre.org/data/definitions/89.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b608_hardcoded_sql_expressions.html
   Location: ./.audit-tools/pipx/venvs/semgrep/lib/python3.12/site-packages/playhouse/migrate.py:706:40
705	    def _get_column_names(self, table):
706	        res = self.database.execute_sql('select * from "%s" limit 1' % table)
707	        return [item[0] for item in res.description]

--------------------------------------------------
>> Issue: [B608:hardcoded_sql_expressions] Possible SQL injection vector through string-based query construction.
   Severity: Medium   Confidence: Medium
   CWE: CWE-89 (https://cwe.mitre.org/data/definitions/89.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b608_hardcoded_sql_expressions.html
   Location: ./.audit-tools/pipx/venvs/semgrep/lib/python3.12/site-packages/playhouse/reflection.py:388:30
387	        # Look up the actual column type for each column.
388	        cursor = self.execute('SELECT * FROM `%s` LIMIT 1' % table)
389	

--------------------------------------------------
>> Issue: [B608:hardcoded_sql_expressions] Possible SQL injection vector through string-based query construction.
   Severity: Medium   Confidence: Low
   CWE: CWE-89 (https://cwe.mitre.org/data/definitions/89.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b608_hardcoded_sql_expressions.html
   Location: ./.audit-tools/pipx/venvs/semgrep/lib/python3.12/site-packages/playhouse/sqlite_ext.py:426:12
425	        res = cls._meta.database.execute_sql(
426	            "INSERT INTO %s(%s) VALUES('%s');" % (tbl, tbl, cmd))
427	        return res.fetchone()

--------------------------------------------------
>> Issue: [B301:blacklist] Pickle and modules that wrap it can be unsafe when used to deserialize untrusted data, possible security issue.
   Severity: Medium   Confidence: High
   CWE: CWE-502 (https://cwe.mitre.org/data/definitions/502.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b301-pickle
   Location: ./.audit-tools/pipx/venvs/semgrep/lib/python3.12/site-packages/pydantic/deprecated/parse.py:54:15
53	        bb = b if isinstance(b, bytes) else b.encode()  # type: ignore
54	        return pickle.loads(bb)
55	    else:

--------------------------------------------------
>> Issue: [B301:blacklist] Pickle and modules that wrap it can be unsafe when used to deserialize untrusted data, possible security issue.
   Severity: Medium   Confidence: High
   CWE: CWE-502 (https://cwe.mitre.org/data/definitions/502.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b301-pickle
   Location: ./.audit-tools/pipx/venvs/semgrep/lib/python3.12/site-packages/pydantic/v1/parse.py:42:15
41	        bb = b if isinstance(b, bytes) else b.encode()
42	        return pickle.loads(bb)
43	    else:

--------------------------------------------------
>> Issue: [B307:blacklist] Use of possibly insecure function - consider using safer ast.literal_eval.
   Severity: Medium   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b307-eval
   Location: ./.audit-tools/pipx/venvs/semgrep/lib/python3.12/site-packages/pydantic/v1/utils.py:195:8
194	    try:
195	        eval('__IPYTHON__')
196	    except NameError:

--------------------------------------------------
>> Issue: [B102:exec_used] Use of exec detected.
   Severity: Medium   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b102_exec_used.html
   Location: ./.audit-tools/pipx/venvs/semgrep/lib/python3.12/site-packages/pygments/formatters/__init__.py:103:12
102	        with open(filename, 'rb') as f:
103	            exec(f.read(), custom_namespace)
104	        # Retrieve the class `formattername` from that namespace

--------------------------------------------------
>> Issue: [B102:exec_used] Use of exec detected.
   Severity: Medium   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b102_exec_used.html
   Location: ./.audit-tools/pipx/venvs/semgrep/lib/python3.12/site-packages/pygments/lexers/__init__.py:154:12
153	        with open(filename, 'rb') as f:
154	            exec(f.read(), custom_namespace)
155	        # Retrieve the class `lexername` from that namespace

--------------------------------------------------
>> Issue: [B310:blacklist] Audit url open for permitted schemes. Allowing use of file:/ or custom schemes is often unexpected.
   Severity: Medium   Confidence: High
   CWE: CWE-22 (https://cwe.mitre.org/data/definitions/22.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b310-urllib-urlopen
   Location: ./.audit-tools/pipx/venvs/semgrep/lib/python3.12/site-packages/pygments/lexers/_lua_builtins.py:225:12
224	    def get_newest_version():
225	        f = urlopen('http://www.lua.org/manual/')
226	        r = re.compile(r'^<A HREF="(\d\.\d)/">(Lua )?\1</A>')

--------------------------------------------------
>> Issue: [B310:blacklist] Audit url open for permitted schemes. Allowing use of file:/ or custom schemes is often unexpected.
   Severity: Medium   Confidence: High
   CWE: CWE-22 (https://cwe.mitre.org/data/definitions/22.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b310-urllib-urlopen
   Location: ./.audit-tools/pipx/venvs/semgrep/lib/python3.12/site-packages/pygments/lexers/_lua_builtins.py:233:12
232	    def get_lua_functions(version):
233	        f = urlopen(f'http://www.lua.org/manual/{version}/')
234	        r = re.compile(r'^<A HREF="manual.html#pdf-(?!lua|LUA)([^:]+)">\1</A>')

--------------------------------------------------
>> Issue: [B310:blacklist] Audit url open for permitted schemes. Allowing use of file:/ or custom schemes is often unexpected.
   Severity: Medium   Confidence: High
   CWE: CWE-22 (https://cwe.mitre.org/data/definitions/22.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b310-urllib-urlopen
   Location: ./.audit-tools/pipx/venvs/semgrep/lib/python3.12/site-packages/pygments/lexers/_mysql_builtins.py:1297:19
1296	        # Pull content from lex.h.
1297	        lex_file = urlopen(LEX_URL).read().decode('utf8', errors='ignore')
1298	        keywords = parse_lex_keywords(lex_file)

--------------------------------------------------
>> Issue: [B310:blacklist] Audit url open for permitted schemes. Allowing use of file:/ or custom schemes is often unexpected.
   Severity: Medium   Confidence: High
   CWE: CWE-22 (https://cwe.mitre.org/data/definitions/22.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b310-urllib-urlopen
   Location: ./.audit-tools/pipx/venvs/semgrep/lib/python3.12/site-packages/pygments/lexers/_mysql_builtins.py:1303:27
1302	        # Parse content in item_create.cc.
1303	        item_create_file = urlopen(ITEM_CREATE_URL).read().decode('utf8', errors='ignore')
1304	        functions.update(parse_item_create_functions(item_create_file))

--------------------------------------------------
>> Issue: [B310:blacklist] Audit url open for permitted schemes. Allowing use of file:/ or custom schemes is often unexpected.
   Severity: Medium   Confidence: High
   CWE: CWE-22 (https://cwe.mitre.org/data/definitions/22.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b310-urllib-urlopen
   Location: ./.audit-tools/pipx/venvs/semgrep/lib/python3.12/site-packages/pygments/lexers/_php_builtins.py:3299:19
3298	    def get_php_references():
3299	        download = urlretrieve(PHP_MANUAL_URL)
3300	        with tarfile.open(download[0]) as tar:

--------------------------------------------------
>> Issue: [B202:tarfile_unsafe_members] tarfile.extractall used without any validation. Please check and discard dangerous members.
   Severity: High   Confidence: High
   CWE: CWE-22 (https://cwe.mitre.org/data/definitions/22.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b202_tarfile_unsafe_members.html
   Location: ./.audit-tools/pipx/venvs/semgrep/lib/python3.12/site-packages/pygments/lexers/_php_builtins.py:3304:16
3303	            else:
3304	                tar.extractall()
3305	        yield from glob.glob(f"{PHP_MANUAL_DIR}{PHP_REFERENCE_GLOB}")

--------------------------------------------------
>> Issue: [B310:blacklist] Audit url open for permitted schemes. Allowing use of file:/ or custom schemes is often unexpected.
   Severity: Medium   Confidence: High
   CWE: CWE-22 (https://cwe.mitre.org/data/definitions/22.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b310-urllib-urlopen
   Location: ./.audit-tools/pipx/venvs/semgrep/lib/python3.12/site-packages/pygments/lexers/_postgres_builtins.py:642:18
641	    def update_myself():
642	        content = urlopen(DATATYPES_URL).read().decode('utf-8', errors='ignore')
643	        data_file = list(content.splitlines())

--------------------------------------------------
>> Issue: [B310:blacklist] Audit url open for permitted schemes. Allowing use of file:/ or custom schemes is often unexpected.
   Severity: Medium   Confidence: High
   CWE: CWE-22 (https://cwe.mitre.org/data/definitions/22.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b310-urllib-urlopen
   Location: ./.audit-tools/pipx/venvs/semgrep/lib/python3.12/site-packages/pygments/lexers/_postgres_builtins.py:647:18
646	
647	        content = urlopen(KEYWORDS_URL).read().decode('utf-8', errors='ignore')
648	        keywords = parse_keywords(content)

--------------------------------------------------
>> Issue: [B301:blacklist] Pickle and modules that wrap it can be unsafe when used to deserialize untrusted data, possible security issue.
   Severity: Medium   Confidence: High
   CWE: CWE-502 (https://cwe.mitre.org/data/definitions/502.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b301-pickle
   Location: ./.audit-tools/pipx/venvs/semgrep/lib/python3.12/site-packages/rich/style.py:475:66
474	        """Get meta information (can not be changed after construction)."""
475	        return {} if self._meta is None else cast(Dict[str, Any], loads(self._meta))
476	

--------------------------------------------------
>> Issue: [B108:hardcoded_tmp_directory] Probable insecure usage of temp file/directory.
   Severity: Medium   Confidence: Medium
   CWE: CWE-377 (https://cwe.mitre.org/data/definitions/377.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b108_hardcoded_tmp_directory.html
   Location: ./.audit-tools/pipx/venvs/semgrep/lib/python3.12/site-packages/ruamel/yaml/compat.py:151:17
150	nprint = Nprint()
151	nprintf = Nprint('/var/tmp/ruamel.yaml.log')
152	

--------------------------------------------------
>> Issue: [B307:blacklist] Use of possibly insecure function - consider using safer ast.literal_eval.
   Severity: Medium   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b307-eval
   Location: ./.audit-tools/pipx/venvs/semgrep/lib/python3.12/site-packages/typing_extensions.py:4034:53
4033	        return_value = {key:
4034	            value if not isinstance(value, str) else eval(value, globals, locals)
4035	            for key, value in ann.items() }

--------------------------------------------------
>> Issue: [B307:blacklist] Use of possibly insecure function - consider using safer ast.literal_eval.
   Severity: Medium   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b307-eval
   Location: ./.audit-tools/pipx/venvs/semgrep/lib/python3.12/site-packages/typing_extensions.py:4116:20
4115	            code = forward_ref.__forward_code__
4116	            value = eval(code, globals, locals)
4117	        forward_ref.__forward_evaluated__ = True

--------------------------------------------------
>> Issue: [B102:exec_used] Use of exec detected.
   Severity: Medium   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b102_exec_used.html
   Location: ./.audit-tools/pipx/venvs/semgrep/lib/python3.12/site-packages/typing_inspection/typing_objects.py:101:4
100	    globals_: dict[str, Any] = {'Any': Any, 'typing': typing, 'typing_extensions': typing_extensions}
101	    exec(func_code, globals_, locals_)
102	    return locals_[function_name]

--------------------------------------------------
>> Issue: [B102:exec_used] Use of exec detected.
   Severity: Medium   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b102_exec_used.html
   Location: ./.audit-tools/pipx/venvs/semgrep/lib/python3.12/site-packages/typing_inspection/typing_objects.py:133:4
132	    globals_: dict[str, Any] = {'Any': Any, 'typing': typing, 'typing_extensions': typing_extensions}
133	    exec(func_code, globals_, locals_)
134	    return locals_[function_name]

--------------------------------------------------
>> Issue: [B104:hardcoded_bind_all_interfaces] Possible binding to all interfaces.
   Severity: Medium   Confidence: Medium
   CWE: CWE-605 (https://cwe.mitre.org/data/definitions/605.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b104_hardcoded_bind_all_interfaces.html
   Location: ./.audit-tools/pipx/venvs/semgrep/lib/python3.12/site-packages/uvicorn/server.py:212:19
211	            addr_format = "%s://%s:%d"
212	            host = "0.0.0.0" if config.host is None else config.host
213	            if ":" in host:

--------------------------------------------------
>> Issue: [B102:exec_used] Use of exec detected.
   Severity: Medium   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b102_exec_used.html
   Location: ./.audit-tools/pipx/venvs/semgrep/lib/python3.12/site-packages/wrapt/decorators.py:23:8
22	            _locs_ = _globs_
23	        exec("""exec _code_ in _globs_, _locs_""")
24	

--------------------------------------------------
>> Issue: [B307:blacklist] Use of possibly insecure function - consider using safer ast.literal_eval.
   Severity: Medium   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b307-eval
   Location: ./.venv/lib/python3.11/site-packages/_pytest/_code/code.py:170:15
169	        f_locals.update(vars)
170	        return eval(code, self.f_globals, f_locals)
171	

--------------------------------------------------
>> Issue: [B102:exec_used] Use of exec detected.
   Severity: Medium   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b102_exec_used.html
   Location: ./.venv/lib/python3.11/site-packages/_pytest/_py/path.py:1153:24
1152	                    with open(str(self), "rb") as f:
1153	                        exec(f.read(), mod.__dict__)
1154	                except BaseException:

--------------------------------------------------
>> Issue: [B102:exec_used] Use of exec detected.
   Severity: Medium   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b102_exec_used.html
   Location: ./.venv/lib/python3.11/site-packages/_pytest/assertion/rewrite.py:197:8
196	            state.trace(f"found cached rewritten pyc for {fn}")
197	        exec(co, module.__dict__)
198	

--------------------------------------------------
>> Issue: [B302:blacklist] Deserialization with the marshal module is possibly dangerous.
   Severity: Medium   Confidence: High
   CWE: CWE-502 (https://cwe.mitre.org/data/definitions/502.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b302-marshal
   Location: ./.venv/lib/python3.11/site-packages/_pytest/assertion/rewrite.py:402:17
401	        try:
402	            co = marshal.load(fp)
403	        except Exception as e:

--------------------------------------------------
>> Issue: [B307:blacklist] Use of possibly insecure function - consider using safer ast.literal_eval.
   Severity: Medium   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b307-eval
   Location: ./.venv/lib/python3.11/site-packages/_pytest/mark/expression.py:353:20
352	        """
353	        return bool(eval(self._code, {"__builtins__": {}}, MatcherAdapter(matcher)))

--------------------------------------------------
>> Issue: [B310:blacklist] Audit url open for permitted schemes. Allowing use of file:/ or custom schemes is often unexpected.
   Severity: Medium   Confidence: High
   CWE: CWE-22 (https://cwe.mitre.org/data/definitions/22.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b310-urllib-urlopen
   Location: ./.venv/lib/python3.11/site-packages/_pytest/pastebin.py:87:12
86	        response: str = (
87	            urlopen(url, data=urlencode(params).encode("ascii")).read().decode("utf-8")
88	        )

--------------------------------------------------
>> Issue: [B307:blacklist] Use of possibly insecure function - consider using safer ast.literal_eval.
   Severity: Medium   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b307-eval
   Location: ./.venv/lib/python3.11/site-packages/_pytest/pytester.py:295:23
294	                    print("NAMEMATCH", name, call)
295	                    if eval(check, backlocals, call.__dict__):
296	                        print("CHECKERMATCH", repr(check), "->", call)

--------------------------------------------------
>> Issue: [B307:blacklist] Use of possibly insecure function - consider using safer ast.literal_eval.
   Severity: Medium   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b307-eval
   Location: ./.venv/lib/python3.11/site-packages/_pytest/skipping.py:119:21
118	            condition_code = compile(condition, filename, "eval")
119	            result = eval(condition_code, globals_)
120	        except SyntaxError as exc:

--------------------------------------------------
>> Issue: [B608:hardcoded_sql_expressions] Possible SQL injection vector through string-based query construction.
   Severity: Medium   Confidence: Medium
   CWE: CWE-89 (https://cwe.mitre.org/data/definitions/89.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b608_hardcoded_sql_expressions.html
   Location: ./.venv/lib/python3.11/site-packages/aiosqlite/tests/perf.py:174:33
173	            for i in range(100):
174	                await db.execute("insert into perf (k) values (%d)" % (i,))
175	            await db.commit()

--------------------------------------------------
>> Issue: [B608:hardcoded_sql_expressions] Possible SQL injection vector through string-based query construction.
   Severity: Medium   Confidence: Medium
   CWE: CWE-89 (https://cwe.mitre.org/data/definitions/89.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b608_hardcoded_sql_expressions.html
   Location: ./.venv/lib/python3.11/site-packages/aiosqlite/tests/perf.py:187:33
186	            for i in range(100):
187	                await db.execute("insert into perf (k) values (%d)" % (i,))
188	            await db.commit()

--------------------------------------------------
>> Issue: [B604:any_other_function_with_shell_equals_true] Function call with shell=True parameter identified, possible security issue.
   Severity: Medium   Confidence: Low
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b604_any_other_function_with_shell_equals_true.html
   Location: ./.venv/lib/python3.11/site-packages/anyio/_backends/_trio.py:1103:28
1102	                stderr=stderr,
1103	                shell=True,
1104	                **kwargs,
1105	            )
1106	        else:
1107	            process = await trio.lowlevel.open_process(
1108	                [convert_item(item) for item in command],
1109	                stdin=stdin,
1110	                stdout=stdout,
1111	                stderr=stderr,

--------------------------------------------------
>> Issue: [B104:hardcoded_bind_all_interfaces] Possible binding to all interfaces.
   Severity: Medium   Confidence: Medium
   CWE: CWE-605 (https://cwe.mitre.org/data/definitions/605.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b104_hardcoded_bind_all_interfaces.html
   Location: ./.venv/lib/python3.11/site-packages/anyio/_core/_sockets.py:490:25
489	    else:
490	        local_address = ("0.0.0.0", 0)
491	

--------------------------------------------------
>> Issue: [B610:django_extra_used] Use of extra potential SQL attack vector.
   Severity: Medium   Confidence: Medium
   CWE: CWE-89 (https://cwe.mitre.org/data/definitions/89.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b610_django_extra_used.html
   Location: ./.venv/lib/python3.11/site-packages/anyio/streams/tls.py:249:22
248	    async def send_eof(self) -> None:
249	        tls_version = self.extra(TLSAttribute.tls_version)
250	        match = re.match(r"TLSv(\d+)(?:\.(\d+))?", tls_version)

--------------------------------------------------
>> Issue: [B301:blacklist] Pickle and modules that wrap it can be unsafe when used to deserialize untrusted data, possible security issue.
   Severity: Medium   Confidence: High
   CWE: CWE-502 (https://cwe.mitre.org/data/definitions/502.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b301-pickle
   Location: ./.venv/lib/python3.11/site-packages/anyio/to_interpreter.py:130:22
129	            if fmt == FMT_PICKLED:
130	                res = pickle.loads(res)
131	

--------------------------------------------------
>> Issue: [B301:blacklist] Pickle and modules that wrap it can be unsafe when used to deserialize untrusted data, possible security issue.
   Severity: Medium   Confidence: High
   CWE: CWE-502 (https://cwe.mitre.org/data/definitions/502.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b301-pickle
   Location: ./.venv/lib/python3.11/site-packages/anyio/to_process.py:94:17
93	
94	        retval = pickle.loads(pickled_response)
95	        if status == b"EXCEPTION":

--------------------------------------------------
>> Issue: [B301:blacklist] Pickle and modules that wrap it can be unsafe when used to deserialize untrusted data, possible security issue.
   Severity: Medium   Confidence: High
   CWE: CWE-502 (https://cwe.mitre.org/data/definitions/502.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b301-pickle
   Location: ./.venv/lib/python3.11/site-packages/anyio/to_process.py:218:29
217	        try:
218	            command, *args = pickle.load(stdin.buffer)
219	        except EOFError:

--------------------------------------------------
>> Issue: [B307:blacklist] Use of possibly insecure function - consider using safer ast.literal_eval.
   Severity: Medium   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b307-eval
   Location: ./.venv/lib/python3.11/site-packages/attr/_make.py:227:4
226	    bytecode = compile(script, filename, "exec")
227	    eval(bytecode, globs, locs)
228	

--------------------------------------------------
>> Issue: [B307:blacklist] Use of possibly insecure function - consider using safer ast.literal_eval.
   Severity: Medium   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b307-eval
   Location: ./.venv/lib/python3.11/site-packages/cffi/recompiler.py:78:16
77	    def as_python_expr(self):
78	        flags = eval(self.flags, G_FLAGS)
79	        fields_expr = [c_field.as_field_python_expr()

--------------------------------------------------
>> Issue: [B102:exec_used] Use of exec detected.
   Severity: Medium   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b102_exec_used.html
   Location: ./.venv/lib/python3.11/site-packages/cffi/setuptools_ext.py:26:4
25	    code = compile(src, filename, 'exec')
26	    exec(code, glob, glob)
27	

--------------------------------------------------
>> Issue: [B303:blacklist] Use of insecure MD2, MD4, MD5, or SHA1 hash function.
   Severity: Medium   Confidence: High
   CWE: CWE-327 (https://cwe.mitre.org/data/definitions/327.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b303-md5
   Location: ./.venv/lib/python3.11/site-packages/cryptography/hazmat/_oid.py:128:40
127	_SIG_OIDS_TO_HASH: dict[ObjectIdentifier, hashes.HashAlgorithm | None] = {
128	    SignatureAlgorithmOID.RSA_WITH_MD5: hashes.MD5(),
129	    SignatureAlgorithmOID.RSA_WITH_SHA1: hashes.SHA1(),

--------------------------------------------------
>> Issue: [B303:blacklist] Use of insecure MD2, MD4, MD5, or SHA1 hash function.
   Severity: Medium   Confidence: High
   CWE: CWE-327 (https://cwe.mitre.org/data/definitions/327.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b303-md5
   Location: ./.venv/lib/python3.11/site-packages/cryptography/hazmat/_oid.py:129:41
128	    SignatureAlgorithmOID.RSA_WITH_MD5: hashes.MD5(),
129	    SignatureAlgorithmOID.RSA_WITH_SHA1: hashes.SHA1(),
130	    SignatureAlgorithmOID._RSA_WITH_SHA1: hashes.SHA1(),

--------------------------------------------------
>> Issue: [B303:blacklist] Use of insecure MD2, MD4, MD5, or SHA1 hash function.
   Severity: Medium   Confidence: High
   CWE: CWE-327 (https://cwe.mitre.org/data/definitions/327.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b303-md5
   Location: ./.venv/lib/python3.11/site-packages/cryptography/hazmat/_oid.py:130:42
129	    SignatureAlgorithmOID.RSA_WITH_SHA1: hashes.SHA1(),
130	    SignatureAlgorithmOID._RSA_WITH_SHA1: hashes.SHA1(),
131	    SignatureAlgorithmOID.RSA_WITH_SHA224: hashes.SHA224(),

--------------------------------------------------
>> Issue: [B303:blacklist] Use of insecure MD2, MD4, MD5, or SHA1 hash function.
   Severity: Medium   Confidence: High
   CWE: CWE-327 (https://cwe.mitre.org/data/definitions/327.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b303-md5
   Location: ./.venv/lib/python3.11/site-packages/cryptography/hazmat/_oid.py:139:43
138	    SignatureAlgorithmOID.RSA_WITH_SHA3_512: hashes.SHA3_512(),
139	    SignatureAlgorithmOID.ECDSA_WITH_SHA1: hashes.SHA1(),
140	    SignatureAlgorithmOID.ECDSA_WITH_SHA224: hashes.SHA224(),

--------------------------------------------------
>> Issue: [B303:blacklist] Use of insecure MD2, MD4, MD5, or SHA1 hash function.
   Severity: Medium   Confidence: High
   CWE: CWE-327 (https://cwe.mitre.org/data/definitions/327.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b303-md5
   Location: ./.venv/lib/python3.11/site-packages/cryptography/hazmat/_oid.py:148:41
147	    SignatureAlgorithmOID.ECDSA_WITH_SHA3_512: hashes.SHA3_512(),
148	    SignatureAlgorithmOID.DSA_WITH_SHA1: hashes.SHA1(),
149	    SignatureAlgorithmOID.DSA_WITH_SHA224: hashes.SHA224(),

--------------------------------------------------
>> Issue: [B305:blacklist] Use of insecure cipher mode cryptography.hazmat.primitives.ciphers.modes.ECB.
   Severity: Medium   Confidence: High
   CWE: CWE-327 (https://cwe.mitre.org/data/definitions/327.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b304-b305-ciphers-and-modes
   Location: ./.venv/lib/python3.11/site-packages/cryptography/hazmat/primitives/keywrap.py:21:42
20	    # RFC 3394 Key Wrap - 2.2.1 (index method)
21	    encryptor = Cipher(AES(wrapping_key), ECB()).encryptor()
22	    n = len(r)

--------------------------------------------------
>> Issue: [B305:blacklist] Use of insecure cipher mode cryptography.hazmat.primitives.ciphers.modes.ECB.
   Severity: Medium   Confidence: High
   CWE: CWE-327 (https://cwe.mitre.org/data/definitions/327.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b304-b305-ciphers-and-modes
   Location: ./.venv/lib/python3.11/site-packages/cryptography/hazmat/primitives/keywrap.py:64:42
63	    # Implement RFC 3394 Key Unwrap - 2.2.2 (index method)
64	    decryptor = Cipher(AES(wrapping_key), ECB()).decryptor()
65	    n = len(r)

--------------------------------------------------
>> Issue: [B305:blacklist] Use of insecure cipher mode cryptography.hazmat.primitives.ciphers.modes.ECB.
   Severity: Medium   Confidence: High
   CWE: CWE-327 (https://cwe.mitre.org/data/definitions/327.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b304-b305-ciphers-and-modes
   Location: ./.venv/lib/python3.11/site-packages/cryptography/hazmat/primitives/keywrap.py:100:46
99	        # RFC 5649 - 4.1 - exactly 8 octets after padding
100	        encryptor = Cipher(AES(wrapping_key), ECB()).encryptor()
101	        b = encryptor.update(aiv + key_to_wrap)

--------------------------------------------------
>> Issue: [B305:blacklist] Use of insecure cipher mode cryptography.hazmat.primitives.ciphers.modes.ECB.
   Severity: Medium   Confidence: High
   CWE: CWE-327 (https://cwe.mitre.org/data/definitions/327.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b304-b305-ciphers-and-modes
   Location: ./.venv/lib/python3.11/site-packages/cryptography/hazmat/primitives/keywrap.py:122:46
121	        # RFC 5649 - 4.2 - exactly two 64-bit blocks
122	        decryptor = Cipher(AES(wrapping_key), ECB()).decryptor()
123	        out = decryptor.update(wrapped_key)

--------------------------------------------------
>> Issue: [B303:blacklist] Use of insecure MD2, MD4, MD5, or SHA1 hash function.
   Severity: Medium   Confidence: High
   CWE: CWE-327 (https://cwe.mitre.org/data/definitions/327.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b303-md5
   Location: ./.venv/lib/python3.11/site-packages/cryptography/hazmat/primitives/serialization/ssh.py:1009:27
1008	            if self._inner_sig_type == _SSH_RSA:
1009	                hash_alg = hashes.SHA1()
1010	            elif self._inner_sig_type == _SSH_RSA_SHA256:

--------------------------------------------------
>> Issue: [B324:hashlib] Use of weak SHA1 hash for security. Consider usedforsecurity=False
   Severity: High   Confidence: High
   CWE: CWE-327 (https://cwe.mitre.org/data/definitions/327.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b324_hashlib.html
   Location: ./.venv/lib/python3.11/site-packages/cryptography/x509/extensions.py:72:11
71	
72	    return hashlib.sha1(data).digest()
73	

--------------------------------------------------
>> Issue: [B610:django_extra_used] Use of extra potential SQL attack vector.
   Severity: Medium   Confidence: Medium
   CWE: CWE-89 (https://cwe.mitre.org/data/definitions/89.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b610_django_extra_used.html
   Location: ./.venv/lib/python3.11/site-packages/httpcore/_backends/anyio.py:84:19
83	        if info == "ssl_object":
84	            return self._stream.extra(anyio.streams.tls.TLSAttribute.ssl_object, None)
85	        if info == "client_addr":

--------------------------------------------------
>> Issue: [B610:django_extra_used] Use of extra potential SQL attack vector.
   Severity: Medium   Confidence: Medium
   CWE: CWE-89 (https://cwe.mitre.org/data/definitions/89.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b610_django_extra_used.html
   Location: ./.venv/lib/python3.11/site-packages/httpcore/_backends/anyio.py:86:19
85	        if info == "client_addr":
86	            return self._stream.extra(anyio.abc.SocketAttribute.local_address, None)
87	        if info == "server_addr":

--------------------------------------------------
>> Issue: [B610:django_extra_used] Use of extra potential SQL attack vector.
   Severity: Medium   Confidence: Medium
   CWE: CWE-89 (https://cwe.mitre.org/data/definitions/89.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b610_django_extra_used.html
   Location: ./.venv/lib/python3.11/site-packages/httpcore/_backends/anyio.py:88:19
87	        if info == "server_addr":
88	            return self._stream.extra(anyio.abc.SocketAttribute.remote_address, None)
89	        if info == "socket":

--------------------------------------------------
>> Issue: [B610:django_extra_used] Use of extra potential SQL attack vector.
   Severity: Medium   Confidence: Medium
   CWE: CWE-89 (https://cwe.mitre.org/data/definitions/89.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b610_django_extra_used.html
   Location: ./.venv/lib/python3.11/site-packages/httpcore/_backends/anyio.py:90:19
89	        if info == "socket":
90	            return self._stream.extra(anyio.abc.SocketAttribute.raw_socket, None)
91	        if info == "is_readable":

--------------------------------------------------
>> Issue: [B610:django_extra_used] Use of extra potential SQL attack vector.
   Severity: Medium   Confidence: Medium
   CWE: CWE-89 (https://cwe.mitre.org/data/definitions/89.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b610_django_extra_used.html
   Location: ./.venv/lib/python3.11/site-packages/httpcore/_backends/anyio.py:92:19
91	        if info == "is_readable":
92	            sock = self._stream.extra(anyio.abc.SocketAttribute.raw_socket, None)
93	            return is_socket_readable(sock)

--------------------------------------------------
>> Issue: [B324:hashlib] Use of weak SHA1 hash for security. Consider usedforsecurity=False
   Severity: High   Confidence: High
   CWE: CWE-327 (https://cwe.mitre.org/data/definitions/327.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b324_hashlib.html
   Location: ./.venv/lib/python3.11/site-packages/httpx/_auth.py:309:15
308	
309	        return hashlib.sha1(s).hexdigest()[:16].encode()
310	

--------------------------------------------------
>> Issue: [B310:blacklist] Audit url open for permitted schemes. Allowing use of file:/ or custom schemes is often unexpected.
   Severity: Medium   Confidence: High
   CWE: CWE-22 (https://cwe.mitre.org/data/definitions/22.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b310-urllib-urlopen
   Location: ./.venv/lib/python3.11/site-packages/jsonschema/validators.py:112:9
111	    request = Request(uri, headers=headers)  # noqa: S310
112	    with urlopen(request) as response:  # noqa: S310
113	        warnings.warn(

--------------------------------------------------
>> Issue: [B113:request_without_timeout] Call to requests without timeout
   Severity: Medium   Confidence: Low
   CWE: CWE-400 (https://cwe.mitre.org/data/definitions/400.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b113_request_without_timeout.html
   Location: ./.venv/lib/python3.11/site-packages/jsonschema/validators.py:1224:21
1223	            # json over http
1224	            result = requests.get(uri).json()
1225	        else:

--------------------------------------------------
>> Issue: [B310:blacklist] Audit url open for permitted schemes. Allowing use of file:/ or custom schemes is often unexpected.
   Severity: Medium   Confidence: High
   CWE: CWE-22 (https://cwe.mitre.org/data/definitions/22.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b310-urllib-urlopen
   Location: ./.venv/lib/python3.11/site-packages/jsonschema/validators.py:1228:17
1227	            from urllib.request import urlopen
1228	            with urlopen(uri) as url:  # noqa: S310
1229	                result = json.loads(url.read().decode("utf-8"))

--------------------------------------------------
>> Issue: [B310:blacklist] Audit url open for permitted schemes. Allowing use of file:/ or custom schemes is often unexpected.
   Severity: Medium   Confidence: High
   CWE: CWE-22 (https://cwe.mitre.org/data/definitions/22.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b310-urllib-urlopen
   Location: ./.venv/lib/python3.11/site-packages/jwt/jwks_client.py:118:17
117	            r = urllib.request.Request(url=self.uri, headers=self.headers)
118	            with urllib.request.urlopen(
119	                r, timeout=self.timeout, context=self.ssl_context
120	            ) as response:
121	                jwk_set = json.load(response)

--------------------------------------------------
>> Issue: [B602:subprocess_popen_with_shell_equals_true] subprocess call with shell=True identified, security issue.
   Severity: High   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b602_subprocess_popen_with_shell_equals_true.html
   Location: ./.venv/lib/python3.11/site-packages/mcp/cli/cli.py:48:16
47	            try:
48	                subprocess.run([cmd, "--version"], check=True, capture_output=True, shell=True)
49	                return cmd

--------------------------------------------------
>> Issue: [B602:subprocess_popen_with_shell_equals_true] subprocess call with shell=True identified, security issue.
   Severity: High   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b602_subprocess_popen_with_shell_equals_true.html
   Location: ./.venv/lib/python3.11/site-packages/mcp/cli/cli.py:281:18
280	            check=True,
281	            shell=shell,
282	            env=dict(os.environ.items()),  # Convert to list of tuples for env update
283	        )
284	        sys.exit(process.returncode)
285	    except subprocess.CalledProcessError as e:
286	        logger.error(
287	            "Dev server failed",

--------------------------------------------------
>> Issue: [B301:blacklist] Pickle and modules that wrap it can be unsafe when used to deserialize untrusted data, possible security issue.
   Severity: Medium   Confidence: High
   CWE: CWE-502 (https://cwe.mitre.org/data/definitions/502.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b301-pickle
   Location: ./.venv/lib/python3.11/site-packages/pydantic/deprecated/parse.py:54:15
53	        bb = b if isinstance(b, bytes) else b.encode()  # type: ignore
54	        return pickle.loads(bb)
55	    else:

--------------------------------------------------
>> Issue: [B301:blacklist] Pickle and modules that wrap it can be unsafe when used to deserialize untrusted data, possible security issue.
   Severity: Medium   Confidence: High
   CWE: CWE-502 (https://cwe.mitre.org/data/definitions/502.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b301-pickle
   Location: ./.venv/lib/python3.11/site-packages/pydantic/v1/parse.py:42:15
41	        bb = b if isinstance(b, bytes) else b.encode()
42	        return pickle.loads(bb)
43	    else:

--------------------------------------------------
>> Issue: [B307:blacklist] Use of possibly insecure function - consider using safer ast.literal_eval.
   Severity: Medium   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b307-eval
   Location: ./.venv/lib/python3.11/site-packages/pydantic/v1/utils.py:195:8
194	    try:
195	        eval('__IPYTHON__')
196	    except NameError:

--------------------------------------------------
>> Issue: [B102:exec_used] Use of exec detected.
   Severity: Medium   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b102_exec_used.html
   Location: ./.venv/lib/python3.11/site-packages/pygments/formatters/__init__.py:103:12
102	        with open(filename, 'rb') as f:
103	            exec(f.read(), custom_namespace)
104	        # Retrieve the class `formattername` from that namespace

--------------------------------------------------
>> Issue: [B102:exec_used] Use of exec detected.
   Severity: Medium   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b102_exec_used.html
   Location: ./.venv/lib/python3.11/site-packages/pygments/lexers/__init__.py:154:12
153	        with open(filename, 'rb') as f:
154	            exec(f.read(), custom_namespace)
155	        # Retrieve the class `lexername` from that namespace

--------------------------------------------------
>> Issue: [B310:blacklist] Audit url open for permitted schemes. Allowing use of file:/ or custom schemes is often unexpected.
   Severity: Medium   Confidence: High
   CWE: CWE-22 (https://cwe.mitre.org/data/definitions/22.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b310-urllib-urlopen
   Location: ./.venv/lib/python3.11/site-packages/pygments/lexers/_lua_builtins.py:225:12
224	    def get_newest_version():
225	        f = urlopen('http://www.lua.org/manual/')
226	        r = re.compile(r'^<A HREF="(\d\.\d)/">(Lua )?\1</A>')

--------------------------------------------------
>> Issue: [B310:blacklist] Audit url open for permitted schemes. Allowing use of file:/ or custom schemes is often unexpected.
   Severity: Medium   Confidence: High
   CWE: CWE-22 (https://cwe.mitre.org/data/definitions/22.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b310-urllib-urlopen
   Location: ./.venv/lib/python3.11/site-packages/pygments/lexers/_lua_builtins.py:233:12
232	    def get_lua_functions(version):
233	        f = urlopen(f'http://www.lua.org/manual/{version}/')
234	        r = re.compile(r'^<A HREF="manual.html#pdf-(?!lua|LUA)([^:]+)">\1</A>')

--------------------------------------------------
>> Issue: [B310:blacklist] Audit url open for permitted schemes. Allowing use of file:/ or custom schemes is often unexpected.
   Severity: Medium   Confidence: High
   CWE: CWE-22 (https://cwe.mitre.org/data/definitions/22.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b310-urllib-urlopen
   Location: ./.venv/lib/python3.11/site-packages/pygments/lexers/_mysql_builtins.py:1297:19
1296	        # Pull content from lex.h.
1297	        lex_file = urlopen(LEX_URL).read().decode('utf8', errors='ignore')
1298	        keywords = parse_lex_keywords(lex_file)

--------------------------------------------------
>> Issue: [B310:blacklist] Audit url open for permitted schemes. Allowing use of file:/ or custom schemes is often unexpected.
   Severity: Medium   Confidence: High
   CWE: CWE-22 (https://cwe.mitre.org/data/definitions/22.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b310-urllib-urlopen
   Location: ./.venv/lib/python3.11/site-packages/pygments/lexers/_mysql_builtins.py:1303:27
1302	        # Parse content in item_create.cc.
1303	        item_create_file = urlopen(ITEM_CREATE_URL).read().decode('utf8', errors='ignore')
1304	        functions.update(parse_item_create_functions(item_create_file))

--------------------------------------------------
>> Issue: [B310:blacklist] Audit url open for permitted schemes. Allowing use of file:/ or custom schemes is often unexpected.
   Severity: Medium   Confidence: High
   CWE: CWE-22 (https://cwe.mitre.org/data/definitions/22.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b310-urllib-urlopen
   Location: ./.venv/lib/python3.11/site-packages/pygments/lexers/_php_builtins.py:3299:19
3298	    def get_php_references():
3299	        download = urlretrieve(PHP_MANUAL_URL)
3300	        with tarfile.open(download[0]) as tar:

--------------------------------------------------
>> Issue: [B202:tarfile_unsafe_members] tarfile.extractall used without any validation. Please check and discard dangerous members.
   Severity: High   Confidence: High
   CWE: CWE-22 (https://cwe.mitre.org/data/definitions/22.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b202_tarfile_unsafe_members.html
   Location: ./.venv/lib/python3.11/site-packages/pygments/lexers/_php_builtins.py:3304:16
3303	            else:
3304	                tar.extractall()
3305	        yield from glob.glob(f"{PHP_MANUAL_DIR}{PHP_REFERENCE_GLOB}")

--------------------------------------------------
>> Issue: [B310:blacklist] Audit url open for permitted schemes. Allowing use of file:/ or custom schemes is often unexpected.
   Severity: Medium   Confidence: High
   CWE: CWE-22 (https://cwe.mitre.org/data/definitions/22.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b310-urllib-urlopen
   Location: ./.venv/lib/python3.11/site-packages/pygments/lexers/_postgres_builtins.py:642:18
641	    def update_myself():
642	        content = urlopen(DATATYPES_URL).read().decode('utf-8', errors='ignore')
643	        data_file = list(content.splitlines())

--------------------------------------------------
>> Issue: [B310:blacklist] Audit url open for permitted schemes. Allowing use of file:/ or custom schemes is often unexpected.
   Severity: Medium   Confidence: High
   CWE: CWE-22 (https://cwe.mitre.org/data/definitions/22.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b310-urllib-urlopen
   Location: ./.venv/lib/python3.11/site-packages/pygments/lexers/_postgres_builtins.py:647:18
646	
647	        content = urlopen(KEYWORDS_URL).read().decode('utf-8', errors='ignore')
648	        keywords = parse_keywords(content)

--------------------------------------------------
>> Issue: [B303:blacklist] Use of insecure MD2, MD4, MD5, or SHA1 hash function.
   Severity: Medium   Confidence: High
   CWE: CWE-327 (https://cwe.mitre.org/data/definitions/327.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b303-md5
   Location: ./.venv/lib/python3.11/site-packages/telegram/_passport/credentials.py:187:44
186	                    b64decode(self.secret),
187	                    OAEP(mgf=MGF1(algorithm=SHA1()), algorithm=SHA1(), label=None),  # skipcq
188	                )

--------------------------------------------------
>> Issue: [B303:blacklist] Use of insecure MD2, MD4, MD5, or SHA1 hash function.
   Severity: Medium   Confidence: High
   CWE: CWE-327 (https://cwe.mitre.org/data/definitions/327.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b303-md5
   Location: ./.venv/lib/python3.11/site-packages/telegram/_passport/credentials.py:187:63
186	                    b64decode(self.secret),
187	                    OAEP(mgf=MGF1(algorithm=SHA1()), algorithm=SHA1(), label=None),  # skipcq
188	                )

--------------------------------------------------
>> Issue: [B307:blacklist] Use of possibly insecure function - consider using safer ast.literal_eval.
   Severity: Medium   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b307-eval
   Location: ./.venv/lib/python3.11/site-packages/tqdm/cli.py:38:19
37	        if re.match(r"^\\\w+$", val):
38	            return eval(f'"{val}"').encode()
39	        raise TqdmTypeError(f"{val} : {typ}")

--------------------------------------------------
>> Issue: [B307:blacklist] Use of possibly insecure function - consider using safer ast.literal_eval.
   Severity: Medium   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b307-eval
   Location: ./.venv/lib/python3.11/site-packages/typing_extensions.py:4034:53
4033	        return_value = {key:
4034	            value if not isinstance(value, str) else eval(value, globals, locals)
4035	            for key, value in ann.items() }

--------------------------------------------------
>> Issue: [B307:blacklist] Use of possibly insecure function - consider using safer ast.literal_eval.
   Severity: Medium   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/blacklists/blacklist_calls.html#b307-eval
   Location: ./.venv/lib/python3.11/site-packages/typing_extensions.py:4116:20
4115	            code = forward_ref.__forward_code__
4116	            value = eval(code, globals, locals)
4117	        forward_ref.__forward_evaluated__ = True

--------------------------------------------------
>> Issue: [B102:exec_used] Use of exec detected.
   Severity: Medium   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b102_exec_used.html
   Location: ./.venv/lib/python3.11/site-packages/typing_inspection/typing_objects.py:101:4
100	    globals_: dict[str, Any] = {'Any': Any, 'typing': typing, 'typing_extensions': typing_extensions}
101	    exec(func_code, globals_, locals_)
102	    return locals_[function_name]

--------------------------------------------------
>> Issue: [B102:exec_used] Use of exec detected.
   Severity: Medium   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b102_exec_used.html
   Location: ./.venv/lib/python3.11/site-packages/typing_inspection/typing_objects.py:133:4
132	    globals_: dict[str, Any] = {'Any': Any, 'typing': typing, 'typing_extensions': typing_extensions}
133	    exec(func_code, globals_, locals_)
134	    return locals_[function_name]

--------------------------------------------------
>> Issue: [B104:hardcoded_bind_all_interfaces] Possible binding to all interfaces.
   Severity: Medium   Confidence: Medium
   CWE: CWE-605 (https://cwe.mitre.org/data/definitions/605.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b104_hardcoded_bind_all_interfaces.html
   Location: ./.venv/lib/python3.11/site-packages/uvicorn/server.py:212:19
211	            addr_format = "%s://%s:%d"
212	            host = "0.0.0.0" if config.host is None else config.host
213	            if ":" in host:

--------------------------------------------------
>> Issue: [B104:hardcoded_bind_all_interfaces] Possible binding to all interfaces.
   Severity: Medium   Confidence: Medium
   CWE: CWE-605 (https://cwe.mitre.org/data/definitions/605.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b104_hardcoded_bind_all_interfaces.html
   Location: ./tests/test_config_schema.py:181:17
180	            enabled=True,
181	            host="0.0.0.0",
182	            port=8000

--------------------------------------------------
>> Issue: [B108:hardcoded_tmp_directory] Probable insecure usage of temp file/directory.
   Severity: Medium   Confidence: Medium
   CWE: CWE-377 (https://cwe.mitre.org/data/definitions/377.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b108_hardcoded_tmp_directory.html
   Location: ./tests/test_sandbox.py:8:16
7	    command = "ls -la"
8	    workspace = "/tmp/fake_workspace"
9	    cwd = "/tmp/fake_workspace/subdir"

--------------------------------------------------
>> Issue: [B108:hardcoded_tmp_directory] Probable insecure usage of temp file/directory.
   Severity: Medium   Confidence: Medium
   CWE: CWE-377 (https://cwe.mitre.org/data/definitions/377.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b108_hardcoded_tmp_directory.html
   Location: ./tests/test_sandbox.py:9:10
8	    workspace = "/tmp/fake_workspace"
9	    cwd = "/tmp/fake_workspace/subdir"
10	    

--------------------------------------------------
>> Issue: [B108:hardcoded_tmp_directory] Probable insecure usage of temp file/directory.
   Severity: Medium   Confidence: Medium
   CWE: CWE-377 (https://cwe.mitre.org/data/definitions/377.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b108_hardcoded_tmp_directory.html
   Location: ./tests/test_sandbox.py:37:16
36	    command = "pwd"
37	    workspace = "/tmp/fake_workspace"
38	    # CWD yang mencoba kabur dari workspace

--------------------------------------------------
>> Issue: [B108:hardcoded_tmp_directory] Probable insecure usage of temp file/directory.
   Severity: Medium   Confidence: Medium
   CWE: CWE-377 (https://cwe.mitre.org/data/definitions/377.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b108_hardcoded_tmp_directory.html
   Location: ./tests/test_sandbox.py:39:10
38	    # CWD yang mencoba kabur dari workspace
39	    cwd = "/tmp/hack_the_system"
40	    

--------------------------------------------------
>> Issue: [B108:hardcoded_tmp_directory] Probable insecure usage of temp file/directory.
   Severity: Medium   Confidence: Medium
   CWE: CWE-377 (https://cwe.mitre.org/data/definitions/377.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b108_hardcoded_tmp_directory.html
   Location: ./tools/sandbox.py:47:19
46	        "--dev", "/dev",
47	        "--tmpfs", "/tmp",
48	        "--tmpfs", parent_dir,           # Sembunyikan parent directory
49	        "--dir", str(ws),                # Buat mount point workspace baru
50	        "--bind", str(ws), str(ws),      # Mount workspace RW
51	        "--chdir", sandbox_cwd,          # Atur working directory
52	        "--", "sh", "-c", command
53	    ]
54	
55	    return args

--------------------------------------------------

Code scanned:
	Total lines of code: 2108972
	Total lines skipped (#nosec): 5
	Total potential issues skipped due to specifically being disabled (e.g., #nosec BXXX): 21

Run metrics:
	Total issues (by severity):
		Undefined: 0
		Low: 6620
		Medium: 320
		High: 55
	Total issues (by confidence):
		Undefined: 0
		Low: 23
		Medium: 288
		High: 6684
Files skipped (0):
```

## 4. Static Analysis (semgrep)

```
```

## 5. Dependency Audit (pip-audit)

```
WARNING:pip_audit._dependency_source.pip:pip-audit will run pip against /home/sandi/.local/share/pipx/venvs/pip-audit/bin/python, but you have a virtual environment loaded at /home/sandi/PocketFlow/idolhub/.venv. This may result in unintuitive audits, since your local environment will not be audited. You can forcefully override this behavior by setting PIPAPI_PYTHON_LOCATION to the location of your virtual environment's Python interpreter.
No known vulnerabilities found
```

## 6. Vulnerability Check (safety)

```
/home/sandi/.local/share/pipx/venvs/safety/lib/python3.12/site-packages/safety/auth/main.py:5: AuthlibDeprecationWarning: authlib.jose module is deprecated, please use joserfc instead.
It will be compatible before version 2.0.0.
  from authlib.jose.errors import ExpiredTokenError


+===========================================================================================================================================================================================+


DEPRECATED: this command (`check`) has been DEPRECATED, and will be unsupported beyond 01 June 2024.


We highly encourage switching to the new `scan` command which is easier to use, more powerful, and can be set up to mimic the deprecated command if required.


+===========================================================================================================================================================================================+


{
    "report_meta": {
        "scan_target": "environment",
        "scanned": [
            "/home/sandi/.local/share/pipx/venvs/safety/lib/python3.12/site-packages",
            "/home/sandi/.local/share/pipx/shared/lib/python3.12/site-packages"
        ],
        "scanned_full_path": [
            "/home/sandi/.local/share/pipx/venvs/safety/lib/python3.12/site-packages",
            "/home/sandi/.local/share/pipx/shared/lib/python3.12/site-packages"
        ],
        "target_languages": [
            "python"
        ],
        "policy_file": null,
        "policy_file_source": "local",
        "audit_and_monitor": false,
        "api_key": false,
        "account": "",
        "local_database_path": null,
        "safety_version": "3.8.1",
        "timestamp": "2026-06-07 11:41:05",
        "packages_found": 41,
        "vulnerabilities_found": 0,
        "vulnerabilities_ignored": 0,
        "remediations_recommended": 0,
        "telemetry": {
            "safety_options": {
                "json": {
                    "--json": 1
                }
            },
            "safety_version": "3.8.1",
            "safety_source": "cli",
            "os_type": "Linux",
            "os_release": "6.8.0-124-generic",
            "os_description": "Linux-6.8.0-124-generic-x86_64-with-glibc2.39",
            "python_version": "3.12.3",
            "safety_command": "check"
        },
        "git": {
            "branch": "main",
            "tag": "",
            "commit": "eabf14e6846ec57814432661af06b78a27a8d9b0",
            "dirty": "True",
            "origin": "https://github.com/primit1v0/idolhub-bot.git"
        },
        "project": null,
        "json_version": "1.1",
        "remediations_attempted": 0,
        "remediations_completed": 0,
        "remediation_mode": "NON_INTERACTIVE"
    },
    "scanned_packages": {
        "typing_extensions": {
            "name": "typing_extensions",
            "version": "4.15.0",
            "requirements": [
                {
                    "raw": "typing_extensions==4.15.0",
                    "extras": [],
                    "marker": null,
                    "name": "typing_extensions",
                    "specifier": "==4.15.0",
                    "url": null,
                    "found": "/home/sandi/.local/share/pipx/venvs/safety/lib/python3.12/site-packages/typing_extensions-4.15.0.dist-info"
                }
            ]
        },
        "truststore": {
            "name": "truststore",
            "version": "0.10.4",
            "requirements": [
                {
                    "raw": "truststore==0.10.4",
                    "extras": [],
                    "marker": null,
                    "name": "truststore",
                    "specifier": "==0.10.4",
                    "url": null,
                    "found": "/home/sandi/.local/share/pipx/venvs/safety/lib/python3.12/site-packages/truststore-0.10.4.dist-info"
                }
            ]
        },
        "tqdm": {
            "name": "tqdm",
            "version": "4.68.1",
            "requirements": [
                {
                    "raw": "tqdm==4.68.1",
                    "extras": [],
                    "marker": null,
                    "name": "tqdm",
                    "specifier": "==4.68.1",
                    "url": null,
                    "found": "/home/sandi/.local/share/pipx/venvs/safety/lib/python3.12/site-packages/tqdm-4.68.1.dist-info"
                }
            ]
        },
        "tomlkit": {
            "name": "tomlkit",
            "version": "0.15.0",
            "requirements": [
                {
                    "raw": "tomlkit==0.15.0",
                    "extras": [],
                    "marker": null,
                    "name": "tomlkit",
                    "specifier": "==0.15.0",
                    "url": null,
                    "found": "/home/sandi/.local/share/pipx/venvs/safety/lib/python3.12/site-packages/tomlkit-0.15.0.dist-info"
                }
            ]
        },
        "tenacity": {
            "name": "tenacity",
            "version": "9.1.4",
            "requirements": [
                {
                    "raw": "tenacity==9.1.4",
                    "extras": [],
                    "marker": null,
                    "name": "tenacity",
                    "specifier": "==9.1.4",
                    "url": null,
                    "found": "/home/sandi/.local/share/pipx/venvs/safety/lib/python3.12/site-packages/tenacity-9.1.4.dist-info"
                }
            ]
        },
        "shellingham": {
            "name": "shellingham",
            "version": "1.5.4",
            "requirements": [
                {
                    "raw": "shellingham==1.5.4",
                    "extras": [],
                    "marker": null,
                    "name": "shellingham",
                    "specifier": "==1.5.4",
                    "url": null,
                    "found": "/home/sandi/.local/share/pipx/venvs/safety/lib/python3.12/site-packages/shellingham-1.5.4.dist-info"
                }
            ]
        },
        "ruamel.yaml": {
            "name": "ruamel.yaml",
            "version": "0.19.1",
            "requirements": [
                {
                    "raw": "ruamel.yaml==0.19.1",
                    "extras": [],
                    "marker": null,
                    "name": "ruamel.yaml",
                    "specifier": "==0.19.1",
                    "url": null,
                    "found": "/home/sandi/.local/share/pipx/venvs/safety/lib/python3.12/site-packages/ruamel_yaml-0.19.1.dist-info"
                }
            ]
        },
        "regex": {
            "name": "regex",
            "version": "2026.5.9",
            "requirements": [
                {
                    "raw": "regex==2026.5.9",
                    "extras": [],
                    "marker": null,
                    "name": "regex",
                    "specifier": "==2026.5.9",
                    "url": null,
                    "found": "/home/sandi/.local/share/pipx/venvs/safety/lib/python3.12/site-packages/regex-2026.5.9.dist-info"
                }
            ]
        },
        "Pygments": {
            "name": "Pygments",
            "version": "2.20.0",
            "requirements": [
                {
                    "raw": "Pygments==2.20.0",
                    "extras": [],
                    "marker": null,
                    "name": "Pygments",
                    "specifier": "==2.20.0",
                    "url": null,
                    "found": "/home/sandi/.local/share/pipx/venvs/safety/lib/python3.12/site-packages/pygments-2.20.0.dist-info"
                }
            ]
        },
        "pycparser": {
            "name": "pycparser",
            "version": "3.0",
            "requirements": [
                {
                    "raw": "pycparser==3.0",
                    "extras": [],
                    "marker": null,
                    "name": "pycparser",
                    "specifier": "==3.0",
                    "url": null,
                    "found": "/home/sandi/.local/share/pipx/venvs/safety/lib/python3.12/site-packages/pycparser-3.0.dist-info"
                }
            ]
        },
        "packaging": {
            "name": "packaging",
            "version": "26.2",
            "requirements": [
                {
                    "raw": "packaging==26.2",
                    "extras": [],
                    "marker": null,
                    "name": "packaging",
                    "specifier": "==26.2",
                    "url": null,
                    "found": "/home/sandi/.local/share/pipx/venvs/safety/lib/python3.12/site-packages/packaging-26.2.dist-info"
                }
            ]
        },
        "mdurl": {
            "name": "mdurl",
            "version": "0.1.2",
            "requirements": [
                {
                    "raw": "mdurl==0.1.2",
                    "extras": [],
                    "marker": null,
                    "name": "mdurl",
                    "specifier": "==0.1.2",
                    "url": null,
                    "found": "/home/sandi/.local/share/pipx/venvs/safety/lib/python3.12/site-packages/mdurl-0.1.2.dist-info"
                }
            ]
        },
        "marshmallow": {
            "name": "marshmallow",
            "version": "4.3.0",
            "requirements": [
                {
                    "raw": "marshmallow==4.3.0",
                    "extras": [],
                    "marker": null,
                    "name": "marshmallow",
                    "specifier": "==4.3.0",
                    "url": null,
                    "found": "/home/sandi/.local/share/pipx/venvs/safety/lib/python3.12/site-packages/marshmallow-4.3.0.dist-info"
                }
            ]
        },
        "MarkupSafe": {
            "name": "MarkupSafe",
            "version": "3.0.3",
            "requirements": [
                {
                    "raw": "MarkupSafe==3.0.3",
                    "extras": [],
                    "marker": null,
                    "name": "MarkupSafe",
                    "specifier": "==3.0.3",
                    "url": null,
                    "found": "/home/sandi/.local/share/pipx/venvs/safety/lib/python3.12/site-packages/markupsafe-3.0.3.dist-info"
                }
            ]
        },
        "joblib": {
            "name": "joblib",
            "version": "1.5.3",
            "requirements": [
                {
                    "raw": "joblib==1.5.3",
                    "extras": [],
                    "marker": null,
                    "name": "joblib",
                    "specifier": "==1.5.3",
                    "url": null,
                    "found": "/home/sandi/.local/share/pipx/venvs/safety/lib/python3.12/site-packages/joblib-1.5.3.dist-info"
                }
            ]
        },
        "idna": {
            "name": "idna",
            "version": "3.18",
            "requirements": [
                {
                    "raw": "idna==3.18",
                    "extras": [],
                    "marker": null,
                    "name": "idna",
                    "specifier": "==3.18",
                    "url": null,
                    "found": "/home/sandi/.local/share/pipx/venvs/safety/lib/python3.12/site-packages/idna-3.18.dist-info"
                }
            ]
        },
        "h11": {
            "name": "h11",
            "version": "0.16.0",
            "requirements": [
                {
                    "raw": "h11==0.16.0",
                    "extras": [],
                    "marker": null,
                    "name": "h11",
                    "specifier": "==0.16.0",
                    "url": null,
                    "found": "/home/sandi/.local/share/pipx/venvs/safety/lib/python3.12/site-packages/h11-0.16.0.dist-info"
                }
            ]
        },
        "filelock": {
            "name": "filelock",
            "version": "3.29.1",
            "requirements": [
                {
                    "raw": "filelock==3.29.1",
                    "extras": [],
                    "marker": null,
                    "name": "filelock",
                    "specifier": "==3.29.1",
                    "url": null,
                    "found": "/home/sandi/.local/share/pipx/venvs/safety/lib/python3.12/site-packages/filelock-3.29.1.dist-info"
                }
            ]
        },
        "click": {
            "name": "click",
            "version": "8.4.1",
            "requirements": [
                {
                    "raw": "click==8.4.1",
                    "extras": [],
                    "marker": null,
                    "name": "click",
                    "specifier": "==8.4.1",
                    "url": null,
                    "found": "/home/sandi/.local/share/pipx/venvs/safety/lib/python3.12/site-packages/click-8.4.1.dist-info"
                }
            ]
        },
        "certifi": {
            "name": "certifi",
            "version": "2026.5.20",
            "requirements": [
                {
                    "raw": "certifi==2026.5.20",
                    "extras": [],
                    "marker": null,
                    "name": "certifi",
                    "specifier": "==2026.5.20",
                    "url": null,
                    "found": "/home/sandi/.local/share/pipx/venvs/safety/lib/python3.12/site-packages/certifi-2026.5.20.dist-info"
                }
            ]
        },
        "annotated-types": {
            "name": "annotated-types",
            "version": "0.7.0",
            "requirements": [
                {
                    "raw": "annotated-types==0.7.0",
                    "extras": [],
                    "marker": null,
                    "name": "annotated-types",
                    "specifier": "==0.7.0",
                    "url": null,
                    "found": "/home/sandi/.local/share/pipx/venvs/safety/lib/python3.12/site-packages/annotated_types-0.7.0.dist-info"
                }
            ]
        },
        "annotated-doc": {
            "name": "annotated-doc",
            "version": "0.0.4",
            "requirements": [
                {
                    "raw": "annotated-doc==0.0.4",
                    "extras": [],
                    "marker": null,
                    "name": "annotated-doc",
                    "specifier": "==0.0.4",
                    "url": null,
                    "found": "/home/sandi/.local/share/pipx/venvs/safety/lib/python3.12/site-packages/annotated_doc-0.0.4.dist-info"
                }
            ]
        },
        "typing-inspection": {
            "name": "typing-inspection",
            "version": "0.4.2",
            "requirements": [
                {
                    "raw": "typing-inspection==0.4.2",
                    "extras": [],
                    "marker": null,
                    "name": "typing-inspection",
                    "specifier": "==0.4.2",
                    "url": null,
                    "found": "/home/sandi/.local/share/pipx/venvs/safety/lib/python3.12/site-packages/typing_inspection-0.4.2.dist-info"
                }
            ]
        },
        "pydantic_core": {
            "name": "pydantic_core",
            "version": "2.46.4",
            "requirements": [
                {
                    "raw": "pydantic_core==2.46.4",
                    "extras": [],
                    "marker": null,
                    "name": "pydantic_core",
                    "specifier": "==2.46.4",
                    "url": null,
                    "found": "/home/sandi/.local/share/pipx/venvs/safety/lib/python3.12/site-packages/pydantic_core-2.46.4.dist-info"
                }
            ]
        },
        "nltk": {
            "name": "nltk",
            "version": "3.9.4",
            "requirements": [
                {
                    "raw": "nltk==3.9.4",
                    "extras": [],
                    "marker": null,
                    "name": "nltk",
                    "specifier": "==3.9.4",
                    "url": null,
                    "found": "/home/sandi/.local/share/pipx/venvs/safety/lib/python3.12/site-packages/nltk-3.9.4.dist-info"
                }
            ]
        },
        "markdown-it-py": {
            "name": "markdown-it-py",
            "version": "4.2.0",
            "requirements": [
                {
                    "raw": "markdown-it-py==4.2.0",
                    "extras": [],
                    "marker": null,
                    "name": "markdown-it-py",
                    "specifier": "==4.2.0",
                    "url": null,
                    "found": "/home/sandi/.local/share/pipx/venvs/safety/lib/python3.12/site-packages/markdown_it_py-4.2.0.dist-info"
                }
            ]
        },
        "Jinja2": {
            "name": "Jinja2",
            "version": "3.1.6",
            "requirements": [
                {
                    "raw": "Jinja2==3.1.6",
                    "extras": [],
                    "marker": null,
                    "name": "Jinja2",
                    "specifier": "==3.1.6",
                    "url": null,
                    "found": "/home/sandi/.local/share/pipx/venvs/safety/lib/python3.12/site-packages/jinja2-3.1.6.dist-info"
                }
            ]
        },
        "httpcore": {
            "name": "httpcore",
            "version": "1.0.9",
            "requirements": [
                {
                    "raw": "httpcore==1.0.9",
                    "extras": [],
                    "marker": null,
                    "name": "httpcore",
                    "specifier": "==1.0.9",
                    "url": null,
                    "found": "/home/sandi/.local/share/pipx/venvs/safety/lib/python3.12/site-packages/httpcore-1.0.9.dist-info"
                }
            ]
        },
        "dparse": {
            "name": "dparse",
            "version": "0.6.4",
            "requirements": [
                {
                    "raw": "dparse==0.6.4",
                    "extras": [],
                    "marker": null,
                    "name": "dparse",
                    "specifier": "==0.6.4",
                    "url": null,
                    "found": "/home/sandi/.local/share/pipx/venvs/safety/lib/python3.12/site-packages/dparse-0.6.4.dist-info"
                }
            ]
        },
        "cffi": {
            "name": "cffi",
            "version": "2.0.0",
            "requirements": [
                {
                    "raw": "cffi==2.0.0",
                    "extras": [],
                    "marker": null,
                    "name": "cffi",
                    "specifier": "==2.0.0",
                    "url": null,
                    "found": "/home/sandi/.local/share/pipx/venvs/safety/lib/python3.12/site-packages/cffi-2.0.0.dist-info"
                }
            ]
        },
        "anyio": {
            "name": "anyio",
            "version": "4.13.0",
            "requirements": [
                {
                    "raw": "anyio==4.13.0",
                    "extras": [],
                    "marker": null,
                    "name": "anyio",
                    "specifier": "==4.13.0",
                    "url": null,
                    "found": "/home/sandi/.local/share/pipx/venvs/safety/lib/python3.12/site-packages/anyio-4.13.0.dist-info"
                }
            ]
        },
        "rich": {
            "name": "rich",
            "version": "15.0.0",
            "requirements": [
                {
                    "raw": "rich==15.0.0",
                    "extras": [],
                    "marker": null,
                    "name": "rich",
                    "specifier": "==15.0.0",
                    "url": null,
                    "found": "/home/sandi/.local/share/pipx/venvs/safety/lib/python3.12/site-packages/rich-15.0.0.dist-info"
                }
            ]
        },
        "pydantic": {
            "name": "pydantic",
            "version": "2.13.4",
            "requirements": [
                {
                    "raw": "pydantic==2.13.4",
                    "extras": [],
                    "marker": null,
                    "name": "pydantic",
                    "specifier": "==2.13.4",
                    "url": null,
                    "found": "/home/sandi/.local/share/pipx/venvs/safety/lib/python3.12/site-packages/pydantic-2.13.4.dist-info"
                }
            ]
        },
        "httpx": {
            "name": "httpx",
            "version": "0.28.1",
            "requirements": [
                {
                    "raw": "httpx==0.28.1",
                    "extras": [],
                    "marker": null,
                    "name": "httpx",
                    "specifier": "==0.28.1",
                    "url": null,
                    "found": "/home/sandi/.local/share/pipx/venvs/safety/lib/python3.12/site-packages/httpx-0.28.1.dist-info"
                }
            ]
        },
        "cryptography": {
            "name": "cryptography",
            "version": "48.0.0",
            "requirements": [
                {
                    "raw": "cryptography==48.0.0",
                    "extras": [],
                    "marker": null,
                    "name": "cryptography",
                    "specifier": "==48.0.0",
                    "url": null,
                    "found": "/home/sandi/.local/share/pipx/venvs/safety/lib/python3.12/site-packages/cryptography-48.0.0.dist-info"
                }
            ]
        },
        "typer": {
            "name": "typer",
            "version": "0.25.1",
            "requirements": [
                {
                    "raw": "typer==0.25.1",
                    "extras": [],
                    "marker": null,
                    "name": "typer",
                    "specifier": "==0.25.1",
                    "url": null,
                    "found": "/home/sandi/.local/share/pipx/venvs/safety/lib/python3.12/site-packages/typer-0.25.1.dist-info"
                }
            ]
        },
        "safety-schemas": {
            "name": "safety-schemas",
            "version": "0.0.16",
            "requirements": [
                {
                    "raw": "safety-schemas==0.0.16",
                    "extras": [],
                    "marker": null,
                    "name": "safety-schemas",
                    "specifier": "==0.0.16",
                    "url": null,
                    "found": "/home/sandi/.local/share/pipx/venvs/safety/lib/python3.12/site-packages/safety_schemas-0.0.16.dist-info"
                }
            ]
        },
        "joserfc": {
            "name": "joserfc",
            "version": "1.7.0",
            "requirements": [
                {
                    "raw": "joserfc==1.7.0",
                    "extras": [],
                    "marker": null,
                    "name": "joserfc",
                    "specifier": "==1.7.0",
                    "url": null,
                    "found": "/home/sandi/.local/share/pipx/venvs/safety/lib/python3.12/site-packages/joserfc-1.7.0.dist-info"
                }
            ]
        },
        "Authlib": {
            "name": "Authlib",
            "version": "1.7.2",
            "requirements": [
                {
                    "raw": "Authlib==1.7.2",
                    "extras": [],
                    "marker": null,
                    "name": "Authlib",
                    "specifier": "==1.7.2",
                    "url": null,
                    "found": "/home/sandi/.local/share/pipx/venvs/safety/lib/python3.12/site-packages/authlib-1.7.2.dist-info"
                }
            ]
        },
        "safety": {
            "name": "safety",
            "version": "3.8.1",
            "requirements": [
                {
                    "raw": "safety==3.8.1",
                    "extras": [],
                    "marker": null,
                    "name": "safety",
                    "specifier": "==3.8.1",
                    "url": null,
                    "found": "/home/sandi/.local/share/pipx/venvs/safety/lib/python3.12/site-packages/safety-3.8.1.dist-info"
                }
            ]
        },
        "pip": {
            "name": "pip",
            "version": "26.1.2",
            "requirements": [
                {
                    "raw": "pip==26.1.2",
                    "extras": [],
                    "marker": null,
                    "name": "pip",
                    "specifier": "==26.1.2",
                    "url": null,
                    "found": "/home/sandi/.local/share/pipx/shared/lib/python3.12/site-packages/pip-26.1.2.dist-info"
                }
            ]
        }
    },
    "affected_packages": {},
    "announcements": [],
    "vulnerabilities": [],
    "ignored_vulnerabilities": [],
    "remediations": {},
    "remediations_results": {
        "vulnerabilities_fixed": [],
        "remediations_applied": {},
        "remediations_skipped": {}
    }
}


+===========================================================================================================================================================================================+


DEPRECATED: this command (`check`) has been DEPRECATED, and will be unsupported beyond 01 June 2024.


We highly encourage switching to the new `scan` command which is easier to use, more powerful, and can be set up to mimic the deprecated command if required.


+===========================================================================================================================================================================================+


```

---

## Summary

| Tool | Status |
|------|--------|
| pytest | ❌ FAILED |
| ruff | ❌ FAILED |
| bandit | ❌ FAILED |
| semgrep | ✅ PASSED |
| pip-audit | ✅ PASSED |
| safety | ✅ PASSED |

**Report saved to:** `hasilaudit.md`
