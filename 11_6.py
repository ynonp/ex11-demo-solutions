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
