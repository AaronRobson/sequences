#!/usr/bin/python

from time import sleep
from itertools import cycle

badgers = ('badger',)*12
mushrooms = ('mushroom',)*2
snakes = ('snake a snake oh it\'s a snake',)

full = ((badgers + mushrooms) * 4) + badgers + snakes


def BadgerMushroomSnakeGenerator():
    '''Based on the Weebl looping animated video "Badgers":
    https://en.wikipedia.org/wiki/Badgers_(animation)
    '''
    return cycle(full)


def PrintBadger(timeBetween=0):
    for line in BadgerMushroomSnakeGenerator():
        print(line)
        sleep(timeBetween)


if __name__ == "__main__":
    PrintBadger(0.42)
