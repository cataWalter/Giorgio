import os
import sys
import time
from typing import List

# Placeholder for Gemini API call
def call_gemini_api(question: str, memory: str) -> str:
    # Replace this with actual Gemini API integration
    return f"Gemini response to: '{question}' with memory: '{memory[:50]}...'"

QUESTIONS_FILE = "questions.txt"

def save_question(question: str):
    with open(QUESTIONS_FILE, "a", encoding="utf-8") as f:
        f.write(question.strip() + "\n")

def load_memory() -> str:
    if not os.path.exists(QUESTIONS_FILE):
        return ""
    with open(QUESTIONS_FILE, "r", encoding="utf-8") as f:
        return f.read()

def main():
    print("Ask a question (type 'exit' to quit):")
    while True:
        question = input("> ").strip()
        if question.lower() == "exit":
            print("Goodbye!")
            break
        if not question:
            continue
        save_question(question)
        memory = load_memory()
        response = call_gemini_api(question, memory)
        print(f"Gemini: {response}")

if __name__ == "__main__":
    main()