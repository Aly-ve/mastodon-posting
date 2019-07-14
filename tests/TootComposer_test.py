#!/bin/python3

import sys
sys.path.append('../helpers')

import unittest
from TootComposer import *

class TestTootComposer(unittest.TestCase):

  def setUp(self):
    self.shortToot = "Hello world"
    self.longToot = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam blandit venenatis pharetra. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Pellentesque venenatis magna vitae ultricies posuere. Morbi vitae dolor bibendum, pharetra lectus vel, luctus erat. Mauris at sem porttitor erat placerat fermentum. Duis luctus mattis luctus. Nullam erat odio, tincidunt quis dignissim sit amet, laoreet eget lectus. Nunc dolor nisi, varius at purus id, viverra tempor diam. Morbi eget eleifend sem. Duis malesuada varius metus."

  def test_create_short_toot(self):
    tootComposer = TootComposer(toot = self.shortToot)
    toots = tootComposer.fill()
    self.assertEqual(len(toots), 1)
    self.assertEqual(toots[0], "Hello world")

  def test_create_long_toot(self):
    tootComposer = TootComposer(toot = self.longToot)
    toots = tootComposer.fill()
    self.assertEqual(len(toots), 2)

  def test_empty_toot(self):
    tootComposer = TootComposer(toot = [])
    toots = tootComposer.fill()
    self.assertEqual(len(toots), 0)

if __name__ == '__main__':
  unittest.main(verbosity=2)