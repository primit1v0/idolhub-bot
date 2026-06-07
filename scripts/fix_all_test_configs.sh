#!/bin/bash
# Fix all inline test configs to pass Pydantic validation

cd /home/sandi/PocketFlow/idolhub

# Fix all empty long_term paths in remaining test files
find tests/ -name "*.py" -type f -exec sed -i 's/"long_term": {"backend": "none", "path": ""}/"long_term": {"backend": "none", "path": ".\/data\/vectors.db"}/g' {} \;

# Add missing plugins field after tools field
find tests/ -name "*.py" -type f -exec sed -i 's/"tools": {"dir": ".\/tools"},/"tools": {"dir": ".\/tools"},\n        "plugins": {"dir": ".\/plugins"},/g' {} \;

# Add missing api field after plugins field  
find tests/ -name "*.py" -type f -exec sed -i 's/"plugins": {"dir": ".\/plugins"},/"plugins": {"dir": ".\/plugins"},\n        "api": {"enabled": False},/g' {} \;

echo "✅ Fixed all test config validation issues"
