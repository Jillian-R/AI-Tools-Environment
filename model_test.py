import os
from dotenv import load_dotenv
from openai import OpenAI

# Load the API key securely from the .env file
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY was not found.")

client = OpenAI(api_key=api_key)

response = client.responses.create(
    model="gpt-5-mini",
    input="Reply with exactly this sentence: Local API connection successful."
)

print(response.output_text)