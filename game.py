import player
import world
import random

#Default settings to start the game
NUM_PLAYERS = 100
NUM_FOOD = 50

def main():
    #init players
    for i in range(NUM_PLAYERS):
        sex = random.choice(['M', 'F'])

    plr = player.player(1,1,1,1,1)

    #wd = world.World(NUM_PLAYERS, NUM_FOOD)

if __name__ == "__main__":
    main()
