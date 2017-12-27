def toJadenCase(string):
    words = []
    work_list = list(string)
    for x in work_list:
        letter1 = list(x)
        print (letter1)
        letter1[0] = letter1[0].upper()
        words.append(''.join(letter1))
        print (words)
    return ' '.join(words)

#upper()
#''.join(a)
quote = "How can mirrors be real if our eyes aren't real"
toJadenCase(quote)  # "How Can Mirrors Be Real If Our Eyes Aren't Real")
