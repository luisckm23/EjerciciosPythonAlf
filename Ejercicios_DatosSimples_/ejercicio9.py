#Escribir un programa que pregunte al usuario una cantidad a invertir
#El interés anual y el número de años y muestre por pantalla el capital obtenido de la inversión

inversion = float(input("Ingresa la cantidad a invertir: "))
añosInversion = int(input("Ingresa los años a invertir: "))
tasaInversion = float(input("Ingresa la tasa de interés anual: "))

print("Cpital final: " + str(round(inversion *(tasaInversion / 100 + 1) ** añosInversion,2)))