count = 0
number = int(input("Enter a number"))
smallest_num = largest_num = number

while count < 5:
    if number < smallest_num:
        smallest_num = largest_num
        smallest_num = number

    if number > largest_num:
        largest_num = number

count += 1
print("smallest number is", smallest_num, "largest number is", largest_num)
