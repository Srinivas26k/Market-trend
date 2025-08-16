"""
this Agent is responsible for retrieving stock market data .
"""

from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm
import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import numpy as np

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variable (optional at import time)
openrouter_api_key = os.getenv("OPENROUTER_API_KEY")
if openrouter_api_key:
    # Set the environment variable for the library to use
    os.environ["OPENROUTER_API_KEY"] = openrouter_api_key



def stock_data(symbol: str):
    """
    Comprehensive stock data retrieval function for financial experts.
    
    Args:
        symbol (str): Stock symbol (e.g., 'AAPL', 'GOOGL', 'TSLA')
    
    Returns:
        dict: Comprehensive financial data including price metrics, technical indicators, and analysis
    """
    try:
        # Create ticker object
        ticker = yf.Ticker(symbol)
        
        # Get current date
        today = datetime.now()
        
        # Define time periods
        periods = {
            '1d': today - timedelta(days=1),
            '1w': today - timedelta(weeks=1),
            '1m': today - timedelta(days=30),
            '3m': today - timedelta(days=90),
            '6m': today - timedelta(days=180),
            '1y': today - timedelta(days=365),
            '2y': today - timedelta(days=730),
            '5y': today - timedelta(days=1825)
        }
        
        # Get historical data for different periods
        hist_1d = ticker.history(period="1d", interval="1m")
        hist_1w = ticker.history(period="5d")
        hist_1m = ticker.history(period="1mo")
        hist_3m = ticker.history(period="3mo")
        hist_6m = ticker.history(period="6mo")
        hist_1y = ticker.history(period="1y")
        hist_2y = ticker.history(period="2y")
        hist_5y = ticker.history(period="5y")
        
        # Get company info
        info = ticker.info
        
        # Current price data
        current_price = hist_1d['Close'].iloc[-1] if not hist_1d.empty else None
        open_price = hist_1d['Open'].iloc[0] if not hist_1d.empty else None
        
        # Calculate means for different periods
        mean_1m = hist_1m['Close'].mean() if not hist_1m.empty else None
        mean_3m = hist_3m['Close'].mean() if not hist_3m.empty else None
        mean_6m = hist_6m['Close'].mean() if not hist_6m.empty else None
        mean_1y = hist_1y['Close'].mean() if not hist_1y.empty else None
        mean_2y = hist_2y['Close'].mean() if not hist_2y.empty else None
        
        # Calculate volatility (standard deviation)
        volatility_1m = hist_1m['Close'].std() if not hist_1m.empty else None
        volatility_6m = hist_6m['Close'].std() if not hist_6m.empty else None
        volatility_1y = hist_1y['Close'].std() if not hist_1y.empty else None
        
        # Calculate price changes and percentages
        price_change_1d = (current_price - hist_1d['Close'].iloc[0]) if len(hist_1d) > 1 else 0
        price_change_1w = (current_price - hist_1w['Close'].iloc[0]) if len(hist_1w) > 1 else 0
        price_change_1m = (current_price - hist_1m['Close'].iloc[0]) if len(hist_1m) > 1 else 0
        price_change_1y = (current_price - hist_1y['Close'].iloc[0]) if len(hist_1y) > 1 else 0
        
        # Calculate percentage changes
        pct_change_1d = (price_change_1d / hist_1d['Close'].iloc[0] * 100) if len(hist_1d) > 1 else 0
        pct_change_1w = (price_change_1w / hist_1w['Close'].iloc[0] * 100) if len(hist_1w) > 1 else 0
        pct_change_1m = (price_change_1m / hist_1m['Close'].iloc[0] * 100) if len(hist_1m) > 1 else 0
        pct_change_1y = (price_change_1y / hist_1y['Close'].iloc[0] * 100) if len(hist_1y) > 1 else 0
        
        # Calculate 52-week high and low
        week_52_high = hist_1y['High'].max() if not hist_1y.empty else None
        week_52_low = hist_1y['Low'].min() if not hist_1y.empty else None
        
        # Calculate moving averages
        ma_50 = hist_1y['Close'].tail(50).mean() if len(hist_1y) >= 50 else None
        ma_200 = hist_1y['Close'].tail(200).mean() if len(hist_1y) >= 200 else None
        
        # Volume analysis
        avg_volume_1m = hist_1m['Volume'].mean() if not hist_1m.empty else None
        current_volume = hist_1d['Volume'].iloc[-1] if not hist_1d.empty else None
        
        # RSI calculation (14-day)
        def calculate_rsi(prices, window=14):
            if len(prices) < window:
                return None
            delta = prices.diff()
            gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
            loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
            rs = gain / loss
            rsi = 100 - (100 / (1 + rs))
            return rsi.iloc[-1]
        
        rsi = calculate_rsi(hist_1m['Close']) if not hist_1m.empty else None
        
        # Beta calculation (correlation with market - using SPY as proxy)
        try:
            spy = yf.Ticker("SPY")
            spy_hist = spy.history(period="1y")
            if not hist_1y.empty and not spy_hist.empty:
                # Align dates
                common_dates = hist_1y.index.intersection(spy_hist.index)
                if len(common_dates) > 10:
                    stock_returns = hist_1y.loc[common_dates]['Close'].pct_change().dropna()
                    market_returns = spy_hist.loc[common_dates]['Close'].pct_change().dropna()
                    beta = np.cov(stock_returns, market_returns)[0][1] / np.var(market_returns)
                else:
                    beta = None
            else:
                beta = None
        except:
            beta = None
        
        # Comprehensive stock data dictionary
        stock_analysis = {
            # Basic Information
            "symbol": symbol.upper(),
            "company_name": info.get('longName', 'N/A'),
            "sector": info.get('sector', 'N/A'),
            "industry": info.get('industry', 'N/A'),
            "market_cap": info.get('marketCap', 'N/A'),
            
            # Current Price Data
            "todays_close_price": round(current_price, 2) if current_price else None,
            "open_price": round(open_price, 2) if open_price else None,
            "current_price": round(current_price, 2) if current_price else None,
            
            # Historical Averages
            "mean_price_1_month": round(mean_1m, 2) if mean_1m else None,
            "mean_price_3_months": round(mean_3m, 2) if mean_3m else None,
            "mean_price_6_months": round(mean_6m, 2) if mean_6m else None,
            "mean_price_1_year": round(mean_1y, 2) if mean_1y else None,
            "mean_price_2_years": round(mean_2y, 2) if mean_2y else None,
            
            # Price Changes
            "price_change_1_day": round(price_change_1d, 2) if price_change_1d else None,
            "price_change_1_week": round(price_change_1w, 2) if price_change_1w else None,
            "price_change_1_month": round(price_change_1m, 2) if price_change_1m else None,
            "price_change_1_year": round(price_change_1y, 2) if price_change_1y else None,
            
            # Percentage Changes
            "percentage_change_1_day": round(pct_change_1d, 2) if pct_change_1d else None,
            "percentage_change_1_week": round(pct_change_1w, 2) if pct_change_1w else None,
            "percentage_change_1_month": round(pct_change_1m, 2) if pct_change_1m else None,
            "percentage_change_1_year": round(pct_change_1y, 2) if pct_change_1y else None,
            
            # 52-Week Range
            "52_week_high": round(week_52_high, 2) if week_52_high else None,
            "52_week_low": round(week_52_low, 2) if week_52_low else None,
            "distance_from_52w_high": round(((current_price - week_52_high) / week_52_high * 100), 2) if current_price and week_52_high else None,
            "distance_from_52w_low": round(((current_price - week_52_low) / week_52_low * 100), 2) if current_price and week_52_low else None,
            
            # Technical Indicators
            "moving_average_50_days": round(ma_50, 2) if ma_50 else None,
            "moving_average_200_days": round(ma_200, 2) if ma_200 else None,
            "rsi_14_days": round(rsi, 2) if rsi else None,
            "beta": round(beta, 2) if beta else None,
            
            # Volatility Analysis
            "volatility_1_month": round(volatility_1m, 2) if volatility_1m else None,
            "volatility_6_months": round(volatility_6m, 2) if volatility_6m else None,
            "volatility_1_year": round(volatility_1y, 2) if volatility_1y else None,
            
            # Volume Analysis
            "current_volume": int(current_volume) if current_volume else None,
            "average_volume_1_month": int(avg_volume_1m) if avg_volume_1m else None,
            "volume_ratio": round((current_volume / avg_volume_1m), 2) if current_volume and avg_volume_1m else None,
            
            # Financial Metrics from Company Info
            "pe_ratio": info.get('trailingPE', 'N/A'),
            "forward_pe": info.get('forwardPE', 'N/A'),
            "price_to_book": info.get('priceToBook', 'N/A'),
            "dividend_yield": info.get('dividendYield', 'N/A'),
            "earnings_per_share": info.get('trailingEps', 'N/A'),
            "book_value": info.get('bookValue', 'N/A'),
            
            # Additional Metrics for Financial Analysis
            "debt_to_equity": info.get('debtToEquity', 'N/A'),
            "return_on_equity": info.get('returnOnEquity', 'N/A'),
            "return_on_assets": info.get('returnOnAssets', 'N/A'),
            "profit_margin": info.get('profitMargins', 'N/A'),
            "operating_margin": info.get('operatingMargins', 'N/A'),
            
            # Analyst Recommendations
            "target_price": info.get('targetMeanPrice', 'N/A'),
            "recommendation": info.get('recommendationKey', 'N/A'),
            
            # Timestamp
            "data_retrieved_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "last_market_close": hist_1d.index[-1].strftime("%Y-%m-%d %H:%M:%S") if not hist_1d.empty else None
        }
        
        return stock_analysis
        
    except Exception as e:
        return {
            "error": f"Failed to retrieve data for {symbol}: {str(e)}",
            "symbol": symbol,
            "data_retrieved_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }



# Create an agent for retrieving stock data
stock_data_retrieval_agent = LlmAgent(
    name="StockDataRetrievalAgent",
    model=LiteLlm(model="openrouter/moonshotai/kimi-k2:free", api_key=os.getenv("OPENROUTER_API_KEY")),
    description="Agent for retrieving stock market data based on user requests",
    instruction="""
    You are a stock market data retrieval agent. 

    Your task is to retrieve comprehensive stock data based on the user's request.
    Provide detailed financial metrics, technical indicators, and analysis for the specified stock symbol.
    Ensure the data is accurate and up-to-date.

    ##Data Requirements
    - Provide current price, historical averages, price changes, percentage changes, and technical indicators.
    - Include 52-week high/low, moving averages, RSI, beta, volatility, and volume analysis.
    - Include financial metrics like P/E ratio, dividend yield, and analyst recommendations.
    - Ensure the data is well-structured and easy to interpret for financial analysis.
    - Provide a timestamp for when the data was retrieved.
    """,
    tools=[stock_data],
    output_key="stock_datasheet"  # Key for the output data in the agent's response
)

root_agent = stock_data_retrieval_agent