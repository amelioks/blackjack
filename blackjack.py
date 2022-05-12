import random
import time

print("Welcome to Blackjack Game")
time.sleep(1)
player_name = input("What is you name? ")
print("Welcome {name}! This is a game of Blackjack.".format(name = player_name))
time.sleep(1)
print("Now, you can start")
time.sleep(1)

deck_card = [2,3,4,5,6,7,8,9,10,10,10,10,11]

player_money = 2500
player_cards = []
dealer_cards = []

player_bet = int(input("Place your bet: "))

def init_player_card():
    player_cards.extend(random.sample(deck_card,2))

def init_dealer_card():
    dealer_cards.extend(random.sample(deck_card,2))

def game_result():
    game_dealer()
    p_card_sum = sum(player_cards)
    d_card_sum = sum(dealer_cards)
    if p_card_sum == 21:
        print("You get a blackjack. Your money now is " + str(player_bet*1.5 + player_money))
    elif p_card_sum > d_card_sum and p_card_sum < 21:
        print("You win. Your money now is " + str(player_bet + player_money))
    elif p_card_sum < d_card_sum and p_card_sum < 21:
        print("You lose. Your money now is " + str(player_money - player_bet))
    elif p_card_sum == d_card_sum and p_card_sum < 21:
        print("Push. Your money now is " + str(player_money))
    else:
        print("You are busted. Your money now is " + str(player_money - player_bet))

def game_play():
    p_card_sum = sum(player_cards)
    if p_card_sum < 21:
        next_player_game = input("Do you want to HIT or STAND? ")
        if next_player_game.lower() == "stand":
            game_result()
        else:
            game_hit()
    else:
        game_result()

def game_hit():
    card_hit = random.sample(deck_card,1)
    player_cards.extend(card_hit)
    print(player_cards)
    game_play()

def game_dealer():
    d_card_sum = sum(dealer_cards)
    if d_card_sum <= 16:
        card_hit = random.sample(deck_card,1)
        dealer_cards.extend(card_hit)


#init cards for player and dealer
init_player_card()
init_dealer_card()

player_card = "Your cards are " + str(player_cards)
print(player_card)
game_play()
dealer_game = "The dealer cards are " + str(dealer_cards)
print(dealer_game)