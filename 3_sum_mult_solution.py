def sum_and_multiply(sum, multiply):
    for x in range(sum + 1):
            if x * (sum - x) == multiply:
                return [x, sum - x]

sum_and_multiply(6, 9)
sum_and_multiply(12, 36)
