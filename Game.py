from Hand import Hand
from handle_hand import handle_hand

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


def round(players, deck):
    results = []
    for player in players:
        player.hands = []

    dealer_cards = []
    while sum(dealer_cards) < 17:
        card = deck.get_card()
        dealer_cards.append(card)

    for player in players:
        if player.money <= 0:
            player.money = 0
            player.money_per_round.append(player.money)
            continue

        card1 = deck.get_card()
        card2 = deck.get_card()
        new_hand = Hand(cards=[card1, card2], bet=player.make_bet(deck))
        player.hands.append(new_hand)
        player.hand_sum_per_round.append(card1 + card2)
        handle_hand(deck=deck, player=player, hand=new_hand, top_card=dealer_cards[0])
        for hand in player.hands:
            if DEBUGGING:
                print("player hand", hand.cards)
            results.append(
                check_if_won(player=player, hand=hand, dealer_cards=dealer_cards)
            )
        player.money_per_round.append(player.money)
    return results


def check_if_won(player, hand, dealer_cards):
    # print("hand", hand.cards)
    # print(dealer_cards)
    if DEBUGGING:
        print("---------CHECKING IF HAND WON--------")
    if DEBUGGING:
        print("checking if hand", hand.cards, "wins with bet", hand.bet)
    if DEBUGGING:
        print("dealer hand is", dealer_cards)
    if DEBUGGING:
        print("money before", player.money)
    hand.update()

    if hand.surrender:
        # player loses bet amount when making the hand, so we return half of the bet
        player.money += hand.bet / 2
        if DEBUGGING:
            print("surrendered")
        if DEBUGGING:
            print("money after", player.money)
        if DEBUGGING:
            print("---------FINISHED CHECKING IF HAND WON--------")
        return -1

    if hand.total > 21:
        if DEBUGGING:
            print("busted")
        if DEBUGGING:
            print("money after", player.money)
        if DEBUGGING:
            print("---------FINISHED CHECKING IF HAND WON--------")
        return -1

    if sum(dealer_cards) > 21:
        player.money += hand.bet * BET_RETURN
        if DEBUGGING:
            print("dealer busted")
        if DEBUGGING:
            print("money after", player.money)
        if DEBUGGING:
            print("---------FINISHED CHECKING IF HAND WON--------")
        return 1

    if hand.total > sum(dealer_cards):
        player.money += hand.bet * BET_RETURN
        if DEBUGGING:
            print("won")
        if DEBUGGING:
            print("money after", player.money)
        if DEBUGGING:
            print("---------FINISHED CHECKING IF HAND WON--------")
        return 1

    if hand.total == sum(dealer_cards):
        player.money += hand.bet
        return 0

    if hand.total < sum(dealer_cards):
        return -1

    if DEBUGGING:
        print("lost")
    if DEBUGGING:
        print("money after", player.money)
    if DEBUGGING:
        print("---------FINISHED CHECKING IF HAND WON--------")
