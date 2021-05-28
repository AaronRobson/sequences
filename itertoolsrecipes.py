#!/usr/bin/python

'''From:
https://docs.python.org/3.8/library/itertools.html#itertools-recipes

Using the names as used in Haskell code as these seem to be the cleanest.
'''
from operator import eq as equal
from itertools import islice, chain, count


def take(n, iterable):
    "Return first n items of the iterable as a list"
    return list(islice(iterable, n))


class DifferentLengthsError(IndexError):
    pass


def first_n(generator, n=None):
    '''Developed from: http://wiki.python.org/moin/Generators
    http://linuxgazette.net/100/pramode.html
    '''
    if n is not None:
        result = take(n, generator)
        if len(result) < n:
            raise DifferentLengthsError(
                'Requested amount exceeds the number in the iteration.')
        return result
    else:
        return generator


def skip_first_n(generator, n=None):
    return islice(generator, n, None)


def nth_term(generator, n=None):
    if (n is not None) and (n < 0):
        raise ValueError('Index must be above zero; %r is invalid.' % (n))

    for item in first_n(generator, n):
        value = item

    # "value" should have a value otherwise "FirstN" would have
    # raised a "DifferentLengthsError".
    return value


def nth_term_zero_based(generator, n=None):
    if n is not None:
        if n <= 0:
            raise ValueError(
                'Index must be zero or above; %r is invalid.' % (n))
        else:
            return nth_term(generator, n+1)
    else:
        assert n is None
        return nth_term(generator, n)


def zip_error_if_different_lengths(*collections):
    iterators = tuple(map(iter, collections))

    while True:
        ended = None
        output = []
        for iterator in iterators:
            try:
                output.append(next(iterator))
            except StopIteration:
                new_ended = True
            else:
                new_ended = False

            if (ended is not None) and (ended != new_ended):
                raise DifferentLengthsError(
                    'The iterations are of unequal lengths.')

            ended = new_ended

        if ended:
            break

        yield tuple(output)


def items_equal(*items):
    if items:
        first = items[0]
        others = items[1:]
        return all(equal(first, other) for other in others)
    else:
        return True


def collections_equal(*collections):
    if collections:
        try:
            return all(
                items_equal(*items)
                for items in zip_error_if_different_lengths(*collections))
        except DifferentLengthsError:
            return False
    else:
        return True


def len_of_generator(gen):
    '''Will use up the generator, use itertools.tee to make independently
    usable copies beforehand if required.

    Found at:
    http://stackoverflow.com/questions/393053/length-of-generator-output
    '''
    return sum(1 for _ in gen)


def len_of_generator_is_not_less_than(gen, minimum_len):
    '''The idea being to save resources by allowing generators to terminate earlier
    when the length is known to be enough for some purpose.
    '''
    min_len = 0
    if minimum_len < min_len:
        raise ValueError(
            'Length must be at least %r, %r rejected.' % (min_len, minimum_len))

    if minimum_len == min_len:
        return True

    for current_len, item in enumerate(gen, 1):
        if minimum_len <= current_len:
            return True
    else:
        return False


# testing an idea for showing the surrounding padding
def rolling_collection(items, sample_size, pad=0, pad_value=None):
    if sample_size < 1:
        raise ValueError('Sample Size must be at least 1.')

    if pad < 0:
        raise ValueError('Padding should be at least 0.')

    padding_items = (pad_value,) * pad
    items = chain(padding_items, items, padding_items)

    items = tuple(items)

    for i in range(len(items)-sample_size+1):
        yield items[i:i+sample_size]


def are_consecutive(items):
    items = iter(items)

    try:
        first_value = next(items)
    except StopIteration:
        return True
    else:
        return all(
            item == expected
            for item, expected in zip(
                chain([first_value], items),
                count(first_value)))
