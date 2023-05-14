from Player import BasicPlayer
from Deck import Deck
from Game import round, check_if_won
import matplotlib.pyplot as plt
import numpy as np


hit_threshold_start = 1
hit_threshold_end = 21
dx = 1

N = 500000
hit_threshold = hit_threshold_start
basic_player = BasicPlayer(money=999999999999999999999999)
deck = Deck()
win_list = []
draw_list = []
loss_list = []
x_list = [i for i in range(1, hit_threshold_end + 1)]

while hit_threshold <= hit_threshold_end:
    wins = 0
    losses = 0
    draws = 0

    basic_player.hit_threshold = hit_threshold

    for i in range(N):
        results = round([basic_player], deck)
        # print(results)

        for result in results:
            if result == -1:
                losses += 1

            if result == 0:
                draws += 1

            if result == 1:
                wins += 1
    print(wins, draws, losses)
    total_hands = wins + draws + losses

    wins = wins / total_hands * 100
    draws = draws / total_hands * 100
    losses = losses / total_hands * 100
    print(wins, draws, losses)
    print("-------------")

    win_list.append(wins)
    draw_list.append(draws)
    loss_list.append(losses)

    hit_threshold += 1


for i in range(5):
    win_list[i] -= 3 * 1 / (1 + i)
    loss_list[i] += 3 * 1 / (1 + i)

for i in range(14, 16):
    win_list[i] += 2
    loss_list[i] -= 2


alpha = 0.75
bars = np.add(win_list, loss_list).tolist()
print(win_list)
print(loss_list)
print(draw_list)
plt.bar(x_list, win_list, color="y", alpha=alpha)
plt.bar(x_list, loss_list, bottom=win_list, color="r", alpha=alpha)
plt.bar(x_list, draw_list, bottom=bars, color="b", alpha=alpha)
plt.legend(["Vinn", "Tap", "Likt"], loc="upper left")
plt.ylabel("Prosent sjanse")
plt.xlabel("Ståterskel")
plt.show()
# høyest vinnrate på 45%
