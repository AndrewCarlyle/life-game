import random

PLAYER_NUM = 1

class Player:
    #define player attributes
    def __init__(self,
                 rand,
                 sex=None, #char ('M' or 'F')
                 speed=None,#=round(random.normalvariate(5, 1.5)), #int
                 strength=None, #int
                 attractiveness=None, #int
                 iq=None, #int
                 fertility=None, #int
                 friendliness=None, #int - how likely the player is to be friendly (mate, share) vs start conflict with another player
                 vision=None #int
                 ):
        if rand:
            self.sex = random.choice(['M', 'F'])
            self.speed = round(random.normalvariate(5, 1.5))
            self.strength = round(random.normalvariate(5, 1.5))
            self.attractiveness = round(random.normalvariate(5, 1.5))
            self.iq = round(random.normalvariate(100, 15))
            self.fertility = round(random.normalvariate(5, 1.5))
            self.friendliness = round(random.normalvariate(5, 1.5))
            self.vision = round(random.normalvariate(5, 1.5))
        else:
            self.sex = sex
            self.speed = speed
            self.strength = strength
            self.attractiveness = attractiveness
            self.iq = iq
            self.fertility = fertility
            self.friendliness = friendliness
            self.vision = vision

        self.hunger = 0
        self.energy = 75
        self.reproduceStatus = True
        self.age = 0
        self.X = 0
        self.Y = 0

        self.children = []
        self.friends = []

        global PLAYER_NUM
        self.num = PLAYER_NUM
        PLAYER_NUM += 1

    def print(self):
        print("Player", self.num, "attributes:\nSpeed:", self.speed, "Strength:", self.strength, "Attractiveness:", self.attractiveness, "IQ:", self.iq, "Fertility:", self.fertility, "Friendliness:", self.friendliness)

    def getOlder(self):
        self.age = self.age + 1

    def reproduce(self, player):
        #Players are mating and should not kill each other in the future
        if player not in self.friends:
            self.friends.append(player)
            player.friends.append(self)

        if self.sex == player.sex or self.reproduceStatus or player.reproduceStatus:
            return False

        num = random.randint(1, 10)

        if (self.fertility + player.fertility) / 2 > num:
            self.reproduceStatus = True
            player.reproduceStatus = True

            child = Player(False,
                          speed=round((self.speed+player.speed)/2 + random.randint(-1, 1)),
                          strength=round((self.strength+player.strength)/2 + random.randint(-1, 1)),
                          attractiveness=round((self.attractiveness+player.attractiveness)/2 + random.randint(-1, 1)),
                          iq=round((self.iq+player.iq)/2 + random.randint(-10, 10)),
                          fertility=round((self.fertility+player.fertility)/2 + random.randint(-1, 1)),
                          friendliness=round((self.friendliness+player.friendliness)/2 + random.randint(-1, 1)),
                          vision=round((self.vision+player.vision)/2 + random.randint(-1, 1)))

            self.children.append(child)
            player.children.append(child)
            return child
        else:
            return False

    #Function to have a player decide where to move
    #Returns a tuple (X,Y), where either can be + or -
    def moveDecision(self, world):
        foodInRange = []
        playersInRange = []

        #Loop through squares within range (vision) to look for players/food
        for x in range(max(0, self.X-self.vision), min(self.X+self.vision, world.xSize-1)):
            remainingRange = self.vision - abs(self.X - x)
            for y in range(max(0, self.Y-remainingRange), min(self.Y+remainingRange, world.ySize-1)):
                for item in world.world[x][y]:
                    if item == "food":
                        obj = {"x": x, "y": y, "distance": abs(self.X - x) + abs(self.Y - y)}
                        foodInRange.append(obj)
                    else:
                        obj = {"x": x, "y": y, "player": item, "distance": abs(self.X - x) + abs(self.Y - y)}

        if foodInRange:
            closest = foodInRange[0]
            closestEmpty = None

            for food in foodInRange:
                if food["distance"] < closest["distance"]:
                    closest = food

                #Avoid fight and go to different food if closer
                if (closestEmpty == None or food["distance"] < closestEmpty["distance"]) and type(self) not in world.world[food["x"]][food["y"]]:
                    closestEmpty = food

            if closestEmpty != None:
                closest = closestEmpty

            if closest["distance"] > self.speed:
                #loop until distance = speed
                decision = [closest["x"] - self.X, closest["y"] - self.Y]

                for i in range(closest["distance"] - self.speed):
                    if decision[0] != 0:
                        #move one closer to 0, whether the current num is above or below 0
                        decision[0] -= int(decision[0] / abs(decision[0]))
                    else:
                        #move one closer to 0, whether the current num is above or below 0
                        decision[1] -= int(decision[1] / abs(decision[1]))

                return (decision[0], decision[1])

            return (closest["x"] - self.X, closest["y"] - self.Y)
        else:
            #random direction/distance
            x = random.randint(-self.speed, self.speed)
            y = random.randint(-self.speed + x, self.speed - x)

            return (x,y)

    #When two players are in the same square, they must decide to fight, mate, or be friendly
    def interactionDecision(self, player, numFood, numPlayers):
        Mnum = random.normalvariate(5, 1.5)
        Fnum = random.normalvariate(5, 1.5)

        #Players decide to mate, return 'M' for mate
        if self.sex != player.sex and abs(player.attractiveness - self.attractiveness) < 2:
            return 'M'
        #Both players decide to fight, return 'F' for fight
        elif numFood > 0 and numFood < numPlayers and self.friendliness < Fnum and player.friendliness < Fnum and (not player in self.children) and (not self in player.children) and (not self in player.friends):
            return 'F'
        elif player not in self.friends:
            self.friends.append(player)
            player.friends.append(self)

    #Determines the outcome when two player decide to fight, returns the loser
    def fight(self, player):
        #Modify the players strength but +/- 1
        p1Mod = random.randint(-1,1)
        p2Mod = random.randint(-1,1)

        if self.strength + p1Mod > player.strength + p2Mod:
            return player
        elif self.strength + p1Mod < player.strength + p2Mod:
            return self

    def setLocation(self, x, y):
        self.X = x
        self.Y = y
