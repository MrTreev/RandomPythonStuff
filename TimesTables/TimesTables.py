while True:
	TableNumber = input("Enter Q to quit or a number for the times table: ")
	try:
		if int(TableNumber) in range(2,13):
			for a in range(0,12):
				print(str(TableNumber) + " * " + str(a+1) + " = " + str(int(TableNumber)*(a+1)))
	except:
		if TableNumber.upper() == "Q":
			break
		else:
			continue