def max_rot(n):
    global greatest
    greatest = 0
    num = (list(str(n)))
    initial_num_length = len(num)
    print ("initial num length ", initial_num_length)
    first_digits = []
    check_greatest(first_digits, num)
    while (len(first_digits) <= initial_num_length - 1):
        rotate(num)
        first_digits.append(num[0])
        del num[0]
        check_greatest(first_digits, num)
    return greatest

def rotate(num):
    temp = num[0]
    del num[0]
    num.append(temp)
    return num

def check_greatest(f, n):
    global greatest
    f = f + n
    a = map(str, f)
    a = int(''.join(f))
    if (a > greatest):
        greatest = a

# print (max_rot(38458215))  # 85821534
# print (max_rot(195881031))  # 988103115
# print (max_rot(896219342))  # 962193428
# print (max_rot(69418307))  # 94183076
print (max_rot(507992495))  # 507992495 a wychodzi - 99249557



"""
84582153
85821534
85215348
85253481
85254813
85254138
85254183

85821534



######
507992495
79924955
99249557
92495579
92955794
92957945
92959457
92959574
92959547
92959547
"""
507992495
