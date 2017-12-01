def start_smoking(bars,boxes):
    nr_cigarettes = bars * 180 + boxes * 18
    cigars_refubrished = round(nr_cigarettes/5)
    print (cigars_refubrished)
    while cigars_refubrished > 4:
        nr_cigarettes += cigars_refubrished
        print ("nr_cig: "+ str(nr_cigarettes))
        cigars_refubrished = cigars_refubrished/5
        print ("nr_ref: "+ str(cigars_refubrished))
    return round(nr_cigarettes)


print (start_smoking(10,2)) #2294
#print (start_smoking(0,1)) #22
#print (start_smoking(1,0)) #224
#print (start_smoking(1,1)) #247
