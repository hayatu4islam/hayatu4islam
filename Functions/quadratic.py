import math
def quadratic(a, b, c):
    r1 = (-b + math.sqrt(b*b - 4*a*c))/2*a
    r2 = (-b - math.sqrt(b*b - 4*a*c))/2*a
    return r1, r2
print(quadratic(1, 5, 6))