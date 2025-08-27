import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.shared import available_functions

from config import SYSTEM_PROMPT


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)
    is_verbose, user_args = get_user_input()

    if not user_args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here" [--verbose]')
        print('Example: python main.py "How do I build a calculator app?"')
        sys.exit(1)
    user_prompt = " ".join(user_args)
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    generate_content(client, messages, is_verbose)


def get_user_input():
    is_verbose = "--verbose" in sys.argv
    args = []
    for arg in sys.argv[1:]:  # Skip the script name (sys.argv[0])
        if not arg.startswith("--"):
            args.append(arg)

    return (is_verbose, args)


def generate_content(client, messages, is_verbose):
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=SYSTEM_PROMPT
        ),
    )
    if not response.function_calls:
        return response.text

    for function_call_part in response.function_calls:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")

    if is_verbose:
        print(f"User prompt: {messages}")
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)


if __name__ == "__main__":
    main()
