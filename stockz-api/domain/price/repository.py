from abc import ABC, abstractmethod
from typing import Optional, Iterable

from domain.price.entity import PriceDaily


class PriceDailyRepository(ABC):
    @abstractmethod
    def save(self, price: PriceDaily) -> PriceDaily:
        """Persist a PriceDaily and return it (possibly with DB filled fields)."""

    @abstractmethod
    def get(self, ticker: str, date) -> Optional[PriceDaily]:
        """Return PriceDaily or None."""

    @abstractmethod
    def list_for_ticker(
        self, ticker: str, limit: int = 100, offset: int = 0
    ) -> Iterable[PriceDaily]:
        """Return an iterable of PriceDaily for ticker, ordered by date desc."""
