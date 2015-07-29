numero = input('Cual numero quieres convertir a letra: ')
entero = 0
decenas = 0
cien = 0
miles = 0
contador = 1
concatenar1 = ""
concatenar2 = ""
concatenar3 = ""
concatenar4 = ""
if(len(numero) == 1):
	for numeros in numero:
		if(contador==1):
			entero = int(numeros)	
elif(len(numero) == 2):
	for numeros in numero:
		if(contador==1):
			decenas = int(numeros)
		elif(contador==2):
			entero = int(numeros)	
		contador+=1
elif(len(numero)==3):
	for numeros in numero:
		if(contador==1):
			cien = int(numeros)
		elif(contador==2):
			decenas = int(numeros)
		elif(contador==3):
			entero = int(numeros)	
		contador+=1
else:
	for numeros in numero:
		if(contador==1):
			miles = int(numeros)
		elif(contador==2):
			cien = int(numeros)
		elif(contador==3):
			decenas = int(numeros)
		elif(contador==4):
			entero =int(numeros)
		contador+=1
if(entero+decenas+cien+miles == 0):
	print ("cero")
else:
	if(entero == 1 and decenas == 1):
		concatenar2 = "once"
	elif(entero == 2 and decenas == 1):
		print("doce")
	elif(entero == 3 and decenas == 1):
		print("trece")
	elif(entero == 4 and decenas == 1):
		print("catorce")
	elif(entero == 5 and decenas == 1):
		print("quince")
	else:
		if(entero==1):
			concatenar1 = "uno"
		elif(entero==2):
			concatenar1 = "dos"
		elif(entero==3):
			concatenar1 = "tres"
		elif(entero==4):
			concatenar1 = "cuatro"
		elif(entero==5):
			concatenar1 = "cinco"
		elif(entero==6):
			concatenar1 = "seis"
		elif(entero==7):
			concatenar1 = "siete"
		elif(entero==8):
			concatenar1 = "ocho"
		elif(entero==9):
			concatenar1 = "nueve"
		if(entero == 0 and decenas == 0 and cien == 1):
			concatenar3 = "cien"
		else:
			if(decenas==1):
				if(entero==0 and decenas==1):
					concatenar2 = "diez"
				else:
					concatenar2 = "diez y"
			elif(decenas==2):
				if(entero==0 and decenas==2):
					concatenar2 = "veinte"
				else:
					concatenar2 = "veinti"
			elif(decenas==3):
				if(entero==0 and decenas==3):
					concatenar2 = "treinta"
				else:
					concatenar2 = "treinta y"
			elif(decenas==4):
				if(entero==0 and decenas==4):
					concatenar2 = "cuarenta"
				else:
					concatenar2 = "cuarenta y"
			elif(decenas==5):
				if(entero==0 and decenas==5):
					concatenar2 = "cincuenta"
				else:
					concatenar2 = "cincuenta y"
			elif(decenas==6):
				if(entero==0 and decenas==6):
					concatenar2 = "sesenta"
				else:
					concatenar2 = "sesenta y"
			elif(decenas==7):
				if(entero==0 and decenas==7):
					concatenar2 = "setenta"
				else:
					concatenar2 = "setenta y"
			elif(decenas==8):
				if(entero==0 and decenas==8):
					concatenar2 = "ochenta"
				else:
					concatenar2 = "ochenta y"
			elif(decenas==9):
				if(entero==0 and decenas==9):
					concatenar2 = "noventa"
				else:
					concatenar2 = "noventa y"

	if(cien==1):
		if(decenas == 0 and entero == 0):
			concatenar3 = "cien"
		elif(decenas>0 or entero>0):
			concatenar3 = "ciento"
	elif(cien==2):
		concatenar3 = "doscientos"
	elif(cien==3):
		concatenar3 = "trescientos"
	elif(cien==4):
		concatenar3 = "cuatrocientos"
	elif(cien==5):
		concatenar3 = "quinientos"
	elif(cien==6):
		concatenar3 = "seiscientos"
	elif(cien==7):
		concatenar3 = "setecientos"
	elif(cien==8):
		concatenar3 = "ochocientos"
	elif(cien==9):
		concatenar3 =  "novecientos"

	if(miles==1):
		concatenar4 = "mil"
	elif(miles==2):
		concatenar4 = "dos mil"
	elif(miles==3):
		concatenar4 = "tres mil"
	elif(miles==4):
		concatenar4 = "cuatro mil"
	elif(miles==5):
		concatenar4 = "cinco mil"
	elif(miles==6):
		concatenar4 = "seis mil"
	elif(miles==7):
		concatenar4 = "siete mil"
	elif(miles==8):
		concatenar4 = "ocho mil"
	elif(miles==9):
		concatenar4 = "nueve mil"
	print (concatenar4, concatenar3, concatenar2, concatenar1)
