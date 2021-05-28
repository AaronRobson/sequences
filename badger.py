#!/usr/bin/python

from time import sleep
from itertools import cycle

badgers = ('badger',)*12
mushrooms = ('mushroom',)*2
snakes = ('snake a snake oh it\'s a snake',)

full = ((badgers + mushrooms) * 4) + badgers + snakes


def badger_mushroom_snake_generator():
    '''Based on the Weebl looping animated video "Badgers":
    https://en.wikipedia.org/wiki/Badgers_(animation)
    '''
    return cycle(full)


def print_badger(time_between=0):
    for line in badger_mushroom_snake_generator():
        print(line)
        sleep(time_between)


if __name__ == "__main__":
    print_badger(0.42)
