#4,5,7,11,19
#número 1 --> 4 (2**0)+3
#número 2 --> 5 (2**1)+3
#número 3 --> 7 (2**2)+3
#número 4 --> 11 (2**3)+3
#número 5 --> 19 (2**4)+3

def sucesion(n):
    return (2**(n-1)) + 3
print (sucesion (1))

