import streamlit as st
from plotly import graph_objs as go
from stock_data import StockData
from datetime import date

class App:
    def __init__(self):
        self.stock_data = None

    def get_user_input(self):
        symbol = st.text_input('Enter stock symbol:', 'AAPL')
        start_date = st.date_input('Start date', date.today())
        end_date = st.date_input('End date', date.today())
        self.stock_data = StockData(symbol, start_date, end_date)

    def update_chart(self):
        if self.stock_data:
            data = self.stock_data.fetch_data()
            fig = go.Figure(data=[go.Candlestick(x=data.index,
                                                 open=data['Open'],
                                                 high=data['High'],
                                                 low=data['Low'],
                                                 close=data['Close'])])
            st.plotly_chart(fig)

    def run(self):
        self.get_user_input()
        self.update_chart()

if __name__ == "__main__":
    app = App()
    app.run()
