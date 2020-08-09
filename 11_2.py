def number_month(prompt):
    while True:
        try:
            return int(input(prompt)) * 12

        except ValueError:
            print("Sorry - you typed something that wasn't a number. Try again")


age = number_month("Please insert your age in years: ")

print(f"your age in months is: {age}")
