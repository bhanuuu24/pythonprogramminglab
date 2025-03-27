import random
n = random.randint(1,100)
while True:
 x=int(input("Guess any number:"))
 if(x<n):
  print("The Number is too low.")
 elif(x>n):
  print("The Number is too high.")
 else:
  print("your Number has matched.")
