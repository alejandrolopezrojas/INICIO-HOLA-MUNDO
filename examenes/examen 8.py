"""
EXAMEN PYTHON – NIVEL AVANZADO (SIN IF)

Punto 1
Pide al usuario:
- nombre
- apellido
- edad (int)

Imprime una sola línea que muestre:
- nombre y apellido en mayúsculas
- edad el próximo año
- si el nombre tiene más caracteres que el apellido (True / False)

Punto 2
Pide:
- una palabra
- un número

Imprime:
- la palabra invertida
- la longitud de la palabra
- si la longitud es impar
- si el último dígito del número no es "0" ni "5"

Punto 3
Crea una lista llamada datos con:
- nombre
- ciudad
- edad
- estatura

Luego:
- imprime la lista
- cambia la edad por edad + 1
- agrega un país
- elimina la ciudad
- imprime el último elemento
- imprime el tamaño final de la lista

Punto 4
Pide dos palabras.

Imprime UN SOLO BOOLEANO que sea True solo si:
- no son iguales
- la primera es más larga que la segunda o tienen la misma longitud
- la primera letra de la primera palabra es menor (ASCII) que la primera letra de la segunda

Punto 5 (FINAL)
Pide:
- nombre
- palabra clave
- número

Imprime una sola expresión lógica que devuelva True solo si:
- el nombre tiene al menos 4 caracteres
- la palabra clave tiene longitud par
- el nombre y la palabra clave son diferentes
- la segunda letra del nombre es mayor que la segunda letra de la palabra clave
- el número está entre 10 y 100
- el nombre NO empieza con la misma letra que la palabra clave
"""
#punto 1
"""nom, ap, edad = input("nombre= "), input("apellido= "), int(input("edad= "))
print(nom.upper(), " ", ap.upper()," el otro año tendras=", edad + 1, len(nom) > len(ap))
"""

#punto 2
"""palabra = input("Una palabra= ")
numero = int(input("un numero= "))
print(palabra[::-1])
print(len(palabra))
print((len(palabra)%2)==0)
print((numero%5) != 0)"""


#punto 3
datos = ["alejandro", "florida", 16, 1.83]
print(datos)
datos[2] = datos[2] + 1
datos.append("colombia")
datos.remove("florida")
print(datos[-1])
print(len(datos))


#punto 4
"""pal1, pal2 = input("="), input("=")
print(
    pal1 != pal2 
    and len(pal1) >= len(pal2) 
    and pal1[0] < pal2[0]
)"""


#punto 5
Nombre = input("=")
Palabra_clave = input("=")
Numero = int(input("="))

print(
    len(Nombre) >= 4
    and (len(Palabra_clave) % 2)==0
    and Nombre != Palabra_clave
    and Nombre[1] > Palabra_clave[1]
    and (Numero >= 10 and Numero <= 100)
)



































