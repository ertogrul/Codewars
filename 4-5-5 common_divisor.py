
def divisors(n):
    number_of_divisors = []
    for i in range(n, 0, -1):
        print(i)
        print (n)
        if n % i == 0:
            number_of_divisors.append(i)
            print (number_of_divisors)
    return len(number_of_divisors)



#divisors(4) # 3
#divisors(5) # 2
#divisors(12) # 6
print (divisors(30)) # 8
