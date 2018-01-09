def gen_nums():
    n = 0
    while n < 4:
        yield n
        n += 1

# print(gen_nums())
nums = gen_nums()
print (type(nums))

for i in nums:
    print (i)

print ()

more_nums = gen_nums()
print (next(more_nums))
print (next(more_nums))
print (next(more_nums))
print (next(more_nums))
