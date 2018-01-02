def triple_double(num1, num2):
    a = list(str(num1))
    b = list(str(num2))
    if search_num1(a, b) is True:
        return True
    else:
        return False


def search_num1(a, b):
    repeated = 0
    previous_digit = -1
    for x in a:
        if previous_digit == x:
            repeated += 1
        else:
            repeated = 0
        previous_digit = x
        if repeated == 2:
            if search_num2(b) is True:
                return True
            else:
                return False
            break
    if repeated < 2:
        return False


def search_num2(b):
    previous_digit = -1
    for y in b:
        if previous_digit == y:
            return True
        previous_digit = y
    return False






# print (triple_double(451999277, 41177722899))  # 1
# print (triple_double(1222345, 12345))  # 0
# print (triple_double(12345, 12345))  # 0
# print (triple_double(666789, 12345667))  # 1
print (triple_double(10560002, 100))  # 1
