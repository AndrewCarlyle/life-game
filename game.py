import player
import world
import random

#Default settings to start the game
NUM_PLAYERS = 10
NUM_FOOD = 10
NUM_ROUNDS = 20

def main():
    #init players
    playerList = []
    for i in range(NUM_PLAYERS):
        playerList.append(player.Player(True))

    wd = world.World(playerList, NUM_FOOD)

    for i in range(1,NUM_ROUNDS+1):
        #wd.print()
        wd.increaseHunger()
        wd.movePlayers()
        wd.checkCollisions()
        wd.checkFood()
        wd.checkDeath()
        wd.addFood(1)
        wd.agePlayers()
        wd.resetReproduce()
        print("End of turn: ", i)

    wd.print()
    print("End of game...")
    print("Number of players currently alive: ", len(wd.playerList))

if __name__ == "__main__":
    main()
