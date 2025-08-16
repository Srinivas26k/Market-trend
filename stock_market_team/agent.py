from google.adk.agents import SequentialAgent, LoopAgent
from google.adk.models.lite_llm import LiteLlm

from .subagents.stock_data_retrieval import stock_data_retrieval_agent
from .subagents.stock_data_validation import stock_data_validation_agent
from .subagents.stock_data_analysis import stock_data_analysis_agent
from .subagents.stock_data_visualization import stock_data_visualization_agent
from .subagents.stock_news_analysis import stock_news_analysis_agent

import os
from dotenv import load_dotenv

load_dotenv()

model = LiteLlm(model="openai/gpt-4o-mini",
                api_key=os.getenv("OPENROUTER_API_KEY"))


# Create a loop agent that can handle tasks in a loop until a condition is met

data_validation_loop = LoopAgent(
    name="DataValidationLoop",
    max_iterations=5,
    sub_agents=[
        stock_data_validation_agent,      # Agent for validating stock data
        stock_data_analysis_agent,        # Agent for analyzing stock data
        stock_data_visualization_agent,   # Agent for visualizing stock data
        stock_news_analysis_agent,        # Agent for analyzing stock news
    ],
    description="Iterateively reviews and validates stock data",
)


# Create a sequential agent that can handle multiple tasks in order
root_agent = SequentialAgent(
    name="StockMarketAgent",
    sub_agents=[
        stock_data_retrieval_agent,    #step1:retrieve stock data according to the user's request
        data_validation_loop,          #step2:validate and analyze the stock data
    ],
    description="Agent for managing stock market data retrieval and validation",
)

