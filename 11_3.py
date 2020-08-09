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
