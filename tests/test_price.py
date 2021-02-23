from unittest import main, TestCase
from datetime import datetime, timedelta

from price import Price
from helpers import get_random_date

class TestHelpers(TestCase):
    def setUp(self):
        self.pricing = Price()

    def test_get_price(self):
      date = get_random_date()
      response = self.pricing.get_price_at_date(date)
      self.assertTrue(type(response["price"]) is float)
