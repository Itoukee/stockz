from datetime import date as d_type

from domain.price.repository import PriceDailyRepository
from domain.price.provider import PriceProvider
from infra.pgsql import Session, session as default_session


class ImportPriceDailyUseCase:
    def __init__(
        self,
        provider: PriceProvider,
        repo: PriceDailyRepository,
        session: Session = default_session,
    ):
        self.provider = provider
        self.repo = repo
        self.session = session

    def execute(self, ticker: str, start: d_type, end: d_type) -> bool:
        try:
            prices = self.provider.fetch_price_daily(ticker, start, end)

            self.repo.save_bulk(prices)
            self.session.commit()

        except Exception as err:
            print(err)
            return False

        return True
