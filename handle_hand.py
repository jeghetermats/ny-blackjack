from Player import BasicPlayer, TestPlayer
from Deck import Deck
from Hand import Hand

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


def handle_hand(deck: Deck, player, hand: Hand, top_card: int):
    if DEBUGGING:
        print("original hand", hand.cards)
    if DEBUGGING:
        print("playermoney", player.money)
    hand.update()
    if hand.total > 21:
        while 11 in hand.cards and hand.total > 21:
            hand.cards.remove(11)
            hand.add_card(1)

    if hand.total > 21:
        return

    player_move = player.make_move(hand=hand, top_card=top_card)
    if DEBUGGING:
        print("first hitting")
    while player_move == "H":
        card = deck.get_card()
        hand.add_card(card)

        # remove ace if hand busts
        while 11 in hand.cards and hand.total > 21:
            hand.cards.remove(11)
            hand.add_card(1)
        if hand.total <= 21:
            if DEBUGGING:
                print("movig")
            player_move = player.make_move(hand=hand, top_card=top_card)
        else:
            player_move = "S"
    if DEBUGGING:
        print("finished first hitting with hand", hand.cards)
    if player_move == "SP":
        if DEBUGGING:
            print("splitting")
        if player.has_split or len(hand.cards) != 2:
            raise Exception(
                "handle_hand: player has already split or handlength != 2, hand:",
                hand.cards,
            )

        player.has_split = True

        first_card = hand.cards[0]
        second_card = hand.cards[1]
        new_card = deck.get_card()

        hand.cards = [first_card]
        hand.update()

        split_hand = Hand([second_card, new_card], player.make_bet(deck))
        player.hands.append(split_hand)
        handle_hand(deck=deck, player=player, hand=hand, top_card=top_card)
        handle_hand(deck=deck, player=player, hand=split_hand, top_card=top_card)

    while 11 in hand.cards and hand.total > 21:
        hand.cards.remove(11)
        hand.add_card(1)
    if hand.total > 21:
        return
    player_move = player.make_move(hand=hand, top_card=top_card)

    while player_move == "H":
        if DEBUGGING:
            print("player hitting")
        card = deck.get_card()
        hand.add_card(card)
        player_move = player.make_move(hand=hand, top_card=top_card)
        if DEBUGGING:
            print("nnew player_move is", player_move)

    if player_move == "DH" or player_move == "DS":
        if DEBUGGING:
            print("doubling")
        player.money -= hand.bet
        hand.bet *= 2
        card = deck.get_card()
        hand.add_card(card)

    if (
        player_move == "UH"
        or player_move == "US"
        or player_move == "USP"
        # and hand.total < 21
    ):
        if DEBUGGING:
            print("hand surrenders")
        hand.surrender = True


if __name__ == "__main__":
    test = TestPlayer(money=100)
    deck = Deck()
    card1 = deck.get_card()
    card2 = deck.get_card()
    new_hand = Hand(cards=[card1, card2], bet=test.make_bet(deck))
    test.hands.append(new_hand)

    handle_hand(deck, test, new_hand, 18)
