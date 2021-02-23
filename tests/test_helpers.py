from unittest import main, TestCase
from datetime import datetime, timedelta

from helpers import get_random_date

class TestHelpers(TestCase):

    def setUp(self):
        self.today = datetime.today()

        ten_years_delta = timedelta(days=10*365)
        self.ten_years_ago = self.today - ten_years_delta

    def test_random_dates_two_dates(self):
        """Get a randomdate up to a specific date"""
        date1 = get_random_date(self.ten_years_ago)
        date2 = get_random_date(self.ten_years_ago)

        self.assertFalse(date1.date() == date2.date())

    def test_random_dates_allow_time_range(self):
        """Allows requesting for a specific time range"""
        date_in_range = get_random_date(self.ten_years_ago, self.today)

        self.assertTrue(date_in_range.date())

    def test_random_dates_valid_timerange_only(self):
        """Enforce a valid timerange (start date < end date)"""
        valid_range = get_random_date(self.ten_years_ago, self.today)

        self.assertTrue(valid_range.date())
        self.assertRaises(
            Exception,
            get_random_date,
            self.today,
            self.ten_years_ago,
        )
