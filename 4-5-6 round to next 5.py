def round_to_next5(n):
    for i in range(n, n+5):
        print(n)
        if n % 5 == 0:
            print("!!!:"+str(n))
            break
        else:
            n += 1
    return n

round_to_next5()

'''
1 -> 5
5    5
7    10
20   20
39   40
0    ->   0
2    ->   5
3    ->   5
12   ->   15
21   ->   25
30   ->   30
'''
