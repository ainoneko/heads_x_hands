#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
На входе функция получает параметр n - натуральное число.
Необходимо сгенерировать n-массивов, заполнить их случайными числами, каждый массив имеет случайный размер.
Размеры массивов не должны совпадать.
Далее необходимо отсортировать массивы.
Массивы с четным порядковым номером отсортировать по возрастанию, с нечетным порядковым номером - по убыванию.
На выходе функция должна вернуть массив с отсортированными массивами.
"""
from numbers import Number
from typing import List
import random

__all__ = ['array_of_sorted_random_arrays']


def random_number(n: int) -> Number:
    return random.randint(1, n)


def create_one_random_array(arr_len: int, rand_fun: type(random_number)) -> List[Number]:
    """ Create array of the specified length with random numbers

   >>> len(create_one_random_array(1, random_number))
   1

   >>> len(create_one_random_array(2, random_number))
   2
    """
    return [rand_fun(arr_len) for _ in range(arr_len)]


def create_random_arrays(n: int) -> List[List[Number]]:
    """Create n arrays with different lengths and random contents

        >>> len(create_random_arrays(1))
        1

        >>> len(create_random_arrays(2))
        2

        >>> len(create_random_arrays(3))
        3

        >>> x = create_random_arrays(3); lens = [len(a) for a in x]; len(lens) == len(set(lens))
        True

        >>> x = create_random_arrays(10); lens = [len(a) for a in x]; len(lens) == len(set(lens))
        True
    """
    sizes: list[int] = list(range(1, 2 * n + 1))
    random.shuffle(sizes)
    sizes = sizes[:n]
    return [create_one_random_array(size, random_number) for size in sizes]


def sort_arrays_in_array(a: List[List[Number]]) -> None:
    """ Sort arrays of the passed array (in-place)

        >>> a = [[1]]; sort_arrays_in_array(a); a
        [[1]]
        >>> a = [[3, 1, 2], [3, 1, 2, 4],  [4, 3, 2]]; sort_arrays_in_array(a); a
        [[1, 2, 3], [4, 3, 2, 1], [2, 3, 4]]

        >>> a = [[1], [3, 1, 2], [3, 1, 2, 4],  [4, 3, 2]]; sort_arrays_in_array(a); a
        [[1], [3, 2, 1], [1, 2, 3, 4], [4, 3, 2]]
    """
    for i, arr in enumerate(a):
        # Consider the first position to be even (index is 0)
        arr.sort(reverse=(i % 2 != 0))


def array_of_sorted_random_arrays(n: int) -> List[List[Number]]:
    """ Create array of random arrays and sort them
    :param n: number of arrays
    :return: array of sorted random arrays
    """
    result = create_random_arrays(n)
    sort_arrays_in_array(result)
    return result

if __name__ == '__main__':
    import doctest
    random.seed(1)
    doctest.testmod()
