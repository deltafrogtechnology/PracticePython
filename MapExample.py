from _functools import reduce
l = [1,2,3,4,5,6,7]


def dubler(a):
    return a*a

doubler = list(map(dubler,l ))

evens = list(filter(lambda a:a%2!=0,l))

sum = (reduce(lambda a,b:a+b, l))
print(evens)
print(sum)
print(doubler)