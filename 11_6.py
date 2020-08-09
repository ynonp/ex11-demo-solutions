import random


def rund_sum():
    rund_num = random.randrange(1, 101)
    #print("rund_num is: ", rund_num)
    while True:
        guess = int(input("Which number did I choose (1 - 100)?"))
        if guess > 100 or guess < 0:
            print("Please select a number between 1 and 100!")
        else:
            if guess < rund_num:
                print("Put the number up")
            elif guess > rund_num:
                print("Put the number down")
            elif guess == rund_num:
                print("Correct!!!")
                break


rund_sum()

# Very good. Just notice, it should be
# `if guess > 100 or guess < 1:` and not
# `if guess > 100 or guess < 0:`.
# There is also a typo in the word "rund" and variable names
# (should be random or rand).
# I would also recommend changing the name of the function rund_sum,
# because it doesn't calculate a sum.

