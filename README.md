# TP CASINO OPENCLASSROOM 

It will be a small game of roulette very simplified in which you can bet a certain amount and win or lose money (such is the fortune, the casino!). When you run out of money, you have lost.
Our rules of the game

Well, the roulette is very nice as a game, but a little too complicated for a first TP. So, we will simplify the rules and I present you right away what we get:

    The player bet on a number between 0 and 49 (50 numbers in all). By choosing his number, he deposits the amount he wants to bet.

    The roulette consists of 50 boxes naturally ranging from 0 to 49. The even numbers are black, the odd numbers are red. The dealer throws the roulette, drops the ball and when the roulette stops, raises the number of the box in which the ball has stopped. In our program, we will not repeat all these details "material" but these explanations are also for those who have had the chance to avoid the casino rooms so far. The number on which the ball stopped is, of course, the winning number.

    If the winning number is the one on which the player has bet (probability of 1/50, rather weak), the dealer gives him 3 times the amount wagered.

    Otherwise, the dealer looks to see if the number bet by the player is the same color as the winning number (if they are both odd or even odd). If so, the dealer gives him 50% of the bet. If this is not the case, the player loses his bet.

In the two winning scenarios seen above (the number wagered and the winning number are identical or have the same color), the dealer gives the player the amount initially wagered before adding his winnings. This means that in both scenarios the player gets money. Only in the third case does he lose the sum bet. We will use for dollar currency $ instead of the euro for encoding reasons under the Windows console.


