list = []


def read_lines(prompt):
    while True:
        row = (input(prompt))
        if not row.strip():
            break
        else:
            list.append(row)
            print(list)


read_lines("Please insert row: ")

list.reverse()
print(list)

# The input and reversing the list are good. But I think you should print each line separately,
# and not as a list. Something like:

for l in list:
    print(l)

# It's also better not to use the word "list" as a variable, since
# it has meaning in Python, and it's better to give the variable
# a different name.

