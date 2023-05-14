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


class Player:
    def __init__(self, money) -> None:
        self.money = money
        self.hands = []
        self.has_split = False

        ##handling average money per game
        self.money_per_round = [money]
        self.money_per_round_per_game = []

        # handling starting sum from hands
        self.hand_sum_per_round = []

    def make_bet(self):
        # Lager bet, så fjernen bet-amounten fra self.money
        bet = 0
        bet = self.money / 10
        self.money -= bet
        return bet

    def make_move(self, hand, top_card):
        # returns types:
        # S = Stand
        # H = Hit
        # Dh = Double (if not allowed, then hit)
        # Ds = Double (if not allowed, then stand)
        # SP = Split
        # Uh = Surrender (if not allowed, then hit)
        # Us = Surrender (if not allowed, then stand)
        # Usp = Surrender (if not allowed, then split)
        pass

    def avg_money(self) -> list:
        if DEBUGGING:
            print("Antall games gjennomsnitt fra:", len(self.money_per_round_per_game))

        avg_money_list = []
        for i in range(ROUND_LIMIT):
            curr_avg = 0
            for j in range(len(self.money_per_round_per_game)):
                curr_avg += self.money_per_round_per_game[j][i]
            curr_avg /= len(self.money_per_round_per_game)
            avg_money_list.append(curr_avg)
        return avg_money_list


class BasicPlayer(Player):
    def __init__(self, money) -> None:
        super().__init__(money)
        self.hit_threshold = 17

    def make_bet(self, deck):
        bet = max(self.money / 10, SMALLEST_BET)
        self.money -= bet
        return bet

    def make_move(self, hand, top_card):
        move = ""
        if hand.total < self.hit_threshold:
            move = "H"
        else:
            move = "S"

        return move


class HiloBasicPlayer(Player):
    def __init__(self, money) -> None:
        super().__init__(money)
        self.hit_threshold = 17

    def make_bet(self, deck):
        bet = deck.hilo()
        bet = max(bet * self.money / 100, SMALLEST_BET)
        self.money -= bet

        return bet

    def make_move(self, hand, top_card):
        move = ""
        if hand.total < self.hit_threshold:
            move = "H"
        else:
            move = "S"

        return move


class TestPlayer(Player):
    def __init__(self, money) -> None:
        super().__init__(money)

    def make_bet(self, deck):
        bet = max(self.money / 10, 1)
        self.money -= bet
        return bet

    def make_move(self, hand, top_card):
        move = ""
        if hand.total < 17:
            move = "H"
        else:
            if self.has_split != True and len(hand.cards) == 2:
                move = "SP"
            else:
                move = "S"
        return move


