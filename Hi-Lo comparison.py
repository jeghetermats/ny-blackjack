from Player import BasicPlayer, HiloBasicPlayer
from Deck import Deck
from Game import round, check_if_won
import matplotlib.pyplot as plt
import numpy as np


N = 1000
basic_player = BasicPlayer(money=1000)
hilo_player = HiloBasicPlayer(money=1000)
deck = Deck()

players = [basic_player, hilo_player]


for i in range(N):
    results = round(players, deck)
