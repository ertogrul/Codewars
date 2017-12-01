def start_smoking(bars,boxes):
    nr_cigs = (bars * 10 + boxes) * 18
    print (nr_cigs)
    handmade_cigs = 0
    while nr_cigs > 4:
        nr_cigs, rest = divmod(nr_cigs, 5)
        handmade_cigs += nr_cigs
        print ("handmade_cigs wieksze o :" + str(nr_cigs))
        print ("rest :" + str(rest))
        nr_cigs += rest
    return (bars * 10 + boxes) * 18 + handmade_cigs


print (start_smoking(10,2)) #2294
#print (start_smoking(0,1)) #22
#print (start_smoking(1,0)) #224
#print (start_smoking(1,1)) #247
