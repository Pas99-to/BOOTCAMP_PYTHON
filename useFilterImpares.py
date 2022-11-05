from functools import reduce

def numeros(*args):
    return args

impares = reduce( lambda a,b: a+b,filter(lambda x: x % 2 != 0,numeros(2,6,7,8,9,11)))

print(impares) 