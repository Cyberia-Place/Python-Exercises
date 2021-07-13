largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    try:
        num = int(num)
    except:
        if num == "done" :
            break
        else :
            print("Invalid input")
            continue

    if (largest and smallest) is None :
        largest = num
        smallest = num
    elif num > largest :
        largest = num
    elif num < smallest :
        smallest = num

print("Maximum is", largest)
print("Minimum is", smallest)


# Write a program that repeatedly prompts a user for integer numbers
# until the user enters 'done'. Once 'done' is entered, print out the
# largest and smallest of the numbers. If the user enters anything other
# than a valid number catch it with a try/except and put out an appropriate
# message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the
# output below.
