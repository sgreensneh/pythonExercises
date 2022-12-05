number = int(input("Enter a number: "))
largest_number = smallest_number = number
while number != 0:
    if number > largest_number:
        largest_number = number
    if number < smallest_number:
        smallest_number = number
    number = int(input("Enter a number(punch 0 to quit)"))

print()

print("The largest number is: ", largest_number, "and smallest number is:", smallest_number)

