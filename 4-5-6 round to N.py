def adjust(coin, price):
    #k = 0
    for i in range(coin):
        if price % coin == 0:
            break
        else:
            price += 1
    return price




'''
In other words: adjust takes two integers, coin and price,
and returns the smallest number k,
such that
price <= k
and k % coin == 0.

adjust( 3, 0 ) ==  0
adjust( 3, 1 ) ==  3
adjust( 3, -2) ==  0
adjust( 3, -4) == -3
adjust( 3, 3 ) ==  3
adjust( 3, 6 ) ==  6
adjust( 3, 7 ) ==  9
'''


#adjust( 3, 0) # 0
#adjust( 3, 1) # 3
#adjust( 3, -2) # 0
#adjust( 3, -4) #-3
#adjust( 3, 3 ) # 3
#adjust( 3, 6 ) # 6
adjust( 3, 7 ) # 9
