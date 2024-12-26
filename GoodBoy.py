import sys

command = input("Continue? [Y/n]: ")  # Fixed typo in variable name

while command == "Y":
    age = int(input("Type your age: "))  # Ensure input is converted to an integer
    text = "So you are born in the year: "
    calculation = 1403 - age
    print(text + str(calculation))
    command = input("Continue? [Y/n]: ")

if command == "n":
    print("GoodBye")
    sys.exit()
