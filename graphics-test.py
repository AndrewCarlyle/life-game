from easygraphics import *

def main():
    init_graph(1000, 1000)
    set_color(Color.RED)
    rect(20,20,39,39)
    pause()
    close_graph()

easy_run(main)

def drawWorld(world):
    for x in range(len(world)):
        for y in range(len(world[x])):
            if len(world[x][y]) > 1:
                set_color(Color.GREEN)
            elif world[x][y] == ['food']:
                set_color(Color.YELLOW)
            elif len(world[x][y]) == 1:
                set_color(Color.RED)
            #else color stays white
