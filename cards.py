"""
    Individual cards are ranked, from highest to lowest: A, K, Q, J, 10, 9, 8, 7, 6, 5, 4, 3 and 2
"""


class Cards:
    allCards = ('2 Diamond', '3 Diamond', '4 Diamond', '5 Diamond', '6 Diamond', '7 Diamond', '8 Diamond',
                         '9 Diamond', '10 Diamond', 'Jack Diamond', 'Queen Diamond', 'King Diamond', 'Ace Diamond',
                         '2 Clover', '3 Clover', '4 Clover', '5 Clover', '6 Clover', '7 Clover', '8 Clover', '9 Clover',
                         '10 Clover', 'Jack Clover', 'Queen Clover', 'King Clover', 'Ace Clover', '2 Heart', '3 Heart',
                         '4 Heart', '5 Heart', '6 Heart', '7 Heart', '8 Heart', '9 Heart', '10 Heart', 'Jack Heart',
                         'Queen Heart', 'King Heart', 'Ace Heart', '2 Spades', '3 Spades', '4 Spades', '5 Spades',
                         '6 Spades', '7 Spades', '8 Spades', '9 Spades', '10 Spades', 'Jack Spades', 'Queen Spades',
                         'King Spades', 'Ace Spades')
    cardValues = {'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}

    def cardValue(self, card):
        cardInfo = card.split(' ')
        if cardInfo[0] not in self.cardValues.keys() and cardInfo[0] in ('2', '3', '4', '5', '6', '7', '8', '9', '10'):
            cardValue = cardInfo[0]
            return int(cardValue)
        else:
            try:
                cardValue = self.cardValues[cardInfo[0]]
                return int(cardValue)
            except:
                raise "Please provide a valid card for valuation"

    def getAllCards(self):
        return self.allCards
