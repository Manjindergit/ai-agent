import os
import argparse
from dotenv import load_dotenv
from google import genai


load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")


if not api_key:
    raise ValueError("API_KEY not found in environment variables.")


def main():
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    args = parser.parse_args()
    print("Hello from ai-agent!")

    client = genai.Client(api_key=api_key)
    response_1 = client.models.generate_content(
        model="gemini-2.5-flash", 
        contents=args.user_prompt,
    )
    
    if not response_1.usage_metadata:
        raise RuntimeError("NO RESPONSE!!")
    
    print(f'Prompt token: {response_1.usage_metadata.prompt_token_count}')
    print("Response tokens:", response_1.usage_metadata.candidates_token_count)
    
          
    print("Response from Gemini API:", response_1.text)


if __name__ == "__main__":
    main()
