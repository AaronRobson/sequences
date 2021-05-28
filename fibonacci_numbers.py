from itertoolsrecipes import take
from decorators import memoised


def _fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def fibonacci_numbers(n=None):
    if n is not None:
        return take(n, _fibonacci())
    else:
        return _fibonacci()


@memoised
def fibonacci_number(num):
    '''Recursive definition from:
    http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-001-structure-and-interpretation-of-computer-programs-spring-2005/video-lectures/1b-procedures-and-processes-substitution-model/
    '''
    if num < 0:
        raise ValueError('Fibonacci numbers not defined for negative numbers.')

    if num < 2:
        return num
    else:
        return fibonacci_number(num-2) + fibonacci_number(num-1)


if __name__ == "__main__":
    print('Fibonacci Sequence:\n')

    print('First Few:')
    for num in fibonacci_numbers(13):
        print(num)

    print()

    from time import sleep

    print('Infinite (Ctrl-C to exit):')
    for num in fibonacci_numbers():
        print(num)
        sleep(.42)
