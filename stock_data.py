## stock_data.py

import yfinance as yf
from datetime import date
from pandas import DataFrame
from typing import Optional

class StockData:
    def __init__(self, symbol: str, start_date: Optional[date] = None, end_date: Optional[date] = None):
        self.symbol = symbol
        self.start_date = start_date if start_date else date.today()
        self.end_date = end_date if end_date else date.today()

    def fetch_data(self) -> DataFrame:
        stock = yf.Ticker(self.symbol)
        data = stock.history(start=self.start_date.strftime('%Y-%m-%d'), end=self.end_date.strftime('%Y-%m-%d'))
        return data
