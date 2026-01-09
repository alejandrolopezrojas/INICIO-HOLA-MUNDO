"""
RETO PYTHON – LOGICA EXTREMA (AND / OR / NOT)

REGLAS:
- NO usar if, for, while
- NO listas, funciones ni imports
- SOLO: input, print, variables, int, str, bool, len
- Operadores aritméticos, comparativos y lógicos

EL PROBLEMA:

El programa debe pedir:
- nombre
- edad
- ciudad
- palabra_clave
- numero

El programa debe imprimir UN SOLO booleano (True o False).

El resultado será True SI SE CUMPLE TODO ESTO:

1) El nombre tiene más de 4 caracteres
   O la ciudad tiene exactamente 5 caracteres

2) La edad es mayor o igual a 18
   Y NO es mayor a 30

3) La palabra_clave NO está vacía
   Y su longitud NO es impar

4) El nombre y la ciudad NO son iguales

5) Se cumple AL MENOS UNA de estas:
   - La primera letra del nombre es menor (ASCII) que la primera letra de la ciudad
   - La última letra de la palabra_clave es mayor (ASCII) que la última letra del nombre

6) El numero cumple:
   - Está entre 1 y 50
   - Y NO es múltiplo de 5

TODO debe resolverse en UNA SOLA expresión lógica.
"""

nombre = input("nombre = ")
edad = int(input("edad = "))
ciudad = input("ciudad = ")
palabra_clave = input("palabra_clave =")
numero = int(input("numero = "))
numero_str = str(numero)
print(
    (len(nombre) > 4 or len(ciudad) == 5)
    and edad >= 18
    and not (edad > 30)
    and bool(palabra_clave)
    and len(palabra_clave) % 2 == 0
    and nombre != ciudad
    and (nombre[0] < ciudad[0] or palabra_clave[-1] > nombre[-1])
    and (numero > 1 and numero < 50)
    and not (numero % 5 == 0)
)