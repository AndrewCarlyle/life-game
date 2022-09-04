from easygraphics import *

class Image:
    def __init__(self, world):
        self.world = world.world
        init_graph(800,800)

    def drawWorld(self):
        for x in range(len(self.world)):
            for y in range(len(self.world[x])):

                if all(z == "food" for z in self.world[x][y]) and len(self.world[x][y]) > 0:
                    set_color(Color.GREEN)
                #Make this color darker based on how many items are there?
                elif len(self.world[x][y]) > 0:
                    set_color(Color.RED)
                #elif len(self.world[x][y]) == 1:
                #    set_color(Color.DARK_YELLOW)
                else:
                    set_color(Color.WHITE)

                #May need to change from +10 to +9?
                rect(x*10,y*10,x*10+9,y*10+9)
