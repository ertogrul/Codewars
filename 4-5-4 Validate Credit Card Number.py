def validate(card_number):
    card_number_list = [int(x) for x in str(card_number)]
    print (card_number_list)
    card_number_doubled = []

    if len(card_number_list) % 2 == 0:
        print ("#1")
        for x in range(0, len(card_number_list), 2):
            print(card_number_list[x])
            y = card_number_list[x] + card_number_list[x]
            if y > 9:
                print ("!!"+str(y))
                nr_string = str(y)
                sum_of_2_numbers = int(nr_string[0]) + int(nr_string[1])
                print("!!wynik: " + str(sum_of_2_numbers))

            card_number_list[x] = y
    else:
        print ("#2")
        for x in range(1, len(card_number_list), 2):
            print ("1")
            print(card_number_list[x])
            y = card_number_list[x] + card_number_list[x]
            card_number_list[x] = y
    print(card_number_list)
'''
if (len(str(card_number)) % 2 == 0):
card_number_doubled = [card_number_list[x] for x in range(0, len(card_number_list), 1) if x % 2 == 0]
else:
card_number_doubled = [card_number_list[x] for x in range(1, len(card_number_list), 2)]
print (card_number_doubled)
'''
#validate(7457975335687532)
validate(579864235797)
#validate(4971032)
