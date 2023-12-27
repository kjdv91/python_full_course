"""
rows = int(input("How many rows?: \n"))
columns = int(input("How many columns:\n"))
symbol = input("Enter a symbol to use:\n")



for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()


while   True:
    name = input("Enter your name:")
    if name != "":
        break

phone_number = "123-456-789"

for i in phone_number:
    if i =="-":
        continue
    #print(i)
    print(i, end="")"""

for i in range (1,20):
    if i == 10:
        pass
    else:
        print(i)