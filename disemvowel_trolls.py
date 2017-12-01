string = "Hello I eee am a troll, YEA TROLL"
vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']
def disemvowel(string):
    for a in string:
        for i in vowels:
            print a, i
            if (a == i):
                string = string.replace(a, "")
                print (string)
                break
    return string


disemvowel(string)
