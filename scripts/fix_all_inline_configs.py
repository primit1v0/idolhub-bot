#!/usr/bin/env python3
"""
Systematically fix all inline AppConfig.model_validate() calls in test files.
Replaces them with valid_test_config_data fixture usage.
"""

import re
from pathlib import Path


def fix_inline_config(content: str) -> str:
    """
    Replace inline AppConfig.model_validate({...}) with fixture usage.
    Handles multi-line config dictionaries.
    """
    # Pattern to match AppConfig.model_validate with multi-line dict
    pattern = r'AppConfig\.model_validate\(\{[^}]*(?:\{[^}]*\}[^}]*)*\}\)'
    
    def replace_config(match):
        config_str = match.group(0)
        
        # Extract agent config if present
        agent_match = re.search(r'"agent":\s*\{([^}]+)\}', config_str)
        
        if agent_match:
            agent_content = agent_match.group(1)
            return f'''config_data = valid_test_config_data.copy()
    config_data["agent"] = {{{agent_content}}}
    cfg = AppConfig.model_validate(config_data)'''
        else:
            return '''config_data = valid_test_config_data.copy()
    cfg = AppConfig.model_validate(config_data)'''
    
    # Replace all occurrences
    result = re.sub(pattern, replace_config, content, flags=re.DOTALL)
    return result


def add_fixture_param(content: str) -> str:
    """Add valid_test_config_data parameter to test functions that need it."""
    
    # Find test functions that use cfg = AppConfig or config_data
    pattern = r'(async def test_\w+)\(([^)]*)\):'
    
    def add_param(match):
        func_def = match.group(1)
        params = match.group(2)
        
        # Check if function body uses config_data or cfg
        # Look ahead to see if this function needs the fixture
        if 'valid_test_config_data' in params:
            return match.group(0)  # Already has it
        
        # Add fixture parameter
        if params:
            new_params = f"{params}, valid_test_config_data"
        else:
            new_params = "valid_test_config_data"
        
        return f"{func_def}({new_params}):"
    
    # Only add to functions that will use config_data
    lines = content.split('\n')
    result_lines = []
    i = 0
    
    while i < len(lines):
        line = lines[i]
        
        # Check if this is a test function definition
        if 'async def test_' in line and '(' in line:
            # Look ahead to see if function uses config_data
            func_end = i + 50  # Look ahead 50 lines
            uses_config = any('config_data' in lines[j] or 'cfg = AppConfig' in lines[j] 
                            for j in range(i, min(func_end, len(lines))))
            
            if uses_config and 'valid_test_config_data' not in line:
                # Add the fixture parameter
                match = re.match(r'(async def test_\w+)\(([^)]*)\):', line)
                if match:
                    func_def = match.group(1)
                    params = match.group(2)
                    if params:
                        line = f"{func_def}({params}, valid_test_config_data):"
                    else:
                        line = f"{func_def}(valid_test_config_data):"
        
        result_lines.append(line)
        i += 1
    
    return '\n'.join(result_lines)


def process_file(file_path: Path) -> tuple[bool, str]:
    """
    Process a single test file.
    Returns: (modified, message)
    """
    try:
        content = file_path.read_text()
        original = content
        
        # Fix inline configs
        content = fix_inline_config(content)
        
        # Add fixture parameters where needed
        content = add_fixture_param(content)
        
        if content != original:
            file_path.write_text(content)
            return True, f"✅ Fixed {file_path.name}"
        else:
            return False, f"⏭️  {file_path.name} - no changes needed"
    
    except Exception as e:
        return False, f"❌ {file_path.name} - error: {e}"


def main():
    """Process all test files."""
    tests_dir = Path(__file__).parent.parent / "tests"
    
    # Files that need fixing (have inline configs)
    test_files = [
        "test_agent.py",
        "test_config.py", 
        "test_llm.py",
        "test_main.py",
        "test_mcp.py",
        "test_memory.py",
    ]
    
    total_fixed = 0
    
    for test_file in test_files:
        file_path = tests_dir / test_file
        if not file_path.exists():
            print(f"⚠️  {test_file} not found")
            continue
        
        modified, message = process_file(file_path)
        print(message)
        if modified:
            total_fixed += 1
    
    print(f"\n📊 Total files modified: {total_fixed}")


if __name__ == "__main__":
    main()