class HiloTablePlayer(Player):
    def __init__(self, money):
        super().__init__(money)

    def make_bet(self, deck):
        bet = deck.hilo()
        bet = max(bet * self.money / 100, SMALLEST_BET)
        self.money -= bet

        return bet

    def make_move(self, hand, top_card) -> str:
        if DEBUGGING:
            print("hand", hand.cards, "top card", top_card)
        play = ""

        pairs_table = {
            (2, 2): "SP",
            (2, 3): "SP",
            (2, 4): "SP",
            (2, 5): "SP",
            (2, 6): "SP",
            (2, 7): "SP",
            (2, 8): "H",
            (2, 9): "H",
            (2, 10): "H",
            (2, 11): "H",
            (3, 2): "SP",
            (3, 3): "SP",
            (3, 4): "SP",
            (3, 5): "SP",
            (3, 6): "SP",
            (3, 7): "SP",
            (3, 8): "H",
            (3, 9): "H",
            (3, 10): "H",
            (3, 11): "H",
            (4, 2): "H",
            (4, 3): "H",
            (4, 4): "H",
            (4, 5): "SP",
            (4, 6): "SP",
            (4, 7): "H",
            (4, 8): "H",
            (4, 9): "H",
            (4, 10): "H",
            (4, 11): "H",
            (5, 2): "DH",
            (5, 3): "DH",
            (5, 4): "DH",
            (5, 5): "DH",
            (5, 6): "DH",
            (5, 7): "DH",
            (5, 8): "DH",
            (5, 9): "DH",
            (5, 10): "H",
            (5, 11): "H",
            (6, 2): "SP",
            (6, 3): "SP",
            (6, 4): "SP",
            (6, 5): "SP",
            (6, 6): "SP",
            (6, 7): "H",
            (6, 8): "H",
            (6, 9): "H",
            (6, 10): "H",
            (6, 11): "H",
            (7, 2): "SP",
            (7, 3): "SP",
            (7, 4): "SP",
            (7, 5): "SP",
            (7, 6): "SP",
            (7, 7): "SP",
            (7, 8): "H",
            (7, 9): "H",
            (7, 10): "H",
            (7, 11): "H",
            (8, 2): "SP",
            (8, 3): "SP",
            (8, 4): "SP",
            (8, 5): "SP",
            (8, 6): "SP",
            (8, 7): "SP",
            (8, 8): "SP",
            (8, 9): "SP",
            (8, 10): "SP",
            (8, 11): "USP",
            (9, 2): "SP",
            (9, 3): "SP",
            (9, 4): "SP",
            (9, 5): "SP",
            (9, 6): "SP",
            (9, 7): "S",
            (9, 8): "SP",
            (9, 9): "SP",
            (9, 10): "S",
            (9, 11): "S",
            (10, 2): "S",
            (10, 3): "S",
            (10, 4): "S",
            (10, 5): "S",
            (10, 6): "S",
            (10, 7): "S",
            (10, 8): "S",
            (10, 9): "S",
            (10, 10): "S",
            (10, 11): "S",
            (11, 2): "SP",
            (11, 3): "SP",
            (11, 4): "SP",
            (11, 5): "SP",
            (11, 6): "SP",
            (11, 7): "SP",
            (11, 8): "SP",
            (11, 9): "SP",
            (11, 10): "SP",
            (11, 11): "SP",
        }
        soft_totals_table = {
            (12, 2): "H",
            (12, 3): "H",
            (12, 4): "H",
            (12, 5): "H",
            (12, 6): "H",
            (12, 7): "H",
            (12, 8): "H",
            (12, 9): "H",
            (12, 10): "H",
            (12, 11): "H",
            (13, 2): "H",
            (13, 3): "H",
            (13, 4): "H",
            (13, 5): "DH",
            (13, 6): "DH",
            (13, 7): "H",
            (13, 8): "H",
            (13, 9): "H",
            (13, 10): "H",
            (13, 11): "H",
            (14, 2): "H",
            (14, 3): "H",
            (14, 4): "H",
            (14, 5): "DH",
            (14, 6): "DH",
            (14, 7): "H",
            (14, 8): "H",
            (14, 9): "H",
            (14, 10): "H",
            (14, 11): "H",
            (15, 2): "H",
            (15, 3): "H",
            (15, 4): "DH",
            (15, 5): "DH",
            (15, 6): "DH",
            (15, 7): "H",
            (15, 8): "H",
            (15, 9): "H",
            (15, 10): "H",
            (15, 11): "H",
            (16, 2): "H",
            (16, 3): "H",
            (16, 4): "DH",
            (16, 5): "DH",
            (16, 6): "DH",
            (16, 7): "H",
            (16, 8): "H",
            (16, 9): "H",
            (16, 10): "H",
            (16, 11): "H",
            (17, 2): "H",
            (17, 3): "DH",
            (17, 4): "DH",
            (17, 5): "DH",
            (17, 6): "DH",
            (17, 7): "H",
            (17, 8): "H",
            (17, 9): "H",
            (17, 10): "H",
            (17, 11): "H",
            (18, 2): "DS",
            (18, 3): "DS",
            (18, 4): "DS",
            (18, 5): "DS",
            (18, 6): "DS",
            (18, 7): "S",
            (18, 8): "S",
            (18, 9): "H",
            (18, 10): "H",
            (18, 11): "H",
            (19, 2): "S",
            (19, 3): "S",
            (19, 4): "S",
            (19, 5): "S",
            (19, 6): "DS",
            (19, 7): "S",
            (19, 8): "S",
            (19, 9): "S",
            (19, 10): "S",
            (19, 11): "S",
            (20, 2): "S",
            (20, 3): "S",
            (20, 4): "S",
            (20, 5): "S",
            (20, 6): "S",
            (20, 7): "S",
            (20, 8): "S",
            (20, 9): "S",
            (20, 10): "S",
            (20, 11): "S",
            (21, 2): "S",
            (21, 3): "S",
            (21, 4): "S",
            (21, 5): "S",
            (21, 6): "S",
            (21, 7): "S",
            (21, 8): "S",
            (21, 9): "S",
            (21, 10): "S",
            (21, 11): "S",
        }
        hard_total_table = {
            (2, 2): "H",
            (2, 3): "H",
            (2, 4): "H",
            (2, 5): "H",
            (2, 6): "H",
            (2, 7): "H",
            (2, 8): "H",
            (2, 9): "H",
            (2, 10): "H",
            (2, 11): "H",
            (3, 2): "H",
            (3, 3): "H",
            (3, 4): "H",
            (3, 5): "H",
            (3, 6): "H",
            (3, 7): "H",
            (3, 8): "H",
            (3, 9): "H",
            (3, 10): "H",
            (3, 11): "H",
            (4, 2): "H",
            (4, 3): "H",
            (4, 4): "H",
            (4, 5): "H",
            (4, 6): "H",
            (4, 7): "H",
            (4, 8): "H",
            (4, 9): "H",
            (4, 10): "H",
            (4, 11): "H",
            (5, 2): "H",
            (5, 3): "H",
            (5, 4): "H",
            (5, 5): "H",
            (5, 6): "H",
            (5, 7): "H",
            (5, 8): "H",
            (5, 9): "H",
            (5, 10): "H",
            (5, 11): "H",
            (6, 2): "H",
            (6, 3): "H",
            (6, 4): "H",
            (6, 5): "H",
            (6, 6): "H",
            (6, 7): "H",
            (6, 8): "H",
            (6, 9): "H",
            (6, 10): "H",
            (6, 11): "H",
            (7, 2): "H",
            (7, 3): "H",
            (7, 4): "H",
            (7, 5): "H",
            (7, 6): "H",
            (7, 7): "H",
            (7, 8): "H",
            (7, 9): "H",
            (7, 10): "H",
            (7, 11): "H",
            (8, 2): "H",
            (8, 3): "H",
            (8, 4): "H",
            (8, 5): "H",
            (8, 6): "H",
            (8, 7): "H",
            (8, 8): "H",
            (8, 9): "H",
            (8, 10): "H",
            (8, 11): "H",
            (9, 2): "H",
            (9, 3): "DH",
            (9, 4): "DH",
            (9, 5): "DH",
            (9, 6): "DH",
            (9, 7): "H",
            (9, 8): "H",
            (9, 9): "H",
            (9, 10): "H",
            (9, 11): "H",
            (10, 2): "DH",
            (10, 3): "DH",
            (10, 4): "DH",
            (10, 5): "DH",
            (10, 6): "DH",
            (10, 7): "DH",
            (10, 8): "DH",
            (10, 9): "DH",
            (10, 10): "H",
            (10, 11): "H",
            (11, 2): "DH",
            (11, 3): "DH",
            (11, 4): "DH",
            (11, 5): "DH",
            (11, 6): "DH",
            (11, 7): "DH",
            (11, 8): "DH",
            (11, 9): "DH",
            (11, 10): "DH",
            (11, 11): "DH",
            (12, 2): "H",
            (12, 3): "H",
            (12, 4): "S",
            (12, 5): "S",
            (12, 6): "S",
            (12, 7): "H",
            (12, 8): "H",
            (12, 9): "H",
            (12, 10): "H",
            (12, 11): "H",
            (13, 2): "S",
            (13, 3): "S",
            (13, 4): "S",
            (13, 5): "S",
            (13, 6): "S",
            (13, 7): "H",
            (13, 8): "H",
            (13, 9): "H",
            (13, 10): "H",
            (13, 11): "H",
            (14, 2): "S",
            (14, 3): "S",
            (14, 4): "S",
            (14, 5): "S",
            (14, 6): "S",
            (14, 7): "H",
            (14, 8): "H",
            (14, 9): "H",
            (14, 10): "H",
            (14, 11): "H",
            (15, 2): "S",
            (15, 3): "S",
            (15, 4): "S",
            (15, 5): "S",
            (15, 6): "S",
            (15, 7): "H",
            (15, 8): "H",
            (15, 9): "H",
            (15, 10): "UH",
            (15, 11): "UH",
            (16, 2): "S",
            (16, 3): "S",
            (16, 4): "S",
            (16, 5): "S",
            (16, 6): "S",
            (16, 7): "H",
            (16, 8): "H",
            (16, 9): "UH",
            (16, 10): "UH",
            (16, 11): "UH",
            (17, 2): "S",
            (17, 3): "S",
            (17, 4): "S",
            (17, 5): "S",
            (17, 6): "S",
            (17, 7): "S",
            (17, 8): "S",
            (17, 9): "S",
            (17, 10): "S",
            (17, 11): "US",
            (18, 2): "S",
            (18, 3): "S",
            (18, 4): "S",
            (18, 5): "S",
            (18, 6): "S",
            (18, 7): "S",
            (18, 8): "S",
            (18, 9): "S",
            (18, 10): "S",
            (18, 11): "S",
            (19, 2): "S",
            (19, 3): "S",
            (19, 4): "S",
            (19, 5): "S",
            (19, 6): "S",
            (19, 7): "S",
            (19, 8): "S",
            (19, 9): "S",
            (19, 10): "S",
            (19, 11): "S",
            (20, 2): "S",
            (20, 3): "S",
            (20, 4): "S",
            (20, 5): "S",
            (20, 6): "S",
            (20, 7): "S",
            (20, 8): "S",
            (20, 9): "S",
            (20, 10): "S",
            (20, 11): "S",
            (21, 2): "S",
            (21, 3): "S",
            (21, 4): "S",
            (21, 5): "S",
            (21, 6): "S",
            (21, 7): "S",
            (21, 8): "S",
            (21, 9): "S",
            (21, 10): "S",
            (21, 11): "S",
        }

        # if DEBUGGING: print("---table strategy")

        if (
            len(hand.cards) == 2
            and self.has_split == False
            and hand.cards[0] == hand.cards[1]
        ):
            # if DEBUGGING: print("---next_play: pair")
            # par
            play = pairs_table[(hand.cards[0], top_card)]

        elif len(hand.cards) == 2 and 11 in hand.cards:
            # if DEBUGGING: print("---next_play: soft totals")
            # soft totals
            # if DEBUGGING: print(sum(hand.cards), top_card)
            play = soft_totals_table[(sum(hand.cards), top_card)]

        else:
            # hard totals
            # if DEBUGGING: print("---next_play: hard totals")
            play = hard_total_table[(sum(hand.cards), top_card)]
        # if DEBUGGING: print("---next_play: play for hand", hand.cards, "is", play)

        return play
