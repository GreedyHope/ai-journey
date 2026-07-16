from google import genai
import os

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

def ask(question):
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=question
    )
    return response.text

if __name__ == "__main__":
    while True:
        question = input("\nAsk something (or 'quit'): ")
        if question.lower() == "quit":
            break
        answer = ask(question)
        print(f"\n{answer}")