# lambda function is used when we want to pass fuction as an argument

# def func(a):
#     return a+5



func = lambda a: a+5
square = lambda x: x*x
sum = lambda a,b,c: a+b+c



x = 12
print(func(x))
print(square(x))
print(sum(x,2,5))