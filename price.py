import ast
import requests

class Price:
  def __init__(self):
    self.currency = "bitcoin"

  def get_price_at_date(self, date):
    short_date = date.strftime("%Y-%m-%d")

    response = requests.get(
      "https://api.coindesk.com/v1/bpi/historical/close.json?start={}&end={}".format(
        short_date, short_date
      )
    )

    content_decoded = response.content.decode("utf-8")
    content = ast.literal_eval(content_decoded)

    return {
      "date": short_date,
      "price": content["bpi"][short_date],
    }
