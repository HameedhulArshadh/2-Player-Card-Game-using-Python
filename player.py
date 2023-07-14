from cards import Cards


class Player(Cards):
    def __init__(self, BothDecks):
        self.player1 = BothDecks[0]
        self.player2 = BothDecks[1]
        self.player1Count = len(BothDecks[0])
        self.player2Count = len(BothDecks[1])

    def getFirstPlayerHand(self):
        return self.player1

    def getSecondPlayerHand(self):
        return self.player2

    def UpdateCount(self):
        self.player1Count = len(self.player1)
        self.player2Count = len(self.player2)

    def play(self):
        reserve = []
        count = 1
        while self.player2Count != 0 and self.player1Count != 0:
            input("Press enter to play...  ")
            self.countUpdate()
            print("\n\n\n")
            print("We are playing the round number ", count)
            count = count + 1
            print("Player 1 Hand:")
            print(self.player1)
            print("Player 2 Hand:")
            print(self.player2)

            if self.player1Count == 0 or self.player2Count == 0:
                self.winner()
                break
            else:
                if super().cardValue(self.player1[0]) > super().cardValue(self.player2[0]):
                    # player 1 wins as his card value is higher than the second players card value
                    self.player1.append(self.player1.pop(0))
                    self.player1.append(self.player2.pop(0))
                    if reserve != []:
                        for card in reserve:
                            self.player1.append(card)
                        reserve = []
                    print("Player 1 wins the round!")


                elif super().cardValue(self.player1[0]) < super().cardValue(self.player2[0]):
                    # player 2 wins as his card value is higher than the first players card value
                    self.player2.append(self.player2.pop(0))
                    self.player2.append(self.player1.pop(0))
                    if reserve != []:
                        for card in reserve:
                            self.player2.append(card)
                        reserve = []
                    print("Player 2 wins the round!")

                elif super().cardValue(self.player1[0]) == super().cardValue(self.player2[0]):
                    # both players are at a tie, so we will check next tiebreaker
                    reserve.append(self.player2.pop(0))
                    reserve.append(self.player1.pop(0))
                    print("It is a tie this round!")

    def countUpdate(self):
        self.player1Count = len(self.player1)
        self.player2Count = len(self.player2)

    def winner(self):
        if self.player1Count > self.player2Count:
            print("Player 1 wins!")
        else:
            print("Player 2 wins!")
