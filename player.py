import random

class Player:
    #define player attributes
    def __init__(self,
                 sex=random.choice(['M', 'F']), #char ('M' or 'F')
                 speed=round(random.normalvariate(5, 1.5)), #int
                 strength=round(random.normalvariate(5, 1.5)), #int
                 attractiveness=round(random.normalvariate(5, 1.5)), #int
                 iq=round(random.normalvariate(100, 15)), #int
                 fertility=round(random.normalvariate(5, 1.5)), #int
                 friendliness=round(random.normalvariate(5, 1.5)), #int - how likely the player is to be friendly (mate, share) vs start conflict with another player
                 ):
        self.sex = sex
        self.speed = speed
        self.strength = strength
        self.attractiveness = attractiveness
        self.iq = iq
        self.fertility = fertility

        self.hunger = 0
        self.energy = 75
        self.age = 0
        self.X = 0
        self.Y = 0

    def getOlder(self):
        self.age = self.age + 1

    def reproduce(self, player):
        if self.sex == player.sex:
            return False

        num = random.randint(1, 10)

        if (self.fertility + player.fertility) / 2 > num:
            return Player(speed=(self.speed+player.speed)/2 + random.randint(-1, 1),
                          strength=(self.strength+player.strength)/2 + random.randint(-1, 1),
                          attractiveness=(self.attractiveness+player.attractiveness)/2 + random.randint(-1, 1),
                          iq=(self.iq+player.iq)/2 + random.randint(-10, 10),
                          fertility=(self.fertility+player.fertility)/2 + random.randint(-1, 1),
                          friendliness=(self.friendliness+player.friendliness)/2 + random.randint(-1, 1),)
        else:
            return False

    #Function to have a player decide where to move
    #Returns a tuple (X,Y), where either can be + or -
    def moveDecision(self, world):
        foodInRange = []
        playersInRange = []

        #Loop through squares within range
        for x in range(max(0, self.X-self.speed), min(self.X+self.speed, world.xSize-1)):
            remainingRange = self.speed - abs(self.X - x)
            for y in range(max(0, self.Y-remainingRange), min(self.Y+remainingRange, world.ySize-1)):
                for item in world.world[x][y]:
                    if item == "food":
                        obj = {"x": x, "y": y, "distance": abs(self.X - x) + abs(self.Y - y)}
                        foodInRange.append(obj)
                    else:
                        obj = {"x": x, "y": y, "player": item, "distance": abs(self.X - x) + abs(self.Y - y)}

        if foodInRange:
            closest = foodInRange[0]

            for food in foodInRange:
                if food["distance"] < closest["distance"]:
                    closest = food

            return (closest["x"] - self.X, closest["y"] - self.Y)
        else:
            #random direction/distance
            x = random.randint(-self.speed, self.speed)
            y = random.randint(-self.speed + x, self.speed - x)

            return (x,y)

    def setLocation(self, x, y):
        self.X = x
        self.Y = y
