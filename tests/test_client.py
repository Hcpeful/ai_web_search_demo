"""
test_client.py
📚 LESSON: TEST-DRIVEN DEVELOPMENT (TDD)
"""
from unittest.mock import patch
from src.client import OpenAIClient

@patch("src.client.OpenAI.chat.completions.create")
def test_ask_returns_string(mock_create):
    mock_create.return_value = type("FakeResponse", (), {
        "choices": [type("Choice", (), {"message": type("Msg", (), {"content": "Hello!"})()})()]
    })
    client = OpenAIClient()
    result = client.ask("Hi")
    assert isinstance(result, str)
    assert result == "Hello!"
