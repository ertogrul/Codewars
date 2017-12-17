def validate(card_number):
    """Validate credit card number."""
    card_number_list = [int(x) for x in str(card_number)]
    print (card_number_list)
    y = 0
    if len(card_number_list) % 2 == 0:
        print ("#1")
        for x in range(0, len(card_number_list), 2):
            print(card_number_list[x])
            y = card_number_list[x] + card_number_list[x]
            if y > 9:
                print ("!!"+str(y))
                nr_string = str(y)
                y = int(nr_string[0]) + int(nr_string[1])
                print("!!wynik: " + str(y))
                # sum_of_2_numbers = int(nr_string[0]) + int(nr_string[1])
                # print("!!wynik: " + str(sum_of_2_numbers))
            card_number_list[x] = y
    else:
        print ("#2")
        for x in range(1, len(card_number_list), 2):
            print(card_number_list[x])
            y = card_number_list[x] + card_number_list[x]
            print ("!!"+str(y))
            if y > 9:
                nr_string = str(y)
                y = int(nr_string[0]) + int(nr_string[1])
                print("!!wynik: " + str(y))
                #sum_of_2_digit_number = int(nr_string[0]) + int(nr_string[1])
                #print("!!wynik: " + str(sum_of_2_digit_number))

            card_number_list[x] = y
    print(card_number_list)
    card_sum = 0
    for z in range(0, len(card_number_list)):
        card_sum += card_number_list[z]
        print (card_sum)
    if (card_sum % 10 == 0):
        return True
    else:
        return False


'''
if (len(str(card_number)) % 2 == 0):
card_number_doubled = [card_number_list[x] for x in range(0, len(card_number_list), 1) if x % 2 == 0]
else:
card_number_doubled = [card_number_list[x] for x in range(1, len(card_number_list), 2)]
print (card_number_doubled)
'''
# print (validate(91))
# print (validate(79927398713))  # True
# print(validate(2543))  # True



print (validate(79927398710))  # False)
'''
# Test.assert_equals(validate(79927398711), False)
# Test.assert_equals(validate(79927398712), False)
# Test.assert_equals(validate(79927398714), False)
# Test.assert_equals(validate(2741), True), False)
'''
