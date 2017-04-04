import math
def average():
	a = 0
	i = 0
	Answer = 0
	Array = []
	try:
		# Get amount of numbers
		Amount = int(input("How many Numbers do you Want to average?\n"))
		# Repeat that many times
		while a < Amount:
			Array.append(int(input("Number:")))
			a = a+1
		# Add the numbers together
		while i < len(Array):
			Answer = Answer + int(Array[i])
			i = i+1
		# Divide them by the amount of numbers
		Answer = Answer/Amount
		# print
		print(Answer)
	except:
		print("Haha, No.")
while True:
	if input("Enter Q to quit or anything else to continue.") == "Q":
		break
	else: 
		average()
