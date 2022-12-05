
unspecified_number = int(input("Enter a positive or negative value ('input 0 to exist')"))
total = 0
average = float(0)
while unspecified_number != 0:
    total = total + unspecified_number
    average = total / unspecified_number

    unspecified_number = int(input("Enter another positive or negative value ('input 0 to exist')"))
    if unspecified_number > 0:
        print(unspecified_number, "is a positve number")
    if unspecified_number < 0:
        print(unspecified_number, "is a negative number")
print("The total value: " +str(total))
print("The averga is: " +str(average))