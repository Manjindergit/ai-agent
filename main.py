import os
import argparse

from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from call_function import available_functions, call_function


def main():
    parser = argparse.ArgumentParser(description="Gemini CLI Tool")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError("API_KEY not found in environment variables.")

    print("Hello from ai-agent!")

    client = genai.Client(api_key=api_key)
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
    if args.verbose:
        print(f"User prompt: {args.user_prompt}\n")
    generate_content(client, messages, args.verbose)


def generate_content(client, messages, verbose):
    response_1 = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=system_prompt
        ),
    )

    if not response_1.usage_metadata:
        raise RuntimeError("NO RESPONSE!!")

    if verbose:
        print(f"Prompt token: {response_1.usage_metadata.prompt_token_count}")
        print("Response tokens:", response_1.usage_metadata.candidates_token_count)

    if not response_1.function_calls:
        print("Response from Gemini API:", response_1.text)
        return
    
    function_response = []
    for function_call in response_1.function_calls:
        result = call_function(function_call, verbose)
        if (
            not result.parts
            or not result.parts[0].function_response
            or "result" not in result.parts[0].function_response
        ):
            print(f"Invalid function response for {function_call.name}")
        if verbose:
            print(f"Function response for {function_call.name}: {result.parts[0].function_response}")
        function_response.append(result)
        
        


if __name__ == "__main__":
    main()
