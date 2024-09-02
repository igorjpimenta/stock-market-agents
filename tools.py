from datetime import datetime
from dateutil.relativedelta import relativedelta
import yfinance as yf
from langchain.tools import Tool
from langchain_community.tools import DuckDuckGoSearchResults


def fetch_stock_price(ticker):
    today = datetime.today()
    end_date = today.strftime('%Y-%m-%d')
    start_date = (today - relativedelta(years=1)).strftime('%Y-%m-%d')

    data = yf.download(
        ticker,
        start=start_date,
        end=end_date
    )

    return data


stock_prices_fetching_tool = Tool(
    name='Yahoo Finance Tool',
    description='Fetches stock prices for {ticket} from the last year about \
        an specific stock from Yahoo Finance API',
    func=lambda ticker: fetch_stock_price(ticker)
)

news_searching_tool = DuckDuckGoSearchResults(
    backend='news',
    num_results=10
)
