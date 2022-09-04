from easygraphics import *

class Image:
    def __init__(self, world):
        self.world = world.world
        init_graph(800,800)

    def drawWorld(self):
        for x in range(len(self.world)):
            for y in range(len(self.world[x])):

                if all(z == "food" for z in self.world[x][y]) and len(self.world[x][y]) > 0:
                    set_fill_color(Color.GREEN)
                #Make this color darker based on how many items are there?
                elif len(self.world[x][y]) > 0:
                    set_fill_color(Color.RED)
                else:
                    set_fill_color(Color.WHITE)

                #May need to change from +10 to +9?
                fill_rect(x*10,y*10,x*10+9,y*10+9)
