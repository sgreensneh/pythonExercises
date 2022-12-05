count = 0
largest_number = 0
second_largest_number = 0
while count < 5:
    num = int(input("Give me a number: "))
    if num > largest_number:
        second_largest_number = largest_number
        largest_number = num

    if largest_number > num:
        second_largest_number = num

    count += 1


print("The largest number is: ", largest_number)
print("The Second largest number is:", second_largest_number)
