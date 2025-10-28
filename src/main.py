"""
main.py
📚 LESSON: CLI DESIGN + ORCHESTRATION
"""
from src.client import OpenAIClient
from src.logging_config import setup_logging

def main():
    logger = setup_logging()
    client = OpenAIClient()

    print("🤖 Welcome to the AI Q&A System!")
    question = input("Ask me anything: ")
    logger.info(f"User asked: {question}")

    answer = client.ask(question)
    print("\n💡 AI Answer:\n", answer)

    logger.info("Answer successfully returned.")

if __name__ == "__main__":
    main()
