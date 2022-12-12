#Players roll 2 dice multiple times. The results are summed up and the winner is the one who scored the most
# number of points. Write a function that will determine the winner. If the result is the same, then 
# the winner is the one who threw out a large amount in the last round. The function accepts the number of players as input, 
# the number of rounds and displays the course of the game (throws in each round) and the winner. On each dice you can 
# throw out a number from 1 to 6
import random

dice_1 = 0
dice_2 = 0
score = 0
round = 1

add_players = int(input("Enter the number of players: "))
num_players =list(range(1, add_players + 1)) #we record the number of players in the list
players = { } #creating unique players
for x in num_players:
    players ['Player ' + str(x)] = 0

add_rounds = int(input("Number of rounds: "))
rounds = list(range(1, add_rounds + 1 ))#we record the number of rounds in the list

while round != add_rounds: # imitation game
    for y in rounds: # what round
        for z in num_players: #player's turn
            dice_1 = random.randint(1,6)
            dice_2 = random.randint(1,6)#roll the dice
            score = dice_1 + dice_2 #recording points
            players['Player ' + str(z)]+=score #adding points to the player
            print ("Round " + str(y) + " Player " + str(z) + ": " + str(dice_1) + " - " + str(dice_2))
            score=0 #reset the account
    round += 1

for a,b in players.items():# score 
    print("{0}: {1}".format(a,b))

