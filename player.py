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
        self.age = 0
        self.X = 0
        self.Y = 0

    def getOlder(self):
        self.age = self.age + 1

    def reproduce(self, player):
        if self.sex != 'F' or player.sex != 'M':
            return False

        num = random.randint(1, 10)

        if self.fertility * player.fertility > num:
            return True
        else:
            return False
