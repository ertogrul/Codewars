def sum_and_multiply(sum, multiply):
    a = []
    is_found = False
    for i in range(sum):
        print(i)
        if (i * (sum - i) == multiply):
            is_found = True
            a.append(i)
            a.append(sum - i)
            print (a)
            #print('x = ' + str(x) + ', y = ' + str(y))
            break
    if(is_found == False):
        return None
    return a


sum_and_multiply(6, 9)
sum_and_multiply(12, 36)
# sum_and_multiply(, 9)
