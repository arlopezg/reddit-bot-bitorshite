#!/usr/bin/python
import os
import praw
import re

from helpers import get_random_date
from price import Price

class Bot:
  def __init__(self):
    self.client_id = os.getenv("CLIENT_ID")
    self.client_secret = os.getenv("CLIENT_SECRET")
    self.password = os.getenv("USER_PASSWORD")
    self.user_agent = os.getenv("APP_USERAGENT")
    self.username = os.getenv("USER_USERNAME")

  def get_client(self):
    return praw.Reddit(
      user_agent=self.user_agent,
      client_id=self.client_id,
      client_secret=self.client_secret,
      username=self.username,
      password=self.password
    )

  def scan_subreddit(self, client, target):
    return client.subreddit(target)

  def search_re_in_post_comments(self, post, reg_exp):
    matching_comment = None

    for comment in post.comments:
      found_number = re.search(reg_exp, comment.body)
      if found_number:
        matching_comment = comment.body
        return {
          "content": comment.body,
          "with_number": found_number.group()
        }

  def get_price_comparison(self, amount):
    date = get_random_date()
    price = Price().get_price_at_date(date)

    return float(amount) / price["price"]

  def run(self):
    subreddit = self.scan_subreddit(self.get_client(), "bitcoin")
    submission = subreddit.random()
    past_date = get_random_date()

    reply_to_comment = self.search_re_in_post_comments(submission, r'(\d[.,]*)+[km]*')

    if reply_to_comment:
      print("With USD${} you would've bought: {}".format(
        reply_to_comment["with_number"],
        self.get_price_comparison(reply_to_comment["with_number"])
      ))
      # submission.reply(bot_phrase)
      return
    print("Didn't find numbers")

bot = Bot()
bot.run()
