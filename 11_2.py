def number_month(prompt):
    while True:
        try:
            return int(input(prompt)) * 12

        except ValueError:
            print("Sorry - you typed something that wasn't a number. Try again")


age = number_month("Please insert your age in years: ")

print(f"your age in months is: {age}")

# Good job. This program works. But I think it's better to keep the input age in years
# in a separate variable - you might want to use it in the future.
# I think it's better to create a function that returns the age in years
# and then calculate the age in months by multiplying it by 12.

# You can also consider asking the age in years & months format,
# and only then converting it to years. For example, if the person's
# age is 36 years and 2 months, then the age in months is 434 months.

# Notice that the input might be negative (such as -2) - you should
# Display an error message in this case too.

# You might also consider limiting the age from above - for example an
# age of 2000 years doesn't make sense.

