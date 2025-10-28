# 🧠 AI Web Search (Mini Project)
## Overview
This is a simple AI-powered Q&A tool built using OpenAI’s Chat API.
## Features
- Clean architecture (API logic separated from UI)
- Rotating file logging (enterprise-style)
- Test-Driven Development (mocked API test)
- CLI user experience
## How to Run
```
pip install -r requirements.txt
echo "OPENAI_API_KEY=sk-your-key-here" > .env
pytest -q
python -m src.main
```
## Example
```
🤖 Welcome to the AI Q&A System!
Ask me anything: What is AI?
💡 AI Answer:
Artificial Intelligence (AI) is...
```
## What I Learned
- How to connect to OpenAI’s API
- How to separate code into layers (Clean Architecture)
- How to use basic enterprise logging
- How to write and mock tests (TDD)
