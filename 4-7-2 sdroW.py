def spin_words(s):
    answer = ""
    temp = s.split(" ")
    for x in temp:
        if (len(x) <= 4):
            answer = answer + x + " "
        else:
            x = "".join(list(reversed(x)))
            answer = answer + x + " "
    return answer.strip()



# print (spin_words("Welcome"))  # "emocleW")
# print (spin_words("Hey fellow warriors"))  # returns "Hey wollef sroirraw"
# print (spin_words("This is a test"))  # returns "This is a test"
print (spin_words("This is another test"))  # returns "This is rehtona test"
