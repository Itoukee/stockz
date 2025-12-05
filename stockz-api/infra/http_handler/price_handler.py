from fastapi import APIRouter
from datetime import date as d_type

from application.price.cases.import_price_daily import ImportPriceDailyUseCase
from infra.price.yahoo_price_provider import YahooPriceProvider
from infra.price.repository import PriceDailyPgsqlRepository

price_router = APIRouter()
yahoo_provider = YahooPriceProvider()
price_repo = PriceDailyPgsqlRepository()


@price_router.post("/prices/import")
def import_prices(ticker: str, start: d_type, end: d_type):
    use_case = ImportPriceDailyUseCase(provider=yahoo_provider, repo=price_repo)

    success = use_case.execute(ticker, start, end)
    return {"Success": success}
