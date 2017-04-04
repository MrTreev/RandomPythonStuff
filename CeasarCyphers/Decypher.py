import sys
import string
strText = input("Enter Message: ")
strCode = input("Enter Password: ")
lstText = []
lstCode = list(strCode)
n = 6
strPrint = ""
lstText = [strText[i:i+n] for i in range(0, len(strText), n)]
for i in range(len(lstText)):
	lstText[i] = int(lstText[i], 16)
	lstText[i] = chr(int(int(lstText[i])/int(ord(lstCode[i%len(lstCode)]))))
	strPrint = strPrint+str(lstText[i])
print(strPrint)
