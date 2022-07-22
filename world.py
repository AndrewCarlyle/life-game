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
            x = randint(0, xSize-1)
            y = randint(0, ySize-1)

            self.world[x][y].append("food")

    def addPlayer(self, player, x=randint(0, xSize-1), y=randint(0, ySize-1)):
        player.X = x
        player.Y = y

        self.world[x][y].append(player)
        self.playerList.append(player)

    def movePlayers(self):
        for player in self.playerList:
            #Remove player from old position
            self.world[player.X][player.Y].remove(player)

            move = player.moveDecision(self)

            #update player X/Y, ensure player is still within array by use min/max
            player.X = min(max(move[0], 0), xSize-1)
            player.Y = min(max(move[1], 0), ySize-1)

            '''direction = randint(1,4)

            #move up
            if direction == 1:
                player.Y = max(player.Y - player.speed, 0)
            #move right
            elif direction == 2:
                player.X = min(player.X + player.speed, xSize-1)
            #move down
            elif direction == 3:
                player.Y = min(player.Y + player.speed, ySize-1)
            #move left
            else:
                player.X = max(player.X - player.speed, 0)'''
            #Add player to new location
            self.world[player.X][player.Y].append(player)

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
