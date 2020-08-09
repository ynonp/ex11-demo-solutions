import random


def rund_sum():
    while True:
        rund_num = random.randrange(1, 1000000)
        if rund_num % 7 == 0 and rund_num % 13 == 0 and rund_num % 15 == 0:
            return rund_num
           # break


rund_num_end = rund_sum()
print("rund num: ", rund_num_end)
