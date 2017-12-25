def toJadenCase(string):
    a = ""
    #string = string.title()
    #for x in range(len(string)):
    str1 = list(string)
    print (str1)
    print (str1[2])
    str1[2] = "Z"
    print (str1[2])


    for x in str1:
        print (str1[x])
        #print (x)

        if x == "'":
            str1[x] = "q"
            print (x)
        else:
            print (x)
        
        # print (string[x])
        #if string[x] == "'":
        #    string[x] = string[x].upper(
        #    print (string[x])
    ''.join(a)
    print (a)
    #return string


#upper()
#''.join(a)
quote = "How can mirrors be real if our eyes aren't real"
toJadenCase(quote)  # "How Can Mirrors Be Real If Our Eyes Aren't Real")
