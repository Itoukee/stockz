import yfinance as yf
from datetime import date as d_type
from typing import List
from pandas.core.frame import DataFrame

from domain.price.entity import PriceDaily, OHLCV
from domain.price.provider import PriceProvider


class YahooPriceProvider(PriceProvider):

    def fetch_price_daily(
        self, ticker: str, start: d_type, end: d_type
    ) -> List[PriceDaily]:
        financial_api_data = yf.download(ticker, start=start, end=end)

        if financial_api_data is None or financial_api_data.empty:
            return []

        prices = []
        for index, row in financial_api_data.iterrows():
            prices.append(
                PriceDaily(
                    ticker=ticker,
                    date=index.date(),
                    ohlcv=OHLCV(
                        open=row["Open"].iloc[0],
                        high=row["High"].iloc[0],
                        low=row["Low"].iloc[0],
                        close=row["Close"].iloc[0],
                        volume=int(row["Volume"].iloc[0]),
                    ),
                )
            )

        return prices
