import random


def rund_sum():
    while True:
        rund_num = random.randrange(1, 1000000)
        if rund_num % 7 == 0 and rund_num % 13 == 0 and rund_num % 15 == 0:
            return rund_num
           # break


rund_num_end = rund_sum()
print("rund num: ", rund_num_end)

# Very good. But maybe it's better to print rund_num each time it is
# calculated.
# Also, there is a typo in the word "rund" and variable names
# (should be random or rand).
# I would also recommend changing the name of the function rund_sum,
# because it doesn't calculate a sum.

# Also notice, it should be random.randrange(1, 1000001)
# (or you can use random.randint(1, 1000000)

