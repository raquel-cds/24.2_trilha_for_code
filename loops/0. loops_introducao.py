import math

n = 2.718
somatorio = 0

while n < 1000:
    somatorio += 1/2**math.log(n, math.e)
    print(somatorio)
    n += 1