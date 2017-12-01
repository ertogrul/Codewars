def high(sentence):
    # create scoring table
    scoring_list = ['zz', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', \
        'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', \
        'x', 'z']
    scoring_table = {}
    for value_score, key_letter in enumerate(scoring_list):
        #print("key_letter "+str(key_letter))
        scoring_table[key_letter] = value_score
        #print (scoring_table)
    # assign score to words
    highest_word_score = 0
    for word in sentence.split(" "):
        word_score = 0
        print(word)
        for letter in word:
            word_score += scoring_table[letter]
            #print (scoring_table[letter])
        if (word_score > highest_word_score):
            highest_word_score = word_score
            highest_word = word
            print ("highest word score: " + str(highest_word_score)+ word)
    return highest_word



#high('aaa bbbb cccc')
a = high('man i need a taxi up to ubud')    # 'taxi'
print (a)
