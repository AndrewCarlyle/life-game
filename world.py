from random import randint

#class used to keep track of the players/food using a data structure
#The data strucutre is a 3D list, which represents a 2D world, where each place
#in the world has a list of player food (the list for a space can be empty)
class World:
    def __init__(self, players, numFood, xSize=25, ySize=25):
        self.world = []
        self.playerList = []

        self.xSize = xSize
        self.ySize = ySize

        self.deathCount = 0
        self.birthCount = 0
        self.fightCount = 0

        #init the 3D list
        for x in range(xSize):
            self.world.append([])
            for y in range(ySize):
                self.world[x].append([])

        #Randomly assign player to a place in the world
        for player in players:
            self.addPlayer(player)

        self.addFood(numFood)

    def addFood(self, numFood):
        #Add food to the world
        for i in range(numFood):
            x = randint(0, self.xSize-1)
            y = randint(0, self.ySize-1)

            self.world[x][y].append("food")

    def addPlayer(self, player, x=-1, y=-1):
        if x == -1:
            x = randint(0, self.xSize-1)

        if y == -1:
            y=randint(0, self.ySize-1)

        player.setLocation(x, y)

        self.world[x][y].append(player)
        self.playerList.append(player)

    def movePlayers(self):
        for player in self.playerList:
            #Remove player from old position
            self.world[player.X][player.Y].remove(player)

            move = player.moveDecision(self)

            #update player X/Y, ensure player is still within array by use min/max
            player.X = min(max(move[0] + player.X, 0), self.xSize-1)
            player.Y = min(max(move[1] + player.Y, 0), self.ySize-1)

            #Add player to new location
            self.world[player.X][player.Y].append(player)
            player.energy -= abs(move[0]) + abs(move[1])

    def print(self):
        for row in self.world:
            str=""

            for column in row:
                if len(column) > 1:
                    str += "M"
                elif column == ["food"]:
                    str += "F"
                elif column == []:
                    str += "-"
                else:
                    str += "P"

            print(str)

    def increaseHunger(self):
        for player in self.playerList:
            player.hunger += 1

    #Checks to see if a player has landed on food
    def checkFood(self):
        for player in self.playerList:
            if len(self.world[player.X][player.Y]) > 1:
                for item in self.world[player.X][player.Y]:
                    #player eats the food
                    if item == "food":
                        #Resets to zero for now, but could just go down by a certain amount (or varying amount --> different food)
                        player.hunger = 0
                        player.energy += 10

                        self.world[player.X][player.Y].remove(item)

                        break

    #Checks to see if a player has landed on (collided) another player
    def checkCollisions(self):
        removedList = []

        for player in self.playerList:
            if len(self.world[player.X][player.Y]) > 1 :
                for item in self.world[player.X][player.Y]:
                    if item != "food" and item != player:
                        #foodPresent = "food" in self.world[player.X][player.Y]
                        #Find the numbe of food in the current square
                        numFood = 0
                        numPlayers = 0

                        for i in self.world[player.X][player.Y]:
                            if i == "food":
                                numFood += 1
                            else:
                                numPlayers += 1

                        #Players may choose to fight, reproduce or remain friendly
                        choice = player.interactionDecision(item, numFood, numPlayers)

                        if choice == 'M':
                            result = player.reproduce(item)

                            if result != False:
                                self.addPlayer(result, player.X, player.Y)
                                self.birthCount += 1

                        elif choice == 'F':
                            result = player.fight(item)

                            if result:
                                self.deathCount += 1
                                self.fightCount += 1

                                self.world[player.X][player.Y].remove(result)
                                self.playerList.remove(result)
                                removedList.append(result)

                                if result == player:
                                    break


    def checkDeath(self):
        for player in self.playerList:
            if player.hunger >= 10 or player.energy <= 0:
                self.deathCount += 1
                self.world[player.X][player.Y].remove(player)
                self.playerList.remove(player)

                #Game ends if all players are dead
                if self.playerList == []:
                    return True

    def agePlayers(self):
        for player in self.playerList:
            player.getOlder()

    def resetReproduce(self):
        for player in self.playerList:
            player.reproduceStatus = False

    def printAvgStats(self):
        speedTotal = 0
        strengthTotal = 0
        attractivenessTotal = 0
        iqTotal = 0
        fertilityTotal = 0
        friendlinessTotal = 0
        hungerTotal = 0
        energyTotal = 0
        ageTotal = 0

        for player in self.playerList:
