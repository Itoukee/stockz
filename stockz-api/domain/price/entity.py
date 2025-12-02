from pydantic import BaseModel
from datetime import date as d_type
from decimal import Decimal


class OHLCV(BaseModel):
    open: Decimal
    high: Decimal
    low: Decimal
    close: Decimal
    volume: int

    model_config = {"frozen": True}


class PriceDaily:
    def __init__(self, ticker: str, date: d_type, ohlcv: OHLCV):
        self.ticker = ticker
        self.date = date
        self.ohlcv = ohlcv

    def to_dict(self):
        pass
