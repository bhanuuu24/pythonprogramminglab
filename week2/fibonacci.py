n = int(input("No. of fibonacci patterns:"))
a = 0
b = 1
print(a,end = " ")
print(b,end = " ")

while (n > 0):
    c = a+b
    print(c,end = " ")
    a = b
    b= c
    n = n - 1