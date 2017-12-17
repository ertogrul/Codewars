def number_property(n):
    results = []
    #checking if n is a prime number
    if (n <= 1):
        results.append(False)
    else:
        is_prime = 1
        for x in range(2, n):
            if (n % x == 0):
                print ("x: ", x)
                results.append(False)
                is_prime = 0
                break
        if is_prime:
            results.append(True)
    # checking if n is even
    if (n % 2 == 0):
        results.append(True)
    else:
        results.append(False)
    # checking if n is result of * 10
    if (n % 10 == 0):
        results.append(True)
    else:
        results.append(False)
    return results

print (number_property(31))
print (number_property(-10))  # [False,True,True]
print (number_property(2))    # [True,True,False]
print (number_property(120))  # [False,True,True]
print (number_property(125))  # [False,False,False]


"""
def number_property(n):
    results = []
    if check_if_prime(n):
        results.append(True)
    else:
        results.append(False)
    if (n % 2 == 0):
        results.append(True)
    else:
        results.append(False)
    if (n % 10 == 0):
        results.append(True)
    else:
        results.append(False)
    return results




def check_if_prime(m):
    if (m <= 0 or m == 1):
        print (m, " is not prime number.")
        return False
    is_prime = 1
    for x in range(2, m):
        if (m % x == 0):
            print (m, " is not a prime numberQQ.")
            is_prime = 0
            return False
            break
    if is_prime:
        print (m, "is a prime number!")
        return True


# print (number_property(31))
# print (number_property(-10))  # [False,True,True]
# print (number_property(2))    # [True,True,False]
# print (number_property(120))  # [False,True,True]
# print (number_property(125))  # [False,False,False]
"""
