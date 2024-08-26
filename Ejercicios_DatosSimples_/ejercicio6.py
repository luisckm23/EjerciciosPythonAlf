#Escribir un programa que lea un entero positivo, n, 
#introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta n.
#La suma de los  primeros enteros positivos puede ser calculada de la siguiente forma:
# suma=n(n+1)/2

numeroUsuario = int(input("Ingresa un número: "))
suma = numeroUsuario*(numeroUsuario+1)/2
print("La suma de los primeros números enteros desde 1 hasta"+str(numeroUsuario)+"es"+str(suma))