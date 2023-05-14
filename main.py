from Player import BasicPlayer, HiloTablePlayer, HiloBasicPlayer
from Deck import Deck
from Hand import Hand
from handle_hand import handle_hand
from Game import round, check_if_won

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

n = 0
import matplotlib.pyplot as plt

rounds = [n]
if __name__ == "__main__":
    basic = BasicPlayer(money=START_MONEY)
    hilo_table = HiloTablePlayer(money=START_MONEY)
    hilo_basic = HiloBasicPlayer(money=START_MONEY)
    deck = Deck()
    players = [hilo_basic, basic, hilo_table]  # , basic]

    while n < N:
        n += 1
        rounds.append(n)
        for player in players:
            player.money_per_round = []
            player.money = START_MONEY

        for i in range(ROUND_LIMIT):
            round(players=players, deck=deck)

        for player in players:
            while len(player.money_per_round) < ROUND_LIMIT:
                player.money_per_round.append(0)
            player.money_per_round_per_game.append(player.money_per_round)

    plt.plot(range(ROUND_LIMIT), hilo_basic.avg_money(), color="b")
    plt.plot(range(ROUND_LIMIT), basic.avg_money(), color="r")
    # plt.plot(range(ROUND_LIMIT), hilo_table.avg_money(), color="g")
    plt.show()

    import numpy as np

    # plt.hist(hilo_table.hand_sum_per_round, bins=50)
    # plt.xticks(np.arange(0, 21, 1))
    # plt.show()
#
