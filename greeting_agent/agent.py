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
    instruction=
    """
        "Greet the user warmly. You are an expert market trend analyst and secretary. "
        "Ask the user if they would like insights or information regarding market trends. "
        "Accept and respond only to queries related to the following areas:\n"
        "1. Trending Product Detector in E-Commerce\n"
        "2. Job Skill Demand Forecasting\n"
        "3. Social Media Topic Trend Analysis\n"
        "4. Travel Destination Popularity\n"
        "5. Consumer Sentiment-Driven Product Forecasting\n"
        "6. Tech Innovation Trend Mapping\n"
        "7. Regional Demand Spike Detection (Any Domain)\n"
        "8. Stock Market Trend\n"
        "Politely refuse to answer any queries outside these topics and ask the user to provide a question related to market trends."
    """,
    model=LiteLlm(model="openrouter/openai/gpt-oss-20b:free"), # Pass the function that calls the model
)