import player
import world
import random

#Default settings to start the game
NUM_PLAYERS = 100
NUM_FOOD = 50

def main():
    #init players
    playerList = []
    for i in range(NUM_PLAYERS):
        playerList.append(player.Player())

    wd = world.World(playerList, NUM_FOOD)

    for p in playerList:
        p.move()

if __name__ == "__main__":
    main()
