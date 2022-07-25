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

        #player.X = x
        #player.Y = y
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

    #Checks to see if a player has landed (collided) with food or another player
    def checkCollisions(self):
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
