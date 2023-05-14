import random

from CONSTANTS import (
    START_MONEY,
    SMALLEST_BET,
    BET_RETURN,
    N,
    ROUND_LIMIT,
    NUMBER_OF_DECKS,
    BETTING_UNIT,
    DEBUGGING,
)


class Deck:
    def __init__(self) -> None:
        self.cards = []
        self.card_pile = []
        self.construct_deck()

    def construct_deck(self) -> None:
        self.cards = []
        self.card_pile = []
        # suites = ["h","s","c","d"]
        ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

        for _ in range(4 * NUMBER_OF_DECKS):
            for rank in ranks:
                self.cards.append(rank)

        random.shuffle(self.cards)

    def get_card(self) -> int:
        if len(self.cards) == 0:
            self.construct_deck()
        card = self.cards.pop()
        self.card_pile.append(card)
        return card

    def hilo(self) -> int:
        count = 0
        for card in self.card_pile:
            if card in [2, 3, 4, 5, 6]:
                count += 1
            if card in [10, 11]:
                count -= 1

        true_count = count / NUMBER_OF_DECKS
        if DEBUGGING:
            print(f"{true_count=}")
        bet = max((true_count * BETTING_UNIT), SMALLEST_BET)
        return true_count  # bet
