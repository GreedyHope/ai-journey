from google import genai
from google.genai import types
import os
import json

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

SYSTEM_PROMPT = "You are a witty pirate captain. You answer every question accurately and helpfully, but always in pirate speak, with nautical metaphors where you can fit them."

MEMORY_FILE = "memory.json"

def load_history():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            raw = json.load(f)
        return [
            types.Content(role=item["role"], parts=[types.Part(text=item["text"])])
            for item in raw
        ]
    return []

def save_history(history):
    raw = [
        {"role": c.role, "text": c.parts[0].text}
        for c in history
    ]
    with open(MEMORY_FILE, "w") as f:
        json.dump(raw, f, indent=2)

conversation_history = load_history()

def ask(question):
    conversation_history.append(
        types.Content(role="user", parts=[types.Part(text=question)])
    )

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=conversation_history,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT
        )
    )

    conversation_history.append(
        types.Content(role="model", parts=[types.Part(text=response.text)])
    )

    save_history(conversation_history)
    return response.text

if __name__ == "__main__":
    while True:
        question = input("\nAsk something (or 'quit'): ")
        if question.lower() == "quit":
            break
        answer = ask(question)
        print(f"\n{answer}")