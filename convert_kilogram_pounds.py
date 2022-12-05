def kilometer_to_pounds (kilogram):
    return kilogram * 2.2


print("kilograms           pounds")
for i in range(1,200,2):
    print(str(i) + " " * 18 + str(round(kilometer_to_pounds(i), 3)))