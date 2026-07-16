from google import genai
from google.genai import types
import os

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

SYSTEM_PROMPT = "You are a witty pirate captain. You answer every question accurately and helpfully, but always in pirate speak, with nautical metaphors where you can fit them."

def ask(question):
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=question,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT
        )
    )
    return response.text

if __name__ == "__main__":
    while True:
        question = input("\nAsk something (or 'quit'): ")
        if question.lower() == "quit":
            break
        answer = ask(question)
        print(f"\n{answer}")