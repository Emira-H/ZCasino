from random import randrange
from math import ceil

def choice_bet():
    bet = 0
    money = 10

    # demander la mise
    while bet <= 0 or bet > money:
        bet = input("veuillez entrer votre mise: ")
        try:
            bet = int(bet)
            print("Vous avez misé {}$".format(bet))
        except ValueError:
            print("votre saisie n'est pas valide. Vous devez saisir un nombre! ")
            bet = -1
            continue
        if bet <= 0:
            print("La mise saisie doit être supérieure à 0")
        if bet > money:
            print("La mise ne peut être supérieure à votre réserve d'argent!")
    return bet

def choice_number():
    number_player = -1
    while number_player not in range(0,50):
        number_player = input("Veuillez choisir un numéro compris entre 0 et 49: ")
        try:
            number_player = int(number_player)
            print("Vous avez choisi de jouer le numéro {}".format(number_player))
            print("Le croupier lance la roulette!")
        except ValueError:
            print("Votre saisie n'est pas valide. Vous devez saisir un nombre! ")
            number_player = -1
            continue
        if number_player not in range(0,50):
            print("Le numéro choisi doit être compris entre 0 et 49")
    number_roulette = randrange(50)
    print("La numéro sur lequel la bille s'arrête est {}".format(number_roulette))
    return (number_player,number_roulette)

def calculate_gain(money):
    bet = choice_bet()
    tuple_number=(number_player,number_roulette) = choice_number()
    if tuple_number[0] == tuple_number[1]:
        gain = 3 * bet
        money += money + gain
        print(" Bravo c'est le jackpot! Vous avez gagné {}!".format(gain))
    elif (tuple_number[0] % 2 == 0 and tuple_number[1] % 2 == 0) or (tuple_number[0] % 2 != 0 and tuple_number[1] % 2 != 0):
        gain = ceil(0.5 * bet)
        money += gain
        print("Vous récupérez la moitié de votre mise soit {}$".format(gain))
    else:
        gain = 0
        money -= bet
        print("Vous avez perdu votre mise de {}$".format(bet))
    return money
