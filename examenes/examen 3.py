"""
RETO PYTHON – NIVEL AVANZADO

Reglas:
No se permite el uso de if, for, while, listas, funciones ni imports.
Solo se pueden usar: print, input, variables, int, str, bool,
operadores aritméticos, comparativos, lógicos y len.
El programa debe ejecutarse sin errores.

Punto 1:
Solicita dos números al usuario (ingresados como texto).
Imprime:
- la suma como número
- el tipo de la suma
- si la suma es mayor o igual a 100

Punto 2:
Solicita una palabra al usuario.
Imprime:
- la palabra
- la cantidad de caracteres
- si la longitud es par

Punto 3:
Sin ejecutar el código, determina el resultado (True o False) de las siguientes comparaciones
y explica la razón:
- "Zebra" > "apple"
- "python" < "Python"
- "aaa" > "aa"

Punto 4:
Solicita una entrada cualquiera al usuario.
Convierte el valor a booleano e imprime:
- el valor original
- el valor booleano
- el tipo del booleano
Luego responde:
¿Qué debe escribir el usuario para que el booleano sea False?

Punto 5:
Solicita dos palabras al usuario.
El programa debe imprimir True o False según se cumpla que:
- la primera palabra tenga una longitud mayor o igual que la segunda
- y ambas palabras no sean iguales
"""

#punto 1
num1 = int(input("num1= "))
num2 = int(input("num2= "))
num3 = num1 + num2
print("la suma de estos dos numeros es= ", num3)
print(type(num3))
print(num3>=100)


#punto 2
pal = input("escriba una palabra= ")
print(len(pal))
print(((len(pal) % 2)//1) != 1)


#punto 3
'''
true, porque la mayuscula al inicio de zebra va antes
true, por la P mayuscula al inicio de el segundo python
false, creo que al ser iguales no es mayor
'''


#punto 4
x = input("escribe lo que sea= ")
xb = bool(x)

print(x)
print(xb)
print(xb == 1)
'''para que bool sea false no tendria queescribir nada,
 ya que false corresponde a 0'''


#punto 5
p1, p2 = input("p1= "), input("p2= ")
print(len(p1) >= len(p2) and p1 != p2)
































