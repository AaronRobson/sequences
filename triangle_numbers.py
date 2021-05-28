from itertools import accumulate, count

from exceed import until_exceeded


def triangle_number(n):
    '''Does floor division to convert from float to int.
    Otherwise answers are floats which are exactly the same as integers.
    '''
    n = int(n)
    return n*(n+1) // 2


def triangle_number_alt(n):
    return sum(range(1, n+1))


def triangle_numbers():
    # return map(triangle_number, count(1))
    return accumulate(count(1))


def is_triangle_number(number):
    last = None

    for num in until_exceeded(number, triangle_numbers()):
        last = num

    return number == last


if __name__ == "__main__":
    from time import sleep

    print('Triangle Numbers (Ctrl-C to Exit):')

    for t_num in triangle_numbers():
        print(t_num)
        sleep(0.42)
