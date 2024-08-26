#Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. 
#Después debe mostrar por pantalla la paga que le corresponde.

horasTrabajadas = int(input("Ingresa el número de horas trabajadas: "))
precioPorHora = int(input("Ingresa el pago por hora: "))

print("Este es el pago correspondiente",horasTrabajadas*precioPorHora)