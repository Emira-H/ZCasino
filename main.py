from tp_casino import choice_bet, choice_number, calculate_gain

replay = True
gain = 0
money = 100
while replay == True:
    money = calculate_gain(money)
    print("Votre réserve de jeu s'élève désormais de {}".format(money))
    replay_game = input("Voulez-vous rejouer? Tapez O pour rejouer").upper()
    if replay_game == "O":
        replay == True
    else:
        replay == False
