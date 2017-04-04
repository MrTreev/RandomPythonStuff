import sys
import string
strText = input("Enter Text: ")
strCode = input("Enter Password: ")
lstText = list(strText)
lstCode = list(strCode)
n = 6
lstTextChanged = []

for i in range(len(lstText)):
	m = i%len(lstCode)
	strHexit = str(hex(ord(lstText[i])*ord(lstCode[m])))
	lstHexit = list(strHexit)
	lstHexit.remove('x')
	while len(lstHexit) < n:
		strHexit="0"+str(lstHexit)
		lstHexit=list(strHexit)
	lstTextChanged.append(str(lstHexit))

strPrint="".join(str(lstTextChanged))
for c in string.punctuation:
	strPrint= strPrint.replace(c,"")
	strPrint= strPrint.replace(" ","")
print("Message: "+strPrint)
