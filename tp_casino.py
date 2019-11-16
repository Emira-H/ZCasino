
from random import randrange

def choice_bet():
    bet = -1
    # demander la mise
    while bet <= 0:
        try:
            bet = input("veuillez entrer votre mise: ")
            bet = int(bet)
        except ValueError:
            print("votre saisie n'est pas valide. Vous devez saisir un nombre! ")
            bet = -1
            continue
        if bet <= 0:
            print("La mise saisie doit être supérieure à 0")
    return bet
choice_bet()

def choice_number():
    number_player = -1
    while number_player not in range(0,50):
        try:
            number_player = input("Veuillez choisir un numéro compris entre 0 et 49: ")
            number_player = int(number_player)
            print("Vous avez choisi de jouer le numéro {}".format(number_player))
            print("Le croupier lance la roulette!")
        except ValueError:
            print("Votre saisie n'est pas valide. Vous devez saisir un nombre! ")
            number_player = -1
            continue
        if number_player not in range(0,50):
            print("Le numéro choisi doit être compris entre 0 et 49")
            return number_player
    number_roulette = randrange(50)
    print("La numéro sur lequel la bille s'arrête est {}".format(number_roulette))
    return number_roulette
choice_number()
