import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")


if not api_key:
    raise ValueError("API_KEY not found in environment variables.")

def main():
    print("Hello from ai-agent!" )
    
    client = genai.Client(api_key=api_key)
    response_1 = client.models.generate_content(
    model="gemini-2.5-flash",
    contents='What model are you',
    )
    
    print("Response from Gemini API:", response_1.text)


if __name__ == "__main__":
    main()
