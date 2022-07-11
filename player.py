from random import randint

class player:
    #define player attributes
    def __init__(self,
                 sex, #char ('M' or 'F')
                 strength, #int
                 attractiveness, #int
                 iq, #int
                 fertility, #int
                 friendliness #int - how likely the player is to be friendly (mate, share) vs start conflict with another player
                 ):
        self.sex = sex
        self.strength = strength
        self.attractiveness = attractiveness
        self.iq = iq
        self.fertility = fertility

        self.hunger = 0
        self.age = 0

    def getOlder(self):
        self.age = self.age + 1

    def reproduce(self, player):
        if self.sex != 'F' or player.sex != 'M':
            return False

        num = randint(1, 10)

        if self.fertility * player.fertility > num:
            return True
        else:
            return False
