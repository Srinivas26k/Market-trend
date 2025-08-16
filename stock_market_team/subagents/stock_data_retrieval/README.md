# Stock Data Retrieval Agent 📊

This subagent is responsible for retrieving comprehensive stock market data using Yahoo Finance. It's part of the larger Stock Market Analysis Team and serves as the primary data source for all subsequent analysis.

## 🎯 Purpose

The Stock Data Retrieval Agent fetches real-time and historical stock market data, providing a solid foundation for technical analysis, validation, and visualization. It ensures all downstream agents have access to accurate, up-to-date market information.

## 🚀 Features

### Data Sources
- **Yahoo Finance Integration**: Real-time stock data via `yfinance` library
- **Multi-timeframe Support**: 1 day to 5 years of historical data
- **Company Information**: Fundamental data and company metrics
- **Technical Indicators**: Built-in calculation capabilities

### Data Types Retrieved
- **Price Data**: Open, High, Low, Close, Adjusted Close
- **Volume Information**: Trading volume across all timeframes
- **Moving Averages**: SMA and EMA calculations
- **Volatility Metrics**: Standard deviation and risk measures
- **Performance Metrics**: Returns and percentage changes
- **52-Week Analysis**: High/low ranges and current positioning
- **Company Fundamentals**: Basic company information

## 📈 Supported Timeframes

| Period | Interval | Description |
|--------|----------|-------------|
| 1 Day | 1 minute | Intraday trading data |
| 1 Week | Daily | 5-day trading period |
| 1 Month | Daily | 30-day historical data |
| 3 Months | Daily | Quarterly analysis |
| 6 Months | Daily | Semi-annual trends |
| 1 Year | Daily | Annual performance |
| 2 Years | Daily | Extended historical view |
| 5 Years | Daily | Long-term trend analysis |

## 🔧 Core Function: `stock_data(symbol)`

### Parameters
- **symbol** (str): Stock ticker symbol (e.g., 'AAPL', 'GOOGL', 'TSLA')

### Returns
Comprehensive dictionary containing:

```python
{
    "symbol": "AAPL",
    "current_price": 150.25,
    "price_changes": {
        "1d": {"absolute": 2.50, "percentage": 1.69},
        "1w": {"absolute": -1.25, "percentage": -0.83},
        "1m": {"absolute": 8.75, "percentage": 6.18}
        # ... additional timeframes
    },
    "moving_averages": {
        "sma_20": 148.30,
        "sma_50": 145.60,
        "ema_12": 149.85
        # ... additional indicators
    },
    "volatility": {
        "1m": 2.45,
        "6m": 3.12,
        "1y": 2.89
    },
    "ranges": {
        "52_week_high": 182.94,
        "52_week_low": 124.17
    },
    "volume_analysis": {
        "current_volume": 125000000,
        "avg_volume_1m": 95000000
    },
    "company_info": {
        "name": "Apple Inc.",
        "sector": "Technology",
        "market_cap": 2450000000000
    }
}
```

## 🛠️ Technical Implementation

### Dependencies
- `yfinance`: Yahoo Finance data retrieval
- `pandas`: Data manipulation and analysis
- `numpy`: Numerical computations
- `datetime`: Date/time handling
- `google.adk`: Agent framework integration

### Agent Configuration
```python
from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm

# Model configuration
model = LiteLlm(
    model="openai/gpt-4o-mini",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

# Agent definition
stock_data_retrieval_agent = LlmAgent(
    name="StockDataRetrieval",
    model=model,
    system_prompt="Expert stock data retrieval specialist...",
    tools=[stock_data]
)
```

## 📊 Data Processing Features

### Price Analysis
- Current market price with real-time updates
- Historical price tracking across multiple timeframes
- Price change calculations (absolute and percentage)
- Opening and closing price analysis

### Technical Indicators
- **Simple Moving Averages (SMA)**: 20, 50, 200-day periods
- **Exponential Moving Averages (EMA)**: 12, 26-day periods
- **Volatility Analysis**: Standard deviation calculations
- **Volume Analysis**: Trading volume trends and averages

### Risk Metrics
- Historical volatility across different timeframes
- Price range analysis (52-week high/low)
- Risk-adjusted return calculations
- Drawdown analysis capabilities

## 🔄 Integration with Team

### Input
- Stock symbol requests from users or upstream agents
- Timeframe specifications for analysis
- Specific data requirements from other subagents

### Output
- Structured financial data ready for validation
- Formatted datasets for technical analysis
- Clean data for visualization components
- Fundamental information for news correlation

### Downstream Consumers
1. **Stock Data Validation Agent**: Validates data quality
2. **Stock Data Analysis Agent**: Performs technical analysis
3. **Stock Data Visualization Agent**: Creates charts and graphs
4. **Stock News Analysis Agent**: Correlates with market news

## 🚦 Error Handling

The agent includes robust error handling for:
- Invalid stock symbols
- Market hours and trading halts
- Network connectivity issues
- Data availability limitations
- API rate limiting

## 🧪 Testing

### Quick Test
```python
from stock_market_team.subagents.stock_data_retrieval.agent import stock_data

# Test with Apple stock
result = stock_data("AAPL")
print(f"Current price: ${result['current_price']:.2f}")
print(f"1-day change: {result['price_changes']['1d']['percentage']:.2f}%")
```

### Test Scripts
- `test_stock_data_function.py`: Unit tests for data retrieval
- `quick_test_stock_data.py`: Quick functionality verification

## 📝 Usage Examples

### Basic Stock Data Retrieval
```python
# Get comprehensive Apple stock data
apple_data = stock_data("AAPL")

# Access specific metrics
current_price = apple_data["current_price"]
daily_change = apple_data["price_changes"]["1d"]["percentage"]
volume = apple_data["volume_analysis"]["current_volume"]
```

### Multiple Stock Analysis
```python
# Analyze multiple stocks
symbols = ["AAPL", "GOOGL", "MSFT", "TSLA"]
stock_results = {}

for symbol in symbols:
    stock_results[symbol] = stock_data(symbol)
    print(f"{symbol}: ${stock_results[symbol]['current_price']:.2f}")
```

## 🔧 Configuration

### Environment Setup
Ensure the following environment variable is set:
```bash
OPENROUTER_API_KEY=your_openrouter_api_key_here
```

### Customization Options
- Modify timeframes in the `periods` dictionary
- Adjust technical indicators calculations
- Extend company information retrieval
- Add custom data validation rules

## 🐛 Troubleshooting

### Common Issues
1. **Symbol Not Found**: Verify ticker symbol validity
2. **No Data Available**: Check market hours and trading status
3. **API Errors**: Verify internet connection and API limits
4. **Calculation Errors**: Ensure sufficient historical data exists

### Debug Mode
Enable detailed logging by setting debug mode in the agent configuration.

## 📚 Additional Resources

- [Yahoo Finance API Documentation](https://python-yahoofinance.readthedocs.io/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Google ADK Agent Framework](https://developers.google.com/agent-development-kit)

---

**Note**: Market data is provided for informational purposes only. Always verify critical financial data through multiple sources before making investment decisions.