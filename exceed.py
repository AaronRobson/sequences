from itertools import takewhile


def does_not_exceed(limit):
    return lambda x: x <= limit


def until_exceeded(max_number, generator):
    return takewhile(does_not_exceed(max_number), generator)


def filter_exceeded(max_number, generator):
    return filter(does_not_exceed(max_number), generator)
