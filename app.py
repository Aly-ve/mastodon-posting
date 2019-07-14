#!/bin/python3

from helpers.TootComposer import TootComposer
from helpers.TootSender import TootSender

def main():
  toot = str(input("Entrez votre toot:\n"))
  media = []

  tootComposer = TootComposer(toot.strip())
  tootSender = TootSender()

  toots = tootComposer.fill()

  if len(media) > 0:
    tootSender.sendWithPicture(toots, media)
  else:
    tootSender.send(toots)


if __name__ == '__main__':
  main()
