list = []
counter = 1
for num in range(10):
    print(counter, " from 10")
    number = int(input("enter number\n"))
    list.append(number)
    counter += 1

print("the max num in list is: ", max(list))
