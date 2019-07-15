#!/bin/python3

from helpers.TootComposer import TootComposer
from helpers.TootSender import TootSender

from flask import request
from flask_api import FlaskAPI, status

app = FlaskAPI(__name__)

app.config['DEFAULT_PARSERS'] = [
  'flask.ext.api.parsers.JSONParser',
  'flask.ext.api.parsers.URLEncodedParser',
  'flask.ext.api.parsers.MaltiPartParser'
]

@app.route('/create', methods=['POST'])
def create():
  test = str(request.data.get('test',))
  print(test)
  
  return {
    "hello": "world"
  }

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
  #main()
  app.run(debug = True)
