import math
import re

def find_primes(start, end):
    k = start if start % 2 == 1 else start + 1
    primes = set(range(start, end)) - set(range(4, end, 2))

    while k < math.sqrt(end) + 1:
        i = 2 * k
        while i < end:
            if i in primes:
                primes.remove(i)
            i += k

        while True:
            k += 2
            if k in primes: break

        print(primes)
        return primes


def sort_list (list):
    return list.sort(reverse=True)

def calculate_expression( str) :
    res = sum(map(int, re.findall(r'[+-]?\d+', str)))
    return res


def test_sort_list():
    assert sort_list({1,2,3,5,40,12,5}) == {1 ,2,3,5,5,12,40}

def test_sort_list_notGood():
    assert sort_list({1,2,3,5,40,12,5}) == {1 ,40,3,5,5,12,40}

def test_sort_list_uncorrectly():
    assert sort_list({1,2,3,5,40,12,5}) == {5,2,3,1,5,12,40}

def calculate_expression():
    assert calculate_expression("45+2==") == 47

def calculate_expression_uncorrectly():
    assert calculate_expression("45+2==") == 42

def test_find_prims():
    assert find_primes(1,10) == {1,3,7}

def test_find_prims_uncorrectly():
    assert find_primes(1, 50) =={1,3,7,11,13,17}

def test_find_prims_notGood():
    assert find_primes(12,100) == {1}