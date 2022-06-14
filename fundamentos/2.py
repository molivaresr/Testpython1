
import random
import math
# Prueba 2
# x = int(input("Ingresa un número: "))
# print("Tu número es: " + str(x))
# print(x)
# print(random.randrange(1, 30))
# Ejercicio 11
# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, 
# y muestre por pantalla el capital obtenido en la inversión.
money = int(input("Ingrese la cantidad a invertir: "))
ti = int(input("Ingrese la tasa anual de interés %: "))
years = int(input("Ingrese los años que desea mantener su depósito: "))
save = round(money * (ti/100 + 1)** years,2)
print("El capital obtenido es: " + str(save)+ " €")
# Ejercicio 12
# Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. 
# Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular 
# el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. 
# Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del 
# paquete que será enviado.
clown = int(input("Ingrese la canitdad payasos: "))
dolly = int(input("Ingrese la cantidad de muñecas: "))
wclown = 112
wdolly = 75 
wpaq = (clown * wclown) + (dolly * wdolly)
print("El peso total del paquete es: " + str(wpaq))
# Ejercicio 13
# Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. 
# Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final 
# de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en 
# la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla 
# la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.
ca = float(input("Ingrese la cantidad que desea ahorrar: "))
i = 0.04
a1 = round((1+i)*ca,2)
a2 = round((1+i)*a1,2)
a3 = round((i+1)*a2,2)
print("Los ahorros al primer año son: " + str(a1))
print("Los ahorros al segundo año son: " + str(a2))
print("Los ahorros al tercer año son: " + str(a3))
# Ejercicio 14
# Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. 
# Escribir un programa que comience leyendo el número de barras vendidas que no son del día. 
# Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca 
# y el coste final total.
pan = float(3.49)
descuento = float(0.6)
npanold = int(input("Cuantas barras has vendido hoy: "))
coste = float(round((npanold*(pan-(pan*descuento))),2))
print("El precio de la barra es: " + str(pan))
print("El descuento si la barra no es fresca es: " + str(100*descuento) + " %")
print("El coste total es: " + str(coste)+" €")