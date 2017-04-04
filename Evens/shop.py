item = [3.14,1.59,9.23,5.89,7.93]
name = ['Pi Pie', 'Chockas Chips', 'Chicken Chimichunga', 'Super Sundae', 'Massive Milkshake']
cont = True
order = []
orderTotal = 0.00
transNo = 0
while cont == True:
    poise=input('Would you like to add a product? please type "yes" or "no" ').lower()
    if poise=="yes":
        try:
            prod=int(input("enter product code: "))
            orderTotal=orderTotal+item[prod]
        except:
            print("please enter a legitimate product code.")
        print("Total: "+str(orderTotal))
    elif poise=="no":
        cont=False
print("Berners-Lee Burgers Deli")
print("Invoice Number: #"+str(transNo))
print("-------------------------------")
