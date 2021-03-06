# fast fibonacci
# F(n) = F(n-1)+F(n-2)
#0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55

def get_last_digit(index):
    a, b = 0, 1
    for x in range(index):
        a, b = b, (a+b) % 10
        print ("a ", a)
        print ("b ", b)
    return a

"""
def get_last_digit(i):
    x = str(fib(i))
    return x[-1:]

def fib(i):
    if i > 1:
        return fib(i - 1) + fib(i - 2)
    elif i == 1:
        return 1
    elif i == 0:
        return 0
"""


# print(get_last_digit(6))  # 8
# print(get_last_digit(10))  # 55)
# print (get_last_digit(79))  # 1)
# print (get_last_digit(20001))  # 6
# print (get_last_digit(193150))  # 5
print (get_last_digit(300))  # 0

# Test.assert_equals(get_last_digit(800), 5)
# Test.assert_equals(get_last_digit(1001), 1)
# Test.assert_equals(get_last_digit(100), 5)
# Test.assert_equals(get_last_digit(260), 5)
# Test.assert_equals(get_last_digit(1111), 9)
# Test.assert_equals(get_last_digit(1234), 7)
# Test.assert_equals(get_last_digit(99999), 6)

# Test.assert_equals(get_last_digit(234), 2)
# Test.assert_equals(get_last_digit(193241), 1)

# Test.assert_equals(get_last_digit(270), 0)
