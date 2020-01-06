# build-in map, filter, reduce

from operator import getitem, truth
from functools import reduce


def keep_truthful(iterable):
    return filter(truth, iterable)

def abs_sum(iterable):
    return sum(list(map(abs, iterable)))

def walk(dictionary, way):
    return reduce(getitem, way, dictionary)


print(list(keep_truthful([True, False, "", "foo"]))) # [True, 'foo]

print(abs_sum([-3, 7])) # 10
print(abs_sum([])) # 0
print(abs_sum([42])) # 42

print(walk({'a': {7: {'b': 42}}}, ["a", 7, "b"])) # 42
print(walk({'a': {7: {'b': 42}}}, ["a", 7])) # {'b': 42}