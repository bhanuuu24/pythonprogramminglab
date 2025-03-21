#code is for compound intrest.
print("enter the principal amount:")
p=int(input())
print("enter the rate of intrest")
r=float(input())
print("enter the number of years")
t=int(input())
compound_interest = p*(1 + r/100) ** t - p
print("the compound intrest is ")
print(compound_interest)
      

