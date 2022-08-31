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
                #color green
            elif world[x][y] == ['food']:
                #color yellow
            elif len(world[x][y]) == 1:
                #color red
            #else color stays white
