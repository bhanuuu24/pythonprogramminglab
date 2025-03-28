import random
n=random.randint(1,100)
print(n)
a=4
while (a>=0):
    print("=====Enter the number to match the random number=====")
    guess=int(input("Enter the number:"))
    if(guess>n):
        print("Number entered is too high")
    elif(guess<n):
        print("Number entered is too low")
    else:
        print("Congratulations You are great !")
        print("Number Matched")
        break
    a=a-1