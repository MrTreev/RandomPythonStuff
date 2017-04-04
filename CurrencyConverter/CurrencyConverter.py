'''
Currency Converter python code
Written by Oliver Patterson
'''
from decimal import *
import xml.etree.ElementTree as ET
with open("ExchangeRates.xml") as file:
	data = file.read()
tree = ET.fromstring(data)
def start():
	print("Welcome to Treev's Currency Converter.")
	print("\n Australian Currency Conversion\n -------------------------------")
	for country in tree.findall('Currency'):
		Name = country.find('Name').text
		Rate = country.find('Rate').text
		print("  " + Name + ": " + str(Decimal(Rate)*AUD))
	print("\n -------------------------------")
	

while True:
	# Check for decimal
	try:
		AUD = Decimal(input('Enter amount in Australian Dollars: '))
	except:
		print("Not a Valid Input")
		break
	start()
	cont = input("\n Enter Q to quit or press enter to continue ...")
	if cont.upper() == 'Q':
		break