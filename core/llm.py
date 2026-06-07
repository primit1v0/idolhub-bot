from openai import AsyncOpenAI

from core.config import AppConfig


def get_llm_client(cfg: AppConfig) -> AsyncOpenAI:
    """
    Mengembalikan instance OpenAI-compatible client berdasarkan provider yang dipilih di config.
    Credentials diambil dari cfg.providers[provider].
    """
    provider_name = cfg.llm.provider
    
    if provider_name not in cfg.providers:
        raise ValueError(f"Provider '{provider_name}' tidak ditemukan di konfigurasi 'providers'")
        
    provider_cfg = cfg.providers[provider_name]
    
    base_url = provider_cfg.base_url
    api_key = None
    
    # Resolve API Key based on provider type
    if provider_name == "openai":
        api_key = provider_cfg.api_key
    elif provider_name == "openai_codex":
        api_key = provider_cfg.oauth_token
    elif provider_name == "github_copilot":
        api_key = provider_cfg.cli_token
    else:
        # Fallback for custom providers using generic api_key
        api_key = provider_cfg.api_key
        
    if not api_key:
        raise ValueError(f"Tidak ada API Key / Token yang valid untuk provider '{provider_name}'")

    return AsyncOpenAI(
        base_url=base_url,
        api_key=api_key,
        timeout=cfg.llm.timeout,
        max_retries=2
    )

async def call_llm(cfg: AppConfig, messages: list, tools: list = None):
    """
    Helper function untuk memanggil LLM secara asinkron dengan menginjeksi system prompt dari agent config.
    """
    client = get_llm_client(cfg)
    
    full_messages = [
        {"role": "system", "content": cfg.agent.system_prompt},
        *messages
    ]
    
    import re
    
    kwargs = {
        "model": cfg.llm.model,
        "messages": full_messages,
        "temperature": cfg.llm.temperature,
        "max_tokens": cfg.llm.max_tokens,
    }
    if tools:
        kwargs["tools"] = tools

    response = await client.chat.completions.create(**kwargs)
    
    msg = response.choices[0].message
    
    if msg.tool_calls:
        # Convert ke dict agar aman saat dikembalikan ke messages array
        return {
            "type": "tool_calls", 
            "calls": msg.tool_calls, 
            "message_obj": msg.model_dump(exclude_none=True)
        }
    
    content = msg.content or ""
    
    # Menghapus reasoning leak (tag <think> atau <thought> beserta isinya)
    # Biasanya model reasoning seperti gemma atau deepseek membocorkan ini
    content = re.sub(r'<(?:think|thought)>.*?</(?:think|thought)>', '', content, flags=re.DOTALL)
    # Hapus tag pembuka atau penutup yang tertinggal
    content = re.sub(r'</?(?:think|thought)>', '', content).strip()
    
    return {"type": "text", "content": content}
