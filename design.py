number = int(input("Enter a number"))
factor = 1
sum_of_number = 0
while factor < number:
    if number % factor == 0:
        sum_of_number = sum_of_number + factor
    factor = factor + 1
    if sum_of_number < number:
        print(number, "is deficient")
    elif sum_of_number > number:
        print(number, "is abundant")
    else:
        print(number, "is a perfect number")




