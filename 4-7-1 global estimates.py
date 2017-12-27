def global_estimate(estimates):
    return#a tuple of two values : (minimum, maximum)






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
