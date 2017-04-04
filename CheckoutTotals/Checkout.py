decTotal = float(0.00)
arrItems = []
def isfloat(strTest):
	try:
		float(strTest)
		return True
	except:
		return False

while True:
	strInput = input("Enter T to total bill or S to subtotal the cost so far: ")
	if strInput.upper() == "T":
		for i in range(0,len(arrItems)):
			decTotal = decTotal + arrItems[i]
		print(decTotal)
		break
	elif strInput.upper() == "S":
		for i in range(0,len(arrItems)):
			print(arrItems[i])
	elif strInput.upper() == "Q":
		
	elif isfloat(strInput) == True:
		arrItems.append(float(strInput))
	else:
		print("error")