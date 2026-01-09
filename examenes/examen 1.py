
"""
EXAMEN 1 – FUNDAMENTOS DE PYTHON

Punto 1:
Crea variables para tu nombre, edad y altura.
Imprime una frase con esos datos en una sola línea.

Punto 2:
Crea dos variables a = 10 y b = 3.
Imprime la suma, resta, multiplicación y división.

Punto 3:
Solicita al usuario su nombre y su edad.
Imprime el nombre registrado y la edad que tendrá el próximo año.

Punto 4:
Solicita al usuario dos números.
Imprime la suma y la multiplicación de ambos.

Punto 5:
Solicita la edad al usuario.
Imprime True si es mayor o igual a 18, False en caso contrario.

Punto 6:
Crea una variable num.
Imprime su tipo de dato y el resultado de multiplicarlo por 2.

Punto 7:
Solicita el nombre y el año de nacimiento.
Imprime cuántos años tendrá en el año 2026.
"""


#punto 1

edad= 16
nombre= "Alejandro"
altura= 1.83
print("hola, mi nombre es", nombre, "mi edad es", edad, "y mi altura es", altura)



#punto 2
a = 10
b = 3

print(a+b)
print(a-b)
print(a*b)
print(a/b)



#punto 3

nombre = input("ingrese su nombre= ")
edad = int(input("ingrese su edad= "))
print("nombre registrado=", nombre)
print("esta es tu edad el proximo año= ", edad+1)



#punto 4

n1, n2 = int(input("ingrese n1= ")), int(input("ingrese n2= "))
print(n1+n2)
print(n1*n2)


#punto 5
edad = int(input("ingrese su edad= "))
print(edad>=18) 



#punto 6

num = int(input("ingrese numero= "))
print(type(num))
print(num * 2)


#punto 7

nombre, naci = input("escribe tu nombre "), int(input("y tu año de nacimiento= "))
print("hola", nombre, "en 2026 tendras", 2026-naci)

















