import math

# NO LEER
print(int(math.pow(3,3)))
x = 4 # x is of type int
y = 5 # x is now of type str
# Ejercicio 1
print ('Hola Mundo')
print(x + y)
# Ejercicio 2
a = "¡Hola "
print(a)
# Ejercicio 3
b = input("Introduce tu nombre")
print(a + b +" !")
# Ejercicio 4 
n = input("Introduce un número:")
print((b+ "\n") * int(n))
# Prueba mía
c = input("Introduce un número:")
print(x * y * int(c))
# Ejercicio 5
print(b.upper() + " tiene " + str(len(b)) + " letras")
# Ejercicio 6
print (((3 + 2)/(2 * 5))**2)
# Ejercicio 7
t = float(input("Introduce el número de horas "))
p = float(input("Introduce el valor que cobras por hora "))
print("Te corresponden " + str(t * p) + " €")
# Ejercicio 8 
"""Escribir un programa que lea un entero positivo, n , 
introducido por el usuario y después muestre en pantalla la suma de todos los 
enteros desde 1 hasta n. La suma de los n primeros enteros positivos puede ser 
calculada de la siguiente forma:"""
# Opción A
# c = input("Introduce un número: ")
# print((int(c)*(int(c)+1))/2)

# Opción B

# numero= int(input("Introduce un número: "))
# if numero < 0:
#     numero  = numero * -1
#     suma = -1 * ((numero  * (numero + 1))/2)
    
# else :
#     suma = (numero  * (numero + 1))/2
# print(f"La sumas es : {suma}")

# Ejercicio 9
# w = float(input("Indique su peso en Kg: "))
# h = float(input("Iniduqe su estatura en Metros: "))
# imc = w/h**2 
# print(round(imc,ndigits=2))
# print("Su Indice de masa corporal es " + str(imc) + " Kg/m2")
# Ejercicio 10
print(20 // 7)
print(20 % 7)
n = input("Ingrese el dividendo: ")
m = input("Ingrese el divisor: ")
print("La operación " + n + " entre " + m + " da un coeciente " + str(int(n) // int(m)) + " y un resto " + str(int(n) % int(m)))