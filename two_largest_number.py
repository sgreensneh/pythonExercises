count = 0
first_number = 0
second_number = 0

while count < 5:
    number = int(input("Enter a number"))
    if number > first_number:
        second_number = first_number
        first_number = number
    if second_number < number < first_number:
        second_number = number
    count += 1


print("the largest number is: ", first_number, "largest number is: ", second_number)

