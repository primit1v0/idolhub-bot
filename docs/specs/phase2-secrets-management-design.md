# Phase 2: Secrets Management - Technical Design

**Status**: 📋 Planned  
**Priority**: Critical  
**Dependencies**: Phase 1 Complete ✅  
**Estimated Duration**: 2-3 weeks  
**Estimated Tests**: +15 tests (128 total)

---

## 🎯 Objectives

### Primary Goals

1. **Remove secrets from config.json**
   - Move all API keys, tokens, passwords to secure backend
   - Keep only secret references in config
   - Maintain backward compatibility with environment variables

2. **Implement secrets backend**
   - Support HashiCorp Vault OR AWS Secrets Manager
   - Fallback to environment variables
   - Hot-reload secrets without restart

3. **Add secrets rotation**
   - Automatic rotation capability
   - Zero-downtime rotation
   - Audit logging for all operations

4. **Enhance security**
   - Encrypt secrets at rest
   - Encrypt secrets in transit
   - Implement access control
   - Add audit logging

### Success Criteria

- [ ] Zero secrets in config.json
- [ ] All secrets in secure backend
- [ ] Rotation works without downtime
- [ ] Audit logs capture all access
- [ ] All tests pass (128+ expected)
- [ ] Documentation complete
- [ ] Backward compatible with env vars

---

## 🏗️ Architecture Design

### Component Overview

```
┌─────────────────────────────────────────────────────────┐
│                     Application                          │
├─────────────────────────────────────────────────────────┤
│  core/secrets.py (SecretsManager)                       │
│    ├── get_secret(key) → str                            │
│    ├── set_secret(key, value) → None                    │
│    ├── rotate_secret(key) → None                        │
│    └── audit_log(action, key) → None                    │
├─────────────────────────────────────────────────────────┤
│  Backends (pluggable)                                    │
│    ├── VaultBackend (HashiCorp Vault)                   │
│    ├── AWSSecretsBackend (AWS Secrets Manager)          │
│    └── EnvBackend (Environment Variables - fallback)    │
├─────────────────────────────────────────────────────────┤
│  core/config_validator.py (updated)                     │
│    └── resolve_secrets(data) → data with resolved refs  │
└─────────────────────────────────────────────────────────┘
```

### Secret Reference Format

```json
{
  "telegram": {
    "token": "secret://telegram/bot_token"
  },
  "providers": {
    "openai": {
      "api_key": "secret://openai/api_key"
    }
  }
}
```

**Supported Prefixes**:
- `secret://` - Use configured secrets backend
- `vault://` - Explicitly use Vault
- `aws://` - Explicitly use AWS Secrets Manager
- `env://` - Explicitly use environment variable
- `$VAR` - Legacy env var syntax (backward compatible)

---

## 📁 File Structure

### New Files

```
core/
├── secrets.py                    # Main secrets manager
├── secrets_backends/
│   ├── __init__.py
│   ├── base.py                   # Abstract base class
│   ├── vault.py                  # HashiCorp Vault backend
│   ├── aws.py                    # AWS Secrets Manager backend
│   └── env.py                    # Environment variable backend

tests/
├── test_secrets.py               # Secrets manager tests
├── test_secrets_vault.py         # Vault backend tests
├── test_secrets_aws.py           # AWS backend tests
└── test_secrets_env.py           # Env backend tests

docs/
├── SECRETS_SETUP.md              # Setup guide
└── specs/
    └── phase2-secrets-management-design.md  # This file
```

### Modified Files

```
core/
├── config_validator.py           # Add resolve_secrets()
└── config_schema.py              # Add SecretsSection

config.example.json               # Update with secret references
README.md                         # Add secrets setup section
```

---

## 🔧 Implementation Plan

### Step 1: Create Base Infrastructure (Week 1, Days 1-2)

**Files to create**:
1. `core/secrets_backends/base.py`
2. `core/secrets_backends/__init__.py`

