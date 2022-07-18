from random import randint

X_SIZE = 25
Y_SIZE = 25

#class used to keep track of the players/food using a data structure
#The data strucutre is a 3D list, which represents a 2D world, where each place
#in the world has a list of player food (the list for a space can be empty)
class World:
    def __init__(self, players, numFood):
        self.world = []
        self.playerList = []

        #init the 3D list
        for x in range(X_SIZE):
            self.world.append([])
            for y in range(Y_SIZE):
                self.world[x].append([])

        #Randomly assign player to a place in the world
        for player in players:
            self.addPlayer(player)

        self.addFood(numFood)

    def addFood(self, numFood):
        #Add food to the world
        for i in range(numFood):
            x = randint(0, X_SIZE-1)
            y = randint(0, Y_SIZE-1)

            self.world[x][y].append("food")

    def addPlayer(self, player, x=randint(0, X_SIZE-1), y=randint(0, Y_SIZE-1)):
        player.X = x
        player.Y = y

        self.world[x][y].append(player)
        self.playerList.append(player)

    def movePlayers(self):
        for player in self.playerList:
            #Remove player from old position
            self.world[player.X][player.Y].remove(player)

            direction = randint(1,4)

            #move up
            if direction == 1:
                player.Y -= player.speed
            #move right
            elif direction == 2:
                player.X += player.speed
            #move down
            elif direction == 3:
                player.Y += player.speed
            #move left
            else:
                player.X -= player.speed

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
