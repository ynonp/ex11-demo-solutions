list = []
counter = 1
for num in range(10):
    print(counter, " from 10")
    number = int(input("enter number\n"))
    list.append(number)
    counter += 1

print("the max num in list is: ", max(list))

# Good job!
# A few comments:
# - This works for integers, but maybe you should allow non-integers values too.
# - You could have used (num + 1) as your counter.

