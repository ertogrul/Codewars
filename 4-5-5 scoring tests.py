#returns test score
def score_test(tests, right, omit, wrong):
    points = 0
    for x in tests:
        print (x)
        if x == 0:
            points += right
            print ("points: "+str(points))
        elif x == 1:
            points += omit
            print ("points: "+str(points))
        elif x == 2:
            points -= wrong
            print ("points: "+str(points))
    return points



print (score_test([0, 0, 0, 0, 2, 1, 0], 2, 0, 1))  # 9
#score_test([0, 1, 0, 0, 2, 1, 0, 2, 2, 1], 3, -1, 2)  # 3
