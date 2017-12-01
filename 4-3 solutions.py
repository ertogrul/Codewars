def last(s):
    l = s.split()
    l.sort(key = lambda x: x[-1])
    return l
Best Practices0Clever0
0ForkCompare with your solutionLink
navka666

def last(s):
  s = s.split()
  s = sorted(s, key=lambda item: item[-1].encode("utf-8"))
  return s
Best Practices0Clever0
0ForkCompare with your solutionLink
lymanchou

def last(s):
    return sorted([i for i in s.split()],key=lambda a:a[-1])
Best Practices0Clever0
0ForkCompare with your solutionLink
yossef76

def last(s):
    return sorted(s.split(), key=lambda i:i[-1])
Best Practices0Clever0
0ForkCompare with your solutionLink
Joachimek666

def last(s) :
  s = s.split()
  return sorted(s,key=lambda x:str(x[-1]))
Best Practices0Clever0
0ForkCompare with your solutionLink
AsherG

last=lambda s:list(sorted(s.split(),key=lambda x:x[-1]))
Best Practices0Clever0
0ForkCompare with your solutionLink
marijapanovic

def last(s):
    s = s.split()
    new_s = sorted(s,key =last_letter)
    return new_s

def last_letter(word):
    return word[-1]

Best Practices0Clever0
0ForkCompare with your solutionLink
emptyrider3

def last(s):
    import random
    words = s.split(' ')
    ordered = [word[-1] for word in words]
    dic = {}
    dontDo = []
    for word in words:
        if ordered.count(word[-1]) != 1:
            dic[words.index(word)] = word

    ordered.sort()
    final = []
    print(ordered)
    print(dic)
    for letter in ordered:
        if ordered.count(letter) != 1:
            for word in list(dic):
                if dic[word][-1] == letter:
                    final.append(dic[word])
                    del dic[word]
        else:
            for word in words:
                if word[-1] == letter:
                    final.append(word)
    for word in final:
        if final.count(word) != words.count(word):
            difference = words.count(word) - final.count(word)
            print(difference)
            index = final.index(word)
            print(index)
            for x in range(difference):
                final.insert(index,word)
    return final


Best Practices0Clever0
0ForkCompare with your solutionLink
danaitabay

def last(s):
    l = []
    word = sorted(s.split(), key=lambda x:x[-1] )
    l.append(word)
    for item in l:
        return (item)
Best Practices0Clever0
0ForkCompare with your solutionLink
Chris_Rands

def last(s):
    lst = s.split()
    lst.sort(key = lambda x: x[-1])
    return lst
Best Practices0Clever0
0ForkCompare with your solutionLink
arunkundgol

def MyFn(s):
    return s[-1]

def last(s):
    return sorted(s.split(" "), key=MyFn)
Best Practices0Clever0
0ForkCompare with your solutionLink
feizhang

def last(s):
    list = s.split()
    length = len(list)
    if length == 0 or length == 1:
        return list

    for i in range(1, length):
        key = list[i]
        j = i - 1
        while j >= 0:
            if key[-1] < list[j][-1]:
                list[j+1] = list[j]
                list[j] = key
            j -= 1

    return list





    #your code here
Best Practices0Clever0
0ForkCompare with your solutionLink
azazeal700

def last(s):
    WordsList = s.split(' ')
    WordsList.sort(key=lambda r: r[-1:])
    return WordsList
Best Practices0Clever0
0ForkCompare with your solutionLink
Kurshin

from operator import itemgetter

def last(s):
    words = s.split(' ')
    return sorted(words, key=itemgetter(-1))

Best Practices0Clever0
0ForkCompare with your solutionLink
evanmarcey

def last(s):
    return sorted(s.split(' '),key=lambda x: x[len(x)-1:])

Best Practices0Clever0
0ForkCompare with your solutionLink
Graham G

def last(s):
    '''This function, given a string of words (x), return an array of the words,
    sorted alphabetically by the final character in each.

    If two words have the same last letter, the returned array shows them in the
    order they appeared in the given string.

    All inputs will be valid.
    '''

    analysis = {}
    words = s.split()
    last = []
    result = []

    for element in words: # Analyse the original string, prepare a sorted list of letters
        if element[-1] not in analysis:
            analysis[element[-1]]=[element]
            last.append(element[-1])
        else:
            temp = analysis.get(element[-1])
            temp.append(element)
            analysis[element[-1]]=temp
    last.sort()

    for element in last: # build the result based on the order in the original string using the results of the analysis
        if element in analysis:
            count = 0
            temp = analysis.get(element)
            while count < len(analysis.get(element)):
                result.append(temp[count])
                count += 1
    return(result)
