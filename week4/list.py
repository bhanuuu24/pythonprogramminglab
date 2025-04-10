l1 = []
l2 = []
l3 = []

n1 = int(input("Enter the size of elements for list 1: "))
n2 = int(input("Enter the size of elements for list 2: "))
n3 = int(input("Enter the size of elements for list 3: "))

def createlist(l, n):
    for i in range(n):
        temp = int(input("Enter an element: "))
        l.append(temp)
    return l

l1 = createlist(l1, n1)
l2 = createlist(l2, n2)
l3 = createlist(l3, n3)

print("Elements in the first list:", l1)
print("Elements in the second list:", l2)
print("Elements in the third list:", l3)

def evensum(l):
    es = 0
    for i in range(0, len(l), 2): 
        es += l[i]
    return es

def oddsum(l):
    os = 0
    for i in range(1, len(l), 2): 
        os += l[i]
    return os

sum_l1 = evensum(l1)
sum_l2 = evensum(l2)
sum_l3 = evensum(l3)

sum_l1_odd = oddsum(l1)
sum_l2_odd = oddsum(l2)
sum_l3_odd = oddsum(l3)

sum_of_even_indexes = sum_l1 + sum_l2 + sum_l3
print("sum of even indexes",sum_of_even_indexes)

sum_of_odd_indexes = sum_l1_odd + sum_l2_odd + sum_l3_odd
print("sum of odd indexes",sum_of_odd_indexes)
