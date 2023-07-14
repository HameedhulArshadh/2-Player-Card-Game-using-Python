from cards import Cards
import random

class Deck(Cards):
    def __init__(self):
        self.deckIndex = ()
        self.deck1 = []
        self.deck2 = []

    def buildDeckSequence(self):
        randomValues = []
        while len(randomValues) < 52:
            value = random.choice(range(0, 52))
            if value not in randomValues:
                randomValues.append(value)
        self.deckIndex = tuple(randomValues)

    def buildDecks(self):
        self.buildDeckSequence()
        allCards = super().getAllCards()
        for i, value in enumerate(self.deckIndex):
            if i%2==0:
                self.deck1.append(allCards[value])
            else:
                self.deck2.append(allCards[value])

        return (self.deck1, self.deck2)





