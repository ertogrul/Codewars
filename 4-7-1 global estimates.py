def global_estimate(e):
    best = 0
    worst = 0
    average = 0

    for x in e:
        best += x[0]
        worst += x[1]
    average = (best+worst)/2
    return (best, average, worst)
    """
    x, y = map(sum, zip(*e))
    return (x, (x+y)/2, y)
    """
# e = ((1, 2), (3, 4))
# print (global_estimate(e))  # (4, 5, 6)

# e = ((0, 1), (0, 10))
# print (global_estimate(e))  # ( (0, 5.5, 11))

# e = ((0, 0), (0, 0))
# print (global_estimate(e))  # (0, 0, 0)

# e = ((1, 1), )
# print (global_estimate(e))  # (1, 1, 1)

e = ((1, 3), (1, 4), (1, 5))
print (global_estimate(e))  # (3, 7.5, 12)


"""
test.describe('Basic tests')
testValues = (
(((1, 2), (3, 4)), (4, 5, 6)),
(((0, 1), (0, 10)), (0, 5.5, 11)),
(((0, 0), (0, 0)), (0, 0, 0)),
(((1, 1), ), (1, 1, 1)),
(((1, 3), (1, 4), (1, 5)), (3, 7.5, 12))
)

for estimates, answer in testValues:
    test.assert_equals(global_estimate(estimates), answer)
"""
