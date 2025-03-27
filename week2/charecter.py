char = input("Enter the input you want to check:")[0]
if char.isupper():
    print(char,"Is Upper")
elif char.islower():
    print(char,"Is Lower")
elif char.isdigit():
    print(char,"Is a digit")
else:
    print(char,"Is a Special Character")