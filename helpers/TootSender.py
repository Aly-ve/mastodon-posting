#!/bin/python3

from mastodon import Mastodon

class TootSender():

  SECRET = 'token.secret'

  def __init__(self):
    self.mastodon = Mastodon(
      access_token = self.SECRET,
      api_base_url = 'https://hostux.social'
    )

  def send(self, toots, visibility = 'public', previous_id = None):
    """Send a list of toot"""
    previous_toot = previous_id
    for toot in toots:
      previous_id = previous_toot.id if previous_toot is not None else None
      toot = self.mastodon.status_post(
        toot,
        in_reply_to_id = previous_id,
        visibility = visibility
      )
      previous_toot = toot
  
  def sendWithPicture(self, toots, pictures, visibility = 'public'):
    """Send a picture in the first toot and send the rest of the toot"""
    media = [self.mastodon.media_post(p) for p in pictures]
    firstToot = toots[0]
    toots.remove(firstToot)

    toot = self.mastodon.status_post(firstToot, media_ids=media)
    self.send(toots, previous_id = toot.id)
