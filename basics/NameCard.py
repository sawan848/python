class Card:
    def __init__(self,rank,suit):
        self.suit=suit
        self.rank=rank
        self.hard,self.soft=self._points()

class NameCard(Card):
    def _points(self):
        return int(self.rank),int(self.rank)

class AceCard(Card):
    def _points(self):
        return 1,11

class FaceCard(Card):
    def _points(self):
        return 10,10
