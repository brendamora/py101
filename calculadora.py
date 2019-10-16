#calculadora basica

numero1 = int (raw_input ("digite su primer numero: "))
numero2 = int (raw_input ("digite su segundo numero: "))

suma = numero1 + numero2
resta = numero1 - numero2
producto = numero1 * numero2
division = numero1 / numero1
potencia = numero1 ** numero2

print (str(numero1) + " + " + str(numero2) + " = " + str(suma))
print (str(numero1) + " - " + str(numero2) + " = " + str(resta))
print (str(numero1) + " * " + str(numero2) + " = " + str(producto))
print (str(numero1) + " / " + str(numero2) + " = " + str(division))
print (str(numero1) + " ** " + str(numero2) + " = " + str(potencia))


""" base por altura = area rectangulo"""

base = int (raw_input ("digite la base del triangulo: "))
altura = int (raw_input ("digite la altura del triangulo ese: "))

area = base * altura

print (str(base) + "*" + str(altura) + "=" + str(area)) 
