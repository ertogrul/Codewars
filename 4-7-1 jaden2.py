def toJadenCase(string):
    return " ".join(w.capitalize() for w in string.split())


quote = "How can mirrors be real if our eyes aren't real"
print (toJadenCase(quote))  # "How Can Mirrors Be Real If Our Eyes Aren't Real")



"""
def toJadenCase(string):
    words = []
    letter = string.split()
    for x in letter:
        letter = list(x)
        letter[0] = letter[0].upper()
        words.append(''.join(il))
    return ' '.join(words)
"""
