def max_rot(n):
    num = (list(str(n)))
    initial_num_length = len(num)
    print ("iiii", initial_num_length)
    first_digits = []
    print (num)

    while (len(first_digits) <= initial_num_length - 2):
        rotate(num)

        first_digits.append(num[0])
        del num[0]
        print ("first digits: ", first_digits)
        print (num)
        check_greatest(first_digits, num)



def rotate(num):
    temp = num[0]
    del num[0]
    num.append(temp)
    print (num)
    return num

def check_greatest(f, n):
    f = f + n
    a = map(str, f)
    print ("fff", a)
    a = int(''.join(f))
    print ("fff", a)
    """
    b = map(str, n)
    print ("nnnn", b)
    b = int(''.join(n))
    print ("nnnn", b)
    """
    if (a > greatest):
        print ("new greatest: ", a)


greatest = 0
print (max_rot(38458215))  # 85821534
# print (max_rot(195881031))  # 988103115
# print (max_rot(896219342))  # 962193428
# print (max_rot(69418307))  # 94183076
