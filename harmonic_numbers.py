from fractions import Fraction
from itertools import accumulate, count


# http://en.wikipedia.org/wiki/Harmonic_number


def reciprocal(number):
    return Fraction(1, number)


fraction_example = Fraction(2, 3)
assert reciprocal(reciprocal(fraction_example)) == fraction_example


def strictly_positive_integers():
    return count(1)


def strictly_positive_reciprocals():
    return map(reciprocal, strictly_positive_integers())


def accumulated_strictly_positive_reciprocals():
    return accumulate(strictly_positive_reciprocals())


harmonic_numbers = accumulated_strictly_positive_reciprocals

if __name__ == '__main__':
    from itertoolsrecipes import take

    number_to_show = 10
    print('Harmonic Numbers; the first {}.'.format(number_to_show))
    for n in take(number_to_show, accumulated_strictly_positive_reciprocals()):
        print(n)
