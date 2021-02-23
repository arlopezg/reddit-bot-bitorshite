from datetime import datetime, timedelta
import random


today = datetime.today()
ten_years_delta = timedelta(days=10*365)
ten_years_ago = today - ten_years_delta

def get_random_date(start=ten_years_ago, end=datetime.today()):
    """Generate a random datetime between `start` and `end`"""
    return start + timedelta(
        # Get a random amount of seconds between `start` and `end`
        seconds=random.randint(0, int((end - start).total_seconds())),
    )
