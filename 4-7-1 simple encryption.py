def decrypt(encrypted_text, n):
    """
    if nr_elements odd = int(1/2) na lewej stronie (part2) i reszta na prawej (part1)
    if nr_elements even = n/2
    """
    encrypted_text = list(str(encrypted_text))
    print (len(encrypted_text))
    pass


def encrypt(text, n):
    if n <= 0:
        return text
    part1 = []
    part2 = []
    iterator = []
    text = list(str(text))
    for a in range(0, n, 1):
        if a > 0:
            text = iterator
            print ("text: ", text)
            part1 = []
            part2 = []
        print ("a: ", a)
        for x in range(0, len(text), 2):
            part1.append(text[x])
            print (text[x])
            print ("part1: ", part1)
        for y in range(1, len(text), 2):
            part2.append(text[y])
            print (text[y])
            print ("part2: ", part2)
        iterator = part2 + part1
    return ''.join(iterator)


# print (encrypt("This is a test!", 0))  # "This is a test!"
# print (encrypt("This is a test!", 1))  # "hsi  etTi sats!"
# print (encrypt("This is a test!", 2))  # "s eT ashi tist!"
# print (encrypt("This is a test!", 3))  # " Tah itse sits!"
# print (encrypt("This is a test!", 4))  # "This is a test!"
# print (encrypt("This is a test!", -1))  # "This is a test!"
# print (encrypt("This kata is very interesting!", 1))  # "hskt svr neetn!Ti aai eyitrsig"

# print (decrypt("This is a test!", 0))  # , "This is a test!")
print (decrypt("hsi  etTi sats!", 1))  # , "This is a test!")
# Test.assert_equals(decrypt("s eT ashi tist!", 2), "This is a test!")
# Test.assert_equals(decrypt(" Tah itse sits!", 3), "This is a test!")
# Test.assert_equals(decrypt("This is a test!", 4), "This is a test!")
# Test.assert_equals(decrypt("This is a test!", -1), "This is a test!")
# Test.assert_equals(decrypt("hskt svr neetn!Ti aai eyitrsig", 1), "This kata is very interesting!")

# Test.assert_equals(encrypt("", 0), "")
# Test.assert_equals(decrypt("", 0), "")
# Test.assert_equals(encrypt(None, 0), None)
# Test.assert_equals(decrypt(None, 0), None)
