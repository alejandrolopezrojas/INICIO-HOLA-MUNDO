"""
EXAMEN 2 – OPERADORES Y COMPARACIONES

Punto 1:
Solicita dos números al usuario.
Imprime la suma de ambos, el tipo del resultado y si la suma es mayor o igual a 100.

Punto 2:
Solicita una palabra al usuario.
Imprime la cantidad de caracteres y si la longitud es par.

Punto 3:
Analiza las siguientes comparaciones de cadenas y escribe si el resultado es True o False,
explicando mentalmente el porqué:
- "Zebra" > "apple"
- "Python" > "python"
- "hola" > "hola"

Punto 4:
Solicita cualquier valor al usuario.
Convierte el valor a booleano y muestra el valor original, su conversión a bool
y el resultado de compararlo con True.

Punto 5:
Solicita dos palabras.
Imprime True si la primera tiene más o igual caracteres que la segunda
y además son diferentes.
"""

#punto 1
nombre, año = input("introduzca su nombre= "), int(input("introduzca su año de nacimiento= "))
print("su nombre es", nombre, type(nombre))
print("y su edad en el 2026 es= ", 2026-año )



#punto 2
105
type str
15
int




#punto 3

frase = input("escribe una frase= ")
valor = print("el numero de caracteres es= ", len(frase))
print(type(valor))


#punto 4
"""
siendo sincero todavia no he aprendido sobre bool
pero creo que puedo saber.
si el valor es 0 puede ser false o nonetype, y si el valor es 5
el valor sera true
"""


#punto 5

edad = int(input("Edad: "))
print("El próximo año tendrás", edad + 1)