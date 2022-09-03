from easygraphics import *

class Image:
    def __init__(self, world):
        self.world = world.world

    def main(self):
        init_graph(800, 800)
        set_color(Color.RED)
        self.drawWorld(self.world)
        pause()
        close_graph()

    def drawWorld(self, world):
        for x in range(len(world)):
            for y in range(len(world[x])):
                #Make this color darker based on how many items are there?
                if len(world[x][y]) > 1:
                    set_color(Color.RED)
                elif world[x][y] == ['food']:
                    set_color(Color.GREEN)
                elif len(world[x][y]) == 1:
                    set_color(Color.YELLOW)
                else:
                    set_color(Color.WHITE)

                #May need to change from +10 to +9?
                rect(x*10,y*10,x*10+10,y*10+10)

    def refreshImage(self):
        easy_run(self.main)
