"""
 This program is for a 2 player card game
 Rules:
    1. Each player will get 26 cards for a 52 card deck.
    2. Cards are assigned in a random manner.
    3. With each round, players can play the cards in the same order they received it.
    4. Each card is assigned a value
    5. Individual cards are ranked, from highest to lowest: A, K, Q, J, 10, 9, 8, 7, 6, 5, 4, 3 and 2
    6. If one player's card is has a higher value then that player will be awarded as the winner for that round.
    7. Winner gets the cards played during that hand.
    8. If both players are having the same value of card, then the hand goes until we get a tiebreaker or one player runs out of cards to play.
"""


# imports
from deck import Deck
from player import Player


if __name__ == '__main__':
    decks = Deck()
    deckForPlayers = decks.buildDecks()
    player = Player(deckForPlayers)
    player.play()






