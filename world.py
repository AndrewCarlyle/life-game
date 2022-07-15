from random import randint

X_SIZE = 1000
Y_SIZE = 1000

#class used to keep track of the players/food using a data structure
#The data strucutre is a 3D list, which represents a 2D world, where each place
#in the world has a list of player food (the list for a space can be empty)
class world:
    def __init__(self, players, numFood):
        self.world = []

        #init the 3D list
        for x in range(X_SIZE):
            self.world.append([])
            for y in range(Y_SIZE):
                self.world[x].append([])

        #Randomly assign player to a place in the world
        for player in players:
            x = randint(0, X_SIZE-1)
            y = randint(0, Y_SIZE-1)

            self.world[x][y].append([player])

        self.addFood(numFood)

    def addFood(self, numFood):
        #Add food to the world
        for i in range(numFood):
            x = randint(0, X_SIZE-1)
            y = randint(0, Y_SIZE-1)

            self.world[x][y].append("food")
