from .expedia import ExpediaScraper
from .orbitz import OrbitzScraper
from .priceline import PricelineScraper
from .travelocity import TravelocityScraper
from .hilton import HiltonScraper


SCRAPERS = [
    ExpediaScraper,
    OrbitzScraper,
    PricelineScraper,
    TravelocityScraper,
    HiltonScraper,
]
SCRAPER_MAP = {s.provider.lower(): s for s in SCRAPERS}


def get_scraper(provider):
    return SCRAPER_MAP.get(provider.lower())