**Base Backend Interface**:
```python
from abc import ABC, abstractmethod
from typing import Optional

class SecretsBackend(ABC):
    """Abstract base class for secrets backends."""
    
    @abstractmethod
    def get_secret(self, key: str) -> str:
        """Retrieve a secret by key."""
        pass
    
    @abstractmethod
    def set_secret(self, key: str, value: str) -> None:
        """Store a secret."""
        pass
    
    @abstractmethod
    def delete_secret(self, key: str) -> None:
        """Delete a secret."""
        pass
    
    @abstractmethod
    def list_secrets(self) -> list[str]:
        """List all secret keys."""
        pass
    
    @abstractmethod
    def rotate_secret(self, key: str, new_value: str) -> None:
        """Rotate a secret to a new value."""
        pass
    
    @abstractmethod
    def health_check(self) -> bool:
        """Check if backend is accessible."""
        pass
```

**Tests to create**: `tests/test_secrets_base.py`

### Step 2: Implement Environment Backend (Week 1, Days 3-4)

**File to create**: `core/secrets_backends/env.py`

**Implementation**:
```python
import os
from .base import SecretsBackend

class EnvBackend(SecretsBackend):
    """Environment variable backend (fallback)."""
    
    def get_secret(self, key: str) -> str:
        value = os.getenv(key)
        if value is None:
            raise KeyError(f"Environment variable {key} not found")
        return value
    
    def set_secret(self, key: str, value: str) -> None:
        os.environ[key] = value
    
    def delete_secret(self, key: str) -> None:
        os.environ.pop(key, None)
    
    def list_secrets(self) -> list[str]:
        return list(os.environ.keys())
    
    def rotate_secret(self, key: str, new_value: str) -> None:
        self.set_secret(key, new_value)
    
    def health_check(self) -> bool:
        return True
```

**Tests to create**: `tests/test_secrets_env.py`

### Step 3: Implement Vault Backend (Week 1, Days 5-7)

**File to create**: `core/secrets_backends/vault.py`

**Dependencies**: `hvac` (HashiCorp Vault client)

**Implementation**:
```python
import hvac
from .base import SecretsBackend

class VaultBackend(SecretsBackend):
    """HashiCorp Vault backend."""
    
    def __init__(self, url: str, token: str, mount_point: str = "secret"):
        self.client = hvac.Client(url=url, token=token)
        self.mount_point = mount_point
        
        if not self.client.is_authenticated():
            raise ValueError("Vault authentication failed")
    
    def get_secret(self, key: str) -> str:
        path = f"{self.mount_point}/data/{key}"
        response = self.client.secrets.kv.v2.read_secret_version(path=key)
        return response["data"]["data"]["value"]
    
    def set_secret(self, key: str, value: str) -> None:
        self.client.secrets.kv.v2.create_or_update_secret(
            path=key,
            secret={"value": value}
        )
    
    def delete_secret(self, key: str) -> None:
        self.client.secrets.kv.v2.delete_metadata_and_all_versions(path=key)
    
    def list_secrets(self) -> list[str]:
        response = self.client.secrets.kv.v2.list_secrets(path="")
        return response["data"]["keys"]
    
    def rotate_secret(self, key: str, new_value: str) -> None:
        # Vault KV v2 automatically versions secrets
        self.set_secret(key, new_value)
    
    def health_check(self) -> bool:
        return self.client.sys.is_initialized() and self.client.is_authenticated()
```

**Tests to create**: `tests/test_secrets_vault.py`

### Step 4: Implement AWS Backend (Week 2, Days 1-3)

**File to create**: `core/secrets_backends/aws.py`

**Dependencies**: `boto3` (AWS SDK)

**Implementation**:
```python
import boto3
from botocore.exceptions import ClientError
from .base import SecretsBackend

class AWSSecretsBackend(SecretsBackend):
    """AWS Secrets Manager backend."""
    
    def __init__(self, region_name: str = "us-east-1"):
        self.client = boto3.client("secretsmanager", region_name=region_name)
    
    def get_secret(self, key: str) -> str:
        try:
            response = self.client.get_secret_value(SecretId=key)
            return response["SecretString"]
        except ClientError as e:
            raise KeyError(f"Secret {key} not found: {e}")
    
    def set_secret(self, key: str, value: str) -> None:
        try:
            self.client.create_secret(Name=key, SecretString=value)
        except ClientError:
            self.client.update_secret(SecretId=key, SecretString=value)
    
    def delete_secret(self, key: str) -> None:
        self.client.delete_secret(SecretId=key, ForceDeleteWithoutRecovery=True)
    
    def list_secrets(self) -> list[str]:
        response = self.client.list_secrets()
        return [s["Name"] for s in response["SecretList"]]
    
    def rotate_secret(self, key: str, new_value: str) -> None:
        self.client.rotate_secret(SecretId=key)
        self.set_secret(key, new_value)
    
    def health_check(self) -> bool:
        try:
            self.client.list_secrets(MaxResults=1)
            return True
        except ClientError:
            return False
```

