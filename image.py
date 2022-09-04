from easygraphics import *

class Image:
    def __init__(self, world):
        self.world = world.world
        init_graph(800,800)

    def drawWorld(self):
        for x in range(len(self.world)):
            for y in range(len(self.world[x])):
                #Make this color darker based on how many items are there?
                if len(self.world[x][y]) > 1:
                    set_color(Color.RED)
                elif self.world[x][y] == ['food']:
                    set_color(Color.GREEN)
                elif len(self.world[x][y]) == 1:
                    set_color(Color.YELLOW)
                else:
                    set_color(Color.WHITE)

                #May need to change from +10 to +9?
                rect(x*10,y*10,x*10+9,y*10+9)
