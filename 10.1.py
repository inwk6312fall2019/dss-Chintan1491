#Prog 10.1
from functools import reduce

lst = [10,11,12,13,14,15,16,17,18,19,20]
def add(x,y):
    return x+y
print(reduce(add, lst))

List = [10,11,12,13,14,15,16,17,18,19,20,[21,22,23,24,[25,26,27]]]
def nested_sum(x,y):
    return x+y
print(reduce(add, List[-1][-1]))
