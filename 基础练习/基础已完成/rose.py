import math
def quadratic(a, b, c):
    x1 = (-b+math.sqrt(pow(b,2)-4*a*c))/(2*a)
    x2 = (-b-math.sqrt(pow(b,2)-4*a*c))/(2*a)
    return x1,x2

r = quadratic(1,3,-4)
print(r)