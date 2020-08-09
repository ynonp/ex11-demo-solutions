import random


def rund_sum():
    rund_num1 = random.randrange(1, 11)
    rund_num2 = random.randrange(1, 11)
    print("rund_num1: ", rund_num1, "rund_num2: ", rund_num2)
    double = 2
    while True:
        small = rund_num1 * double
        if small % rund_num2 == 0:
            print('the small double is: ', small)
            break
        else:
            double += 1


rund_sum()

# Good job. But please notice: rund_num1 and rund_num2 may be identical,
# do you should start with double = 1.
# There is also a typo in the word "rund" and variable names
# (should be random or rand).
# I would also recommend changing the name of the function rund_sum,
# because it doesn't calculate a sum.
