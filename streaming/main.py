import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get the Gemini API key
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Check if the API key is present
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

# Configure the Gemini API
genai.configure(api_key=gemini_api_key)

# Define the model
model = genai.GenerativeModel("gemini-1.5-flash")

def main():
    try:
        # Create a prompt for the agent
        prompt = "You are a helpful assistant named Joker. Please tell me 5 jokes."

        # Generate content
        response = model.generate_content(prompt, stream=True)

        # Stream the response
        for chunk in response:
            print(chunk.text, end="", flush=True)
        print()  # Newline after streaming

    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Run the function
if __name__ == "__main__":
    main()