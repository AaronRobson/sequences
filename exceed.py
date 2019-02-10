from itertools import takewhile


def DoesNotExceed(limit):
    return lambda x: x <= limit


def UntilExceeded(maxNumber, generator):
    return takewhile(DoesNotExceed(maxNumber), generator)


def FilterExceeded(maxNumber, generator):
    return filter(DoesNotExceed(maxNumber), generator)
