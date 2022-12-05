
# for i in range(1,101):
#     if i % 15 == 0:
#         print("fizzbuzz")
#     elif i % 3 == 0:
#         print("fizz")
#     elif i % 5 == 0:
#         print("buzz")
#     else:
#         print(i)

#   score = int(input("Enter a number or -1 to exit: "))
# while (score := int(input("Enter a number or -1 to exit: "))) != -1:
#     print(score)
    # score = int(input("Enter a number or -1 to exit: "))

# for i in range(1,11):
#     print("*" * i)

# string = "mississippi is the longest river"
# print(string[:11:-2])

# a = "spam"
# a = a[:2]+ "er" + a[3]
# print(a)

# name = "green"
# age = 18.6654
# s = "{0:^10} is {1:>5.2f} years old, and {0} loves {2}".format(name, age, "java")
# s = f"{name:^10} is {age:>5.2f} years old, and {name} loves {'java'}"
#
# hello = "hello world"
# for index, letter in enumerate(hello):
#  print(f"{letter} --> {index}")
#
# print()
# green = "top boy"
# for index in range(len(green)):
#       print(f"{green[index]} --> {index}")
#
# for i in range(1, 21, 2):
#     s = "*" * i
#     print(f"{s:<20}{s:^20}{s:>20}")
#
# weight = float(input("Enter your weight: "))
# unit = input("(K)g or (L)bs ")
# if unit.upper() == "K":
#     convert = weight / 0.45
#     print("weight in lbs: " +str(convert))
# else:
#     convert = weight * 0.45
#     print("weight in kgs: " +str(convert))

#print("Hello " + input("What is your name ? "))
# s = "Hello there!!!"
# print(s.find("e",3))

# for i in range(1,15,2):
#     s = "*" * i
#     print(s.center(120))

# blow = "10110001100101111078"
# #print(blow.replace("1", "x").replace("0","1").replace("x","0"))
# print(blow.translate(str.maketrans("01","10", "8")))

# s = "lover"
#
# print(s[2:] + s[:2])

# import string
# user_input = input("Enter the word to decode: ")
# key = int(input("What key would you like to use: "))
#
# lower_letters = string.ascii_lowercase
# upper_letters = string.ascii_uppercase
# decoded_lower_letters = lower_letters[key:] + lower_letters[:key]
# decoded_upper_letters = upper_letters[key:] + upper_letters[:key]
#
# letters = lower_letters + upper_letters + string.whitespace
# decoded_letters = decoded_lower_letters + decoded_upper_letters + string.whitespace
# encoded = user_input.translate(str.maketrans(letters, decoded_letters))
# decoded = encoded.translate(str.maketrans(decoded_letters, letters))
# print(encoded)
# print(decoded)

#
# def celcius_to_fahr(celcius_val):
#     """"
#      This function to convert celcius temp to fahrenheit temp
#      :param celcius_val: float
#      :return: float
#      >>> celcius_to_fahr(16)
#      60.8
#     """
#
#     return celcius_val * 1.8 + 32.0
# cel_val = 16
# print(celcius_to_fahr(cel_val))



#
# def my_name(name):
#
#     print("My name is %s" %name)
# my_name("Sgreen")

# user_input = input("Would you like to use the bank, yes or no: ")
# while user_input != "NO":
#     print("Bank account info")
#     user_input = input("Would you like to use the bank again, yes or no: ")
# print("Thank you for banking with us: ")

# userInput = int(input("Please enter a value: "))
# total = 0
# while userInput != 0:
#     total = total + userInput
#     userInput = int(input("Please enter another value: "))
# print("total value is: " +str(total))

count = 1
while count <= 100:
    print(count)
    count += 1

for count in range(1,101):
    print(count)






