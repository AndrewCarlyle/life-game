from easygraphics import *

class draw:
    def __init__(self):
        print("test")
    #def __init__(self, World):
    #    self.world = World

    def main(self):
        init_graph(1000, 1000)
        set_color(Color.RED)
        rect(20,20,39,39)
        self.drawWorld(self.world)
        pause()
        close_graph()

    def drawWorld(self, world):
        for x in range(len(world)):
            for y in range(len(world[x])):
                #Make this color darker based on how many items are there?
                if len(world[x][y]) > 1:
                    set_color(Color.GREEN)
                elif world[x][y] == ['food']:
                    set_color(Color.YELLOW)
                elif len(world[x][y]) == 1:
                    set_color(Color.RED)
                #else color stays white

    def refreshImage(self):
        easy_run(self.main)

d = draw()
d.refreshImage()
