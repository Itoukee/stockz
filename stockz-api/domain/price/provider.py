from abc import ABC, abstractmethod
from datetime import date as d_type
from typing import List

from domain.price.entity import PriceDaily


class PriceProvider(ABC):
    @abstractmethod
    def fetch_price_daily(
        self, ticker: str, start: d_type, end: d_type
    ) -> List[PriceDaily]:
        pass
