from abc import ABC, abstractmethod
from typing import Optional, Iterable

from domain.price.entity import PriceDaily


class PriceDailyRepository(ABC):
    @abstractmethod
    def save_bulk(self, prices: list[PriceDaily]) -> None:
        """Saves in bulk all the prices for a ticker given a timespan"""

    @abstractmethod
    def get(self, ticker: str, date) -> Optional[PriceDaily]:
        """Return PriceDaily or None."""

    @abstractmethod
    def list_for_ticker(
        self, ticker: str, limit: int = 100, offset: int = 0
    ) -> Iterable[PriceDaily]:
        """Return an iterable of PriceDaily for ticker, ordered by date desc."""
