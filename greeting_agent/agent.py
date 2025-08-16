from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm


import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variable (optional at import time)
openrouter_api_key = os.getenv("OPENROUTER_API_KEY")
if openrouter_api_key:
    # Set the environment variable for the library to use
    os.environ["OPENROUTER_API_KEY"] = openrouter_api_key

root_agent = Agent(
    name="greeting_agent",
    description="An agent that greets users with a friendly message.",
    instruction="Respond to the user with a friendly greeting. You are a helpful financial advisor secretary.",
    model=LiteLlm(model="openrouter/openai/gpt-oss-20b:free"), # Pass the function that calls the model
)