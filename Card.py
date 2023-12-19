import random

class Cards:
  def __init__(self):
    self.colors = ['red', 'orange', 'yellow', 'purple', 'blue', 'green']
    self.special = ['peppermint', 'peanut', 'icecream', 'lollipop']

    self.deck = []
    self.discard = []

    self.makeDeck()
    self.shuffle()
   
  def makeDeck(self):
    for color in self.colors:
      for i in range(6):
        self.deck.append((color, 1))
      for i in range(4):
        self.deck.append((color, 2))
    for char in self.special:
      self.deck.append((char, 'filler'))

  def shuffle(self):
    for i in range(3):
      random.shuffle(self.deck)

  def reshuffle(self):
    self.deck = self.discard
    self.discard = []
    self.shuffle()

  def emptyDeck(self):
    return len(self.deck) == 0
  
  def draw(self):
    if self.emptyDeck():
      self.reshuffle()
    card = self.deck.pop()
    self.discard.append(card)
    return card 