"""
print the evens

i=0
while i<101:
    print (i)
    i=i+2


#print 1-100 say if even or odd

i = 0
while i<101:
    print (i)
    if i % 2 == 0:
        print ("this is even")
    else:
        print ("this is odd")
    i = i + 1


#get 5 numbers, sum them up, print the result

a = int (input("Enter a number: "))
b = int (input("Enter a number: "))
c = int (input("Enter a number: "))
d = int (input("Enter a number: "))
e = int (input("Enter a number: "))
intTotal = a+b+c+d+e
print (intTotal)


total = 0
done = 0
i = int(input("How many numbers? "))
while i > done:
    a = int(input("Number "))
    total = a + total
    done = done + 1
print(total)
"""

item = [3.14,1.59,9.23,5.89,7.93]
pie = 0
chips = 1
chicken = 2
burger = 3
kabab = 4
