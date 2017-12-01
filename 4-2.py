import platform
print (platform.python_version())

def last(s):
    mylist = s.split()
    print (mylist)
    #print (len(mylist))
    for passnum in range(len(mylist)-1, 0, -1):
        print(passnum)
        print(mylist[passnum])
        q = (mylist[passnum])
        print (q)
        print(q[len(q)-1])
        for i in range(passnum):
            aa = mylist[i]
            last_aa = aa[len(aa)-1]
            bb = mylist[i+1]
            last_bb = bb[len(bb)-1]
            if last_aa > last_bb:
                temp = mylist[i]
                mylist[i] = mylist[i+1]
                mylist[i+1] = temp
                print ("sort: " + str(mylist))

s = "man i need a taxi up to ubud"
last(s)

'''
Test.assert_equals(last("man i need a taxi up to ubud"), ["a", "need", "ubud", "i", "taxi", "man", "to", "up"])
Test.assert_equals(last("what time are we climbing up the volcano"), ["time", "are", "we", "the", "climbing", "volcano", "up", "what"])
Test.assert_equals(last("take me to semynak"), ["take", "me", "semynak", "to"])
Test.assert_equals(last("massage yes massage yes massage"), ["massage", "massage", "massage", "yes", "yes"])
Test.assert_equals(last("take bintang and a dance please"), ["a", "and", "take", "dance", "please", "bintang"])
'''