**Tests to create**: `tests/test_secrets_aws.py`

### Step 5: Create Secrets Manager (Week 2, Days 4-5)

**File to create**: `core/secrets.py`

**Implementation**:
```python
import logging
from typing import Optional
from datetime import datetime
from .secrets_backends.base import SecretsBackend
from .secrets_backends.env import EnvBackend
from .secrets_backends.vault import VaultBackend
from .secrets_backends.aws import AWSSecretsBackend

logger = logging.getLogger(__name__)

class SecretsManager:
    """Unified secrets management interface."""
    
    def __init__(self, backend: SecretsBackend, audit_log_path: Optional[str] = None):
        self.backend = backend
        self.audit_log_path = audit_log_path
    
    def get_secret(self, key: str) -> str:
        """Retrieve a secret."""
        self._audit_log("GET", key)
        return self.backend.get_secret(key)
    
    def set_secret(self, key: str, value: str) -> None:
        """Store a secret."""
        self._audit_log("SET", key)
        self.backend.set_secret(key, value)
    
    def delete_secret(self, key: str) -> None:
        """Delete a secret."""
        self._audit_log("DELETE", key)
        self.backend.delete_secret(key)
    
    def rotate_secret(self, key: str, new_value: str) -> None:
        """Rotate a secret."""
        self._audit_log("ROTATE", key)
        self.backend.rotate_secret(key, new_value)
    
    def health_check(self) -> bool:
        """Check backend health."""
        return self.backend.health_check()
    
    def _audit_log(self, action: str, key: str) -> None:
        """Log secret access for audit."""
        timestamp = datetime.utcnow().isoformat()
        log_entry = f"{timestamp} - {action} - {key}"
        
        logger.info(log_entry)
        
        if self.audit_log_path:
            with open(self.audit_log_path, "a") as f:
                f.write(log_entry + "\n")

def create_secrets_manager(config: dict) -> SecretsManager:
    """Factory function to create secrets manager from config."""
    backend_type = config.get("secrets", {}).get("backend", "env")
    
    if backend_type == "vault":
        backend = VaultBackend(
            url=config["secrets"]["vault_url"],
            token=config["secrets"]["vault_token"]
        )
    elif backend_type == "aws":
        backend = AWSSecretsBackend(
            region_name=config["secrets"].get("aws_region", "us-east-1")
        )
    else:
        backend = EnvBackend()
    
    return SecretsManager(
        backend=backend,
        audit_log_path=config.get("secrets", {}).get("audit_log_path")
    )
```

**Tests to create**: `tests/test_secrets.py`

### Step 6: Update Config Validator (Week 2, Days 6-7)

**File to modify**: `core/config_validator.py`

**Add function**:
```python
def resolve_secrets(data: Any, secrets_manager: SecretsManager) -> Any:
    """
    Resolve secret references in configuration.
    
    Supports:
    - secret://path/to/secret
    - vault://path/to/secret
    - aws://secret-name
    - env://VARIABLE_NAME
    - $VARIABLE_NAME (legacy)
    """
    if isinstance(data, dict):
        return {k: resolve_secrets(v, secrets_manager) for k, v in data.items()}
    elif isinstance(data, list):
        return [resolve_secrets(item, secrets_manager) for item in data]
    elif isinstance(data, str):
        if data.startswith("secret://"):
            key = data.replace("secret://", "")
            return secrets_manager.get_secret(key)
        elif data.startswith("vault://"):
            key = data.replace("vault://", "")
            return secrets_manager.get_secret(key)
        elif data.startswith("aws://"):
            key = data.replace("aws://", "")
            return secrets_manager.get_secret(key)
        elif data.startswith("env://"):
            key = data.replace("env://", "")
            return os.getenv(key)
        elif data.startswith("$"):
            return resolve_env(data)  # Legacy support
        return data
    return data
```

