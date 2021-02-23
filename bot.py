#!/usr/bin/python
import os
import praw
import re

class Bot:
  def __init__(self):
    self.client_id = "w-ujp6nymni8oA"
    self.client_secret = "CQ7yAx9S-8X8VDrZ0eHLiQ9zsLHswQ"
    self.password ="sf2^5Z7$Zn"
    self.user_agent = "PriceToCrypto"
    self.username = "shite_or_bitcoin"

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
      has_number = re.search(reg_exp, comment.body)
      if has_number:
        matching_comment = comment.body

    return matching_comment

  def run(self):
    client = self.get_client()
    subreddit = self.scan_subreddit(client, "bitcoin")
    submission = subreddit.random()
    reply_to_comment = self.search_re_in_post_comments(submission, r'(\d[.,]*)+[km]*')

    if reply_to_comment:
      print("Bot found comment:", reply_to_comment)
      # submission.reply(bot_phrase)


bot = Bot()
bot.run()
