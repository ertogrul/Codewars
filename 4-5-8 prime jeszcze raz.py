import math
def number_property(n):
    return [is_prime(n), is_even(n), is_multiple_10(n)]

def is_prime(n):
    if n % 2 == 0 and n > 2 or n < 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

def is_even(n):
    if (n % 2 == 0):
        return True
    else:
        return False
def is_multiple_10(n):
    if (n % 10 == 0):
        return True
    else:
        return False

# print (number_property(31))
print (number_property(-10))  # [False,True,True]
# print (number_property(2))    # [True,True,False]
# print (number_property(120))  # [False,True,True]
# print (number_property(125))  # [False,False,False]
