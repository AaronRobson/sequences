from itertools import count

from exceed import until_exceeded


def hexagonal_number(n):
    n = int(n)
    return n*(2*n-1)


def hexagonal_numbers():
    return map(hexagonal_number, count(1))


def is_hexagonal_number(number):
    last = None

    for num in until_exceeded(number, hexagonal_numbers()):
        last = num

    return number == last


if __name__ == "__main__":
    from time import sleep

    print('Hexagonal Numbers (Ctrl-C to Exit):')

    for t_num in hexagonal_numbers():
        print(t_num)
        sleep(0.42)