**Update load_config**:
```python
def load_config(path: str = "config.json") -> AppConfig:
    # ... existing code ...
    
    # Resolve environment variables (legacy)
    resolved_data = _resolve_dict(raw_data)
    
    # Resolve secrets (new)
    secrets_manager = create_secrets_manager(resolved_data)
    resolved_data = resolve_secrets(resolved_data, secrets_manager)
    
    # Validate with Pydantic
    config = AppConfig(**resolved_data)
    
    return config
```

### Step 7: Update Config Schema (Week 3, Day 1)

**File to modify**: `core/config_schema.py`

**Add section**:
```python
class SecretsSection(BaseModel):
    """Secrets management configuration."""
    
    backend: Literal["env", "vault", "aws"] = Field(
        default="env",
        description="Secrets backend to use"
    )
    
    vault_url: Optional[str] = Field(
        default=None,
        description="HashiCorp Vault URL (required if backend=vault)"
    )
    
    vault_token: Optional[str] = Field(
        default=None,
        description="HashiCorp Vault token (required if backend=vault)"
    )
    
    aws_region: Optional[str] = Field(
        default="us-east-1",
        description="AWS region for Secrets Manager"
    )
    
    audit_log_path: Optional[str] = Field(
        default="./data/secrets_audit.log",
        description="Path to secrets audit log"
    )
    
    @model_validator(mode="after")
    def validate_backend_config(self) -> "SecretsSection":
        if self.backend == "vault":
            if not self.vault_url or not self.vault_token:
                raise ValueError("vault_url and vault_token required for vault backend")
        return self

class AppConfig(BaseModel):
    # ... existing fields ...
    secrets: SecretsSection = Field(default_factory=SecretsSection)
```

### Step 8: Documentation (Week 3, Days 2-3)

**Files to create/update**:

1. `docs/SECRETS_SETUP.md` - Complete setup guide
2. `config.example.json` - Update with secret references
3. `README.md` - Add secrets section
4. `PHASE2_COMPLETION.md` - Completion report (after done)

### Step 9: Testing (Week 3, Days 4-5)

**Test Coverage Required**:
- Unit tests for each backend
- Integration tests for secrets manager
- Config validation tests
- Rotation tests
- Audit logging tests
- Backward compatibility tests

**Minimum 15 new tests**:
- `test_secrets_env.py`: 3 tests
- `test_secrets_vault.py`: 4 tests
- `test_secrets_aws.py`: 4 tests
- `test_secrets.py`: 4 tests

---

## 🔒 Security Considerations

### Encryption

1. **At Rest**: Secrets backend handles encryption
2. **In Transit**: Use HTTPS for all backend communication
3. **In Memory**: Clear secrets from memory after use

### Access Control

1. **Backend Level**: Use backend's native access control
2. **Application Level**: Audit all secret access
3. **Principle of Least Privilege**: Only access needed secrets

### Audit Logging

**Log Format**:
```
2026-06-07T05:00:00Z - GET - telegram/bot_token - SUCCESS
2026-06-07T05:00:01Z - ROTATE - openai/api_key - SUCCESS
2026-06-07T05:00:02Z - GET - invalid/key - FAILED - KeyError
```

**What to Log**:
- Timestamp (UTC)
- Action (GET, SET, DELETE, ROTATE)
- Secret key (not value!)
- Result (SUCCESS/FAILED)
- Error message (if failed)

---

## 🧪 Testing Strategy

### Unit Tests

```python
# tests/test_secrets_env.py
def test_env_backend_get_secret(monkeypatch):
    monkeypatch.setenv("TEST_SECRET", "test_value")
    backend = EnvBackend()
    assert backend.get_secret("TEST_SECRET") == "test_value"

def test_env_backend_missing_secret():
    backend = EnvBackend()
    with pytest.raises(KeyError):
        backend.get_secret("NONEXISTENT")
```

