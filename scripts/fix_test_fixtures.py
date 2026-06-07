#!/usr/bin/env python3
"""
Script to automatically fix test files to use valid_test_config_data fixture.
Replaces inline AppConfig.model_validate() calls with fixture usage.
"""

import re
from pathlib import Path


def fix_test_file(file_path: Path) -> tuple[int, int]:
    """
    Fix a single test file to use valid_test_config_data fixture.
    
    Returns:
        tuple: (functions_fixed, lines_removed)
    """
    content = file_path.read_text()
    original_lines = len(content.splitlines())
    
    # Pattern to match test function signatures
    func_pattern = r'(@pytest\.mark\.asyncio\s+)?async def (test_\w+)\(([^)]*)\):'
    
    # Pattern to match inline config creation
    config_pattern = r'cfg = AppConfig\.model_validate\(\{[^}]+\}\)'
    
    functions_fixed = 0
    
    # Find all test functions
    for match in re.finditer(func_pattern, content):
        func_name = match.group(2)
        params = match.group(3)
        
        # Check if function already has valid_test_config_data
        if 'valid_test_config_data' in params:
            continue
            
        # Check if function has inline config
        func_start = match.start()
        # Find next function or end of file
        next_match = re.search(func_pattern, content[func_start + 10:])
        if next_match:
            func_end = func_start + 10 + next_match.start()
        else:
            func_end = len(content)
        
        func_body = content[func_start:func_end]
        
        # Check if this function has inline config
        if 'AppConfig.model_validate({' not in func_body:
            continue
        
        # Add fixture to parameters
        if params:
            new_params = f"{params}, valid_test_config_data"
        else:
            new_params = "valid_test_config_data"
        
        # Replace function signature
        old_sig = match.group(0)
        new_sig = old_sig.replace(f"({params}):", f"({new_params}):")
        content = content.replace(old_sig, new_sig, 1)
        
        # Find and replace the config creation in this function
        config_match = re.search(
            r'cfg = AppConfig\.model_validate\(\{.*?\}\)',
            func_body,
            re.DOTALL
        )
        
        if config_match:
            old_config = config_match.group(0)
            
            # Extract agent config if present
            agent_match = re.search(r'"agent":\s*\{([^}]+)\}', old_config)
            if agent_match:
                new_config = f'''config_data = valid_test_config_data.copy()
    config_data["agent"] = {{{agent_match.group(1)}}}
    cfg = AppConfig.model_validate(config_data)'''
            else:
                new_config = '''config_data = valid_test_config_data.copy()
    cfg = AppConfig.model_validate(config_data)'''
            
            content = content.replace(old_config, new_config, 1)
            functions_fixed += 1
    
    # Write back
    file_path.write_text(content)
    new_lines = len(content.splitlines())
    
    return functions_fixed, original_lines - new_lines


def main():
    """Fix all test files in the tests directory."""
    tests_dir = Path(__file__).parent.parent / "tests"
    
    test_files = [
        "test_agent.py",
        "test_api.py",
        "test_api_server.py",
        "test_llm.py",
        "test_mcp.py",
    ]
    
    total_fixed = 0
    total_lines_removed = 0
    
    for test_file in test_files:
        file_path = tests_dir / test_file
        if not file_path.exists():
            print(f"⚠️  {test_file} not found")
            continue
        
        fixed, lines_removed = fix_test_file(file_path)
        total_fixed += fixed
        total_lines_removed += lines_removed
        
        if fixed > 0:
            print(f"✅ {test_file}: {fixed} functions fixed, {lines_removed} lines removed")
        else:
            print(f"⏭️  {test_file}: already using fixtures")
    
    print(f"\n📊 Total: {total_fixed} functions fixed, {total_lines_removed} lines removed")


if __name__ == "__main__":
    main()
