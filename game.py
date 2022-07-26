import player
import world
import random

#Default settings to start the game
NUM_PLAYERS = 5
NUM_FOOD = 5
NUM_ROUNDS = 20

def main():
    #init players
    playerList = []
    for i in range(NUM_PLAYERS):
        playerList.append(player.Player())

    wd = world.World(playerList, NUM_FOOD)

    for i in range(NUM_ROUNDS):
        #wd.print()
        wd.increaseHunger()
        wd.movePlayers()
        wd.checkCollisions()
        wd.checkDeath()
        wd.addFood(1)
        print("\nEnd of turn: ", i, "\n")

    wd.print()
    print("End of game...")
    print("Number of players currently alive: ", len(wd.playerList))

if __name__ == "__main__":
    main()
