import os
import sys
from google import genai

def main():
    # Retrieve API key from environment variable
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY environment variable is not set.", file=sys.stderr)
        print("Please set it using: export GEMINI_API_KEY='your_api_key'", file=sys.stderr)
        sys.exit(1)

    # Initialize the Gemini API Client
    client = genai.Client(api_key=api_key)

    # Define the model to use
    model_name = "gemini-2.0-flash"

    # Input prompt for generation
    prompt = "Explain artificial intelligence to a beginner in two clear sentences."

    print(f"Sending prompt to {model_name}...")
    print(f"Prompt: '{prompt}'\n")

    try:
        # Request text generation
        response = client.models.generate_content(
            model=model_name,
            contents=prompt
        )

        # Output the generated text result
        print("=== Generated Response ===")
        print(response.text)
        print("==========================")

    except Exception as e:
        print(f"An error occurred during text generation: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()