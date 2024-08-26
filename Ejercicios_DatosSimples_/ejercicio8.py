#Escribir un programa que pida al usario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente de <c> y 
#un resto de <r> 

n = int(input("Ingresa un numerador: "))
m = int(input("Ingresa un denominador: "))

cociente =  n//m
resto = n%m

print("El cociente de la división es "+str(cociente)+" y el resto es "+str(resto))