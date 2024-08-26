# Una panadería vende barras de pan a 3.49€ cada una.
# El pan que no es el día tiene un descuento del 60%.
# Escribir un programa que comience leyendo el número de barras vendidas que no son del día. 
# Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y
# el coste final total.


noVendido = int(input("Cuantas barras de pan no se vendieron: "))
descuento = 3.49 * (.40)
descuentoTotal = descuento*noVendido

print(f"El costo total de pan con descuento es: {round(descuentoTotal,2)}")