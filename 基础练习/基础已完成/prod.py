from functools import reduce
def prod(L):
    def mult(x,y):
        return x*y
    return reduce(mult,L)
print(prod([3,5,7,9]))