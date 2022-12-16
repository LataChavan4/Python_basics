from functools import reduce

sum = lambda a,b: a+b

l = [2,3,4,5,6]

value = reduce(sum,l)
print(value)