class Hand:
    def __init__(self, cards: list, bet: int) -> None:
        self.cards = cards
        self.bet = bet
        self.total = 0
        self.update()

        # extra
        self.surrender = False

    def add_card(self, card):
        self.cards.append(card)
        self.update()

    def update(self):
        self.total = sum(self.cards)
