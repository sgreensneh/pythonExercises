word = "Hello boss baby"
for i in range(len(word)):

    if word[i] == "b":
       print(word[i], ":", i)

for i in range(len(word)):
    if word[i] != "b":
         print(word[i], end="")

print("\n")

for index, value in enumerate(word):
    if value == "b":
        print(value, ":", index)


for index, value in enumerate(word):
    if value != "b":
        print(value, end="")
