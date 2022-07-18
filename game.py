import player
import world
import random

#Default settings to start the game
NUM_PLAYERS = 5
NUM_FOOD = 5

def main():
    #init players
    playerList = []
    for i in range(NUM_PLAYERS):
        playerList.append(player.Player())

    wd = world.World(playerList, NUM_FOOD)

    wd.print()
    print("\nEnd of turn\n")
    wd.movePlayers()
    wd.print()

if __name__ == "__main__":
    main()
