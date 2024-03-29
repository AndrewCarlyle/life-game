import player
import world
import random
import image
from time import sleep

#Default settings to start the game
NUM_PLAYERS = 50
NUM_FOOD = 100
FOOD_PER_TURN = 25
NUM_ROUNDS = 400
X_SIZE = 80
Y_SIZE = 80
TURN_TIME = 0.25
GUI_ENABLED = False

def main():
    #init players
    playerList = []
    for i in range(NUM_PLAYERS):
        playerList.append(player.Player(True))

    wd = world.World(playerList, NUM_FOOD, X_SIZE, Y_SIZE)
    wd.printAvgStats()

    if GUI_ENABLED:
        img = image.Image(wd)
        img.drawWorld()

    for i in range(1,NUM_ROUNDS+1):
        #wd.print()
        wd.increaseHunger()
        wd.movePlayers()
        wd.checkCollisions()
        wd.checkFood()
        result = wd.checkDeath()
        wd.addFood(FOOD_PER_TURN)
        wd.agePlayers()
        wd.resetReproduce()

        if GUI_ENABLED:
            img.drawWorld()
            sleep(TURN_TIME)

        #print("End of turn: ", i)

        if result:
            print("Game over, all players are dead...")
            break

    #wd.print()
    print("End of game...")
    print("Number of players currently alive: ", len(wd.playerList))
    print("Total number of births: ", wd.birthCount)
    print("Total number of deaths: ", wd.deathCount)
    print("Total number of fight deaths: ", wd.fightCount)

    #for plr in wd.playerList:
    #    plr.print()

    if len(wd.playerList) > 0:
        wd.printAvgStats()

    if GUI_ENABLED:
        print("Click Image to exit.")
        img.endGame()

if __name__ == "__main__":
    main()
