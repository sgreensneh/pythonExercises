def mile_to_kilometers (miles):
    return miles * 1.609


print("miles           kilometers")
for i in range(1,11,1):
    print(str(i) + " " * 18 + str(round(mile_to_kilometers(i), 3)))