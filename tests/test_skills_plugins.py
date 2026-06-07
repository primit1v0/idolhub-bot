from core.event_bus import EventBus
from skills.loader import make_tool_schema, parse_skill_file


def test_event_bus_subscribe_emit():
    bus = EventBus()
    called = []
    
    def listener(ctx):
        called.append(ctx["val"])
        
    bus.subscribe("test_event", listener)
    
    import asyncio
    asyncio.run(bus.emit("test_event", {"val": 42}))
    assert called == [42]

def test_skills_parsing(tmp_path):
    skill_file = tmp_path / "web_search.md"
    skill_file.write_text('''---
name: web_search
description: Search the web
parameters:
  query:
    type: string
    description: Search query
    required: true
---
Instructions here...''')
    
    parsed = parse_skill_file(str(skill_file))
    assert parsed is not None
    metadata, instructions = parsed
    assert metadata["name"] == "web_search"
    assert instructions == "Instructions here..."
    
    schema = make_tool_schema(metadata)
    assert schema["type"] == "function"
    assert schema["function"]["name"] == "web_search"
    assert "query" in schema["function"]["parameters"]["properties"]
    assert "query" in schema["function"]["parameters"]["required"]