### Integration Tests

```python
# tests/test_secrets.py
def test_secrets_manager_with_env_backend(tmp_path):
    audit_log = tmp_path / "audit.log"
    backend = EnvBackend()
    manager = SecretsManager(backend, str(audit_log))
    
    os.environ["TEST_KEY"] = "test_value"
    value = manager.get_secret("TEST_KEY")
    
    assert value == "test_value"
    assert audit_log.exists()
    assert "GET - TEST_KEY" in audit_log.read_text()
```

### Validation Tests

```python
# tests/test_config_validator.py
def test_resolve_secrets_with_secret_prefix():
    data = {"api_key": "secret://openai/key"}
    manager = Mock()
    manager.get_secret.return_value = "sk-test123"
    
    result = resolve_secrets(data, manager)
    
    assert result["api_key"] == "sk-test123"
    manager.get_secret.assert_called_once_with("openai/key")
```

---

## 📋 Migration Guide

### For Users

**Before (Phase 1)**:
```json
{
  "telegram": {
    "token": "$TELEGRAM_BOT_TOKEN"
  },
  "providers": {
    "openai": {
      "api_key": "$OPENAI_API_KEY"
    }
  }
}
```

**After (Phase 2)**:
```json
{
  "secrets": {
    "backend": "vault",
    "vault_url": "https://vault.example.com",
    "vault_token": "$VAULT_TOKEN"
  },
  "telegram": {
    "token": "secret://telegram/bot_token"
  },
  "providers": {
    "openai": {
      "api_key": "secret://openai/api_key"
    }
  }
}
```

**Migration Steps**:
1. Set up secrets backend (Vault or AWS)
2. Store secrets in backend
3. Update config.json with secret references
4. Test with `python -c "from core.config_validator import load_config; load_config()"`
5. Restart application

---

## ✅ Acceptance Criteria

### Functional Requirements

- [ ] EnvBackend works with environment variables
- [ ] VaultBackend works with HashiCorp Vault
- [ ] AWSSecretsBackend works with AWS Secrets Manager
- [ ] SecretsManager provides unified interface
- [ ] Config validator resolves secret references
- [ ] Audit logging captures all operations
- [ ] Rotation works without downtime
- [ ] Backward compatible with $VAR syntax

### Non-Functional Requirements

- [ ] All tests pass (128+ total)
- [ ] Test coverage ≥ 95%
- [ ] Documentation complete
- [ ] No secrets in config.json
- [ ] No secrets in code
- [ ] No secrets in logs (except audit log)
- [ ] Performance impact < 100ms per secret

### Security Requirements

- [ ] Secrets encrypted at rest
- [ ] Secrets encrypted in transit
- [ ] Audit log immutable
- [ ] Access control enforced
- [ ] No secrets in error messages
- [ ] No secrets in stack traces

---

## 🚀 Deployment Checklist

### Pre-Deployment

- [ ] All tests pass
- [ ] Audit tools pass
- [ ] Documentation reviewed
- [ ] Migration guide tested
- [ ] Rollback plan prepared

### Deployment

- [ ] Set up secrets backend
- [ ] Migrate secrets to backend
- [ ] Update config.json
- [ ] Deploy new code
- [ ] Verify health checks
- [ ] Monitor audit logs

### Post-Deployment

- [ ] Verify all secrets resolved
- [ ] Check audit logs
- [ ] Test rotation
- [ ] Monitor performance
- [ ] Update documentation

---

## 📞 Support & Troubleshooting

### Common Issues

**Issue**: Secret not found
```
KeyError: Secret 'openai/api_key' not found
```
**Solution**: Verify secret exists in backend and path is correct

**Issue**: Backend authentication failed
```
ValueError: Vault authentication failed
```
**Solution**: Check vault_token is valid and has correct permissions

**Issue**: Audit log not created
```
FileNotFoundError: [Errno 2] No such file or directory: './data/secrets_audit.log'
```
**Solution**: Create data/ directory or update audit_log_path

---

**Last Updated**: 2026-06-07  
**Author**: Bob Shell (AI Assistant)  
**Status**: Ready for Implementation
