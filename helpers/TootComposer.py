#!/bin/python3

class TootComposer():

  TOOT_MAX_LEN = 480
  SPACE = ' '

  def __init__(self, toot = ""):
    self.toot = toot

  def __get_last_character(self, toot, c):
    """In a string, get the last chacater given as c parameter"""

    index, i = -1, len(toot) - 1
    while index == -1 and i > 0:
      if toot[i] == c:
        index = i
      i -= 1
    return index

  def fill(self):
    """Separe a long toot in many toots depending of the length"""
  
    toots, rest = [], self.toot

    while len(rest) > self.TOOT_MAX_LEN:
      max_length_as_toot = (rest[:self.TOOT_MAX_LEN]).strip()
      index = self.__get_last_character(max_length_as_toot, self.SPACE)
      current_toot = rest[:index]
      toots.append(current_toot.strip())
      rest = rest[index:]
    
    if len(rest) > 0:
      toots.append(rest.strip())

    return toots
