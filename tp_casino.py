
from random import randint

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
    number = -1
    while number not in range(0,50):
        try:
            number = input("Veuillez choisir un numéro compris entre 0 et 49: ")
            number = int(number)
            print("Vous avez choisi de jouer le numéro {}".format(number))
        except ValueError:
            print("Votre saisie n'est pas valide. Vous devez saisir un nombre! ")
            number = -1
            continue
        if number not in range(0,50):
            print("Le numéro choisi doit être compris entre 0 et 49")
    return number
choice_number()
