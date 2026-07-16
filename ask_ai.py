from google import genai
from google.genai import types
import os

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

SYSTEM_PROMPT = "You are a witty pirate captain. You answer every question accurately and helpfully, but always in pirate speak, with nautical metaphors where you can fit them."

# This list holds the whole conversation so far
conversation_history = []

def ask(question):
    # Add the user's new question to the running history
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

    # Add the AI's reply to the history too, so it remembers what it said
    conversation_history.append(
        types.Content(role="model", parts=[types.Part(text=response.text)])
    )

    return response.text

if __name__ == "__main__":
    while True:
        question = input("\nAsk something (or 'quit'): ")
        if question.lower() == "quit":
            break
        answer = ask(question)
        print(f"\n{answer}")