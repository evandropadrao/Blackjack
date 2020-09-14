# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import Deck
import Hand

game_in_progress = False
player_playing = False
chip_bool = 100

bet = 1
result = False
deck = None
player_hand = None
dealer_hand = None

restart_phrase = "Press 'd' to suffle again or 'q' to leave the game!"

suits = ('Hearts', 'Spades', 'Diamonds', 'Clubs')
ranking = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
card_val = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}


def make_bet():
    global bet, player_playing
    bet = 0

    print("")
    print("Player chip total is: ", str(chip_bool))
    print("What amount of chips would you like to bet? (enter a whole a integer please)")

    while bet == 0:
        bet_comp = int(input("> "))

        if (bet_comp > 0) and (bet_comp < chip_bool):
            bet = bet_comp
        elif bet_comp == 0:
            print("Invalid bet. You must define a non zero value!")
        else:
            print("Invalid bet. You have only", str(chip_bool), "chips remaining!")

    player_playing = True


def deal_cards():
    global result, game_in_progress, deck, player_hand, dealer_hand, chip_bool, bet

    deck = Deck.Deck()
    deck.shuffle()

    make_bet()

    player_hand = Hand.Hand()
    dealer_hand = Hand.Hand()

    # Distribui 02 cartas para o jogador
    player_hand.card_add(deck.deal())
    player_hand.card_add(deck.deal())

    # Distribui 02 cartas para o mesário
    dealer_hand.card_add(deck.deal())
    dealer_hand.card_add(deck.deal())

    result = "Hit or Stand? (press 'h' or 's') "

    game_in_progress = True
    game_step()


def hit():
    global result, game_in_progress, deck, player_hand, dealer_hand, chip_bool, bet

    if game_in_progress:
        if player_hand.calc_total_value() <= 21:
            player_hand.card_add(deck.deal())

        print("Player hands", player_hand)

        if player_hand.calc_total_value() > 21:
            result = "Bursted! " + restart_phrase
            chip_bool -= bet
            game_in_progress = False

    else:
        result = "Sorry, can't hit!" + restart_phrase

    game_step()


def stand():
    global result, game_in_progress, deck, player_hand, dealer_hand, chip_bool, bet

    if not game_in_progress:
        if player_hand.calc_total_value() > 0:
            result = "Sorry, you can't stand!"

    else:
        while dealer_hand.calc_total_value() < 17:
            dealer_hand.card_add(deck.deal())

        if dealer_hand.calc_total_value() > 21:
            result = "Dealer bursted! You win! " + restart_phrase
            chip_bool += bet
            game_in_progress = False

        elif dealer_hand.calc_total_value() < player_hand.calc_total_value():
            result = "You beat the dealer! " + restart_phrase
            chip_bool += bet
            game_in_progress = False

        elif dealer_hand.calc_total_value() == player_hand.calc_total_value():
            result = "Tied up!" + restart_phrase
            game_in_progress = False

        else:
            result = "The dealer beat you! " + restart_phrase
            chip_bool -= bet
            game_in_progress = False

    game_step()


def game_step():
    global player_playing

    print("")
    print("Player hand is:")
    player_hand.draw(hidden=False, playing=game_in_progress)
    [x, y] = player_hand.calc_current_score(hidden=False)
    if y == 0:
        print("Player hand total is: {}".format(x))
    else:
        print("Player hand total is: {} or {}".format(x,y))

    print("")
    print("Dealer hand is:")
    dealer_hand.draw(hidden=True, playing=game_in_progress)
    [x, y] = dealer_hand.calc_current_score(hidden=player_playing)
    if y == 0:
        print("Player hand total is: {}".format(x))
    else:
        print("Player hand total is: {} or {}".format(x, y))

    print("")
    print(result)

    player_input()


def game_exit():
    print("")
    print("Thanks for playing!")
    exit()


def player_input():
    global player_playing

    plin = input().lower()

    if plin == 'h':
        hit()
    elif plin == 's':
        player_playing = False
        stand()
    elif plin == 'd' and not game_in_progress:
        deal_cards()
    elif plin == 'q' and not game_in_progress:
        game_exit()
    else:
        if game_in_progress:
            print("Invalid input! Try again entering 'h' or 's'!")
        else:
            print("Invalid input! Try again entering 'h', 's', 'd' or 'q'!")
        player_input()


def intro():
    statement = '''Welcome to BlackJack! Get as close to 21 as you can without going over!
        Dealer hits until she reaches 17. Aces count as 1 or 11.
        Card output goes a letter followed by a number of face notation'''
    print(statement)
    print("")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(" *** BLACKJACK ***")

    # deck = Deck.Deck()
    # deck.shuffle()
    #
    # player_hand = Hand.Hand()
    # dealer_hand = Hand.Hand()

    intro()
    deal_cards()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
