# infrastructure/price/model.py
from decimal import Decimal
from datetime import date as d_type
from typing import Optional

from sqlalchemy import String, Date, Numeric, BigInteger
from sqlalchemy.orm import mapped_column

from infra.pgsql import Base, session as default_session, Session
from domain.price.repository import PriceDailyRepository
from domain.price.entity import PriceDaily, OHLCV


class PriceDailyModel(Base):
    __tablename__ = "price_daily"

    ticker = mapped_column(String, primary_key=True, index=True)
    date = mapped_column(Date, primary_key=True)
    open = mapped_column(Numeric(18, 8), nullable=False)
    high = mapped_column(Numeric(18, 8), nullable=False)
    low = mapped_column(Numeric(18, 8), nullable=False)
    close = mapped_column(Numeric(18, 8), nullable=False)
    volume = mapped_column(BigInteger, nullable=False)


class PriceDailyPgsqlRepository(PriceDailyRepository):

    def __init__(self, session: Session = default_session):
        self.session = session

    def _to_domain(self, model: PriceDailyModel) -> PriceDaily:
        return PriceDaily(
            ticker=model.ticker,
            date=model.date,
            ohlcv=OHLCV(
                open=Decimal(model.open),
                high=Decimal(model.high),
                low=Decimal(model.low),
                close=Decimal(model.close),
                volume=int(model.volume),
            ),
        )

    def _to_model(self, domain: PriceDaily) -> PriceDailyModel:
        return PriceDailyModel(
            ticker=domain.ticker,
            date=domain.date,
            open=domain.ohlcv.open,
            high=domain.ohlcv.high,
            low=domain.ohlcv.low,
            close=domain.ohlcv.close,
            volume=domain.ohlcv.volume,
        )

    def save_bulk(self, prices: list[PriceDaily]) -> None:
        models = [
            PriceDailyModel(
                ticker=p.ticker,
                date=p.date,
                open=p.ohlcv.open,
                high=p.ohlcv.high,
                low=p.ohlcv.low,
                close=p.ohlcv.close,
                volume=p.ohlcv.volume,
            )
            for p in prices
        ]

        for m in models:
            self.session.merge(m)

        return

    def get(self, ticker: str, date: d_type) -> Optional[PriceDaily]:
        model = self.session.get(PriceDailyModel, (ticker, date))
        if model is None:
            return None
        return self._to_domain(model)

    def list_for_ticker(
        self, ticker: str, limit: int = 100, offset: int = 0
    ) -> list[PriceDaily]:
        query = (
            self.session.query(PriceDailyModel)
            .filter(PriceDailyModel.ticker == ticker)
            .order_by(PriceDailyModel.date.desc())
            .limit(limit)
            .offset(offset)
        )
        return [self._to_domain(m) for m in query.all()]
