from itertools import takewhile, chain


def DoesNotExceed(limit):
    return lambda x: x <= limit


def UntilExceeded(maxNumber, generator):
    return takewhile(DoesNotExceed(maxNumber), generator)


def FilterExceeded(maxNumber, generator):
    return filter(DoesNotExceed(maxNumber), generator)


def Test():
    smallNum, bigNum = sorted((8, 10))
    values = tuple(chain(range(bigNum), range(bigNum)))
    oneExpected = tuple(range(smallNum+1))
    twoExpected = tuple(chain(oneExpected, oneExpected))

    assert(tuple(UntilExceeded(smallNum, values)) == oneExpected)
    assert(tuple(FilterExceeded(smallNum, values)) == twoExpected)

    assert(tuple(UntilExceeded(5, [1, 5, 3, 7])) == (1, 5, 3))


if __name__ == "__main__":
    print('Exceed:')
    Test()

    input('\nPress Enter to Close:')
