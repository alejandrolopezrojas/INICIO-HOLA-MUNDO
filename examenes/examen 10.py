"""
EXAMEN PYTHON – PUNTO ÚNICO INTEGRADOR

Pide:
- nombre
- apellido
- edad (int)
- ciudad
- palabra clave
- número (int)

Crea:
- lista comidas con 3 strings
- lista perfil con todos los datos

Imprime UN SOLO BOOLEANO que sea True solo si:

- len(nombre) >= 4
- len(apellido) es impar
- edad >= 16
- ciudad no está vacía
- len(palabra_clave) es par
- nombre != palabra_clave
- nombre[0] < apellido[0]
- apellido[-1] > palabra_clave[-1]
- número entre 10 y 100
- último dígito del número no es "0" ni "5"
- len(nombre) + len(apellido) > número / 2
- len(perfil) > 5
- len(comidas) >= 3
- comidas[0] != palabra_clave

TODO en una sola expresión lógica.
"""
nombre = input("nombre= ")
apellido = input("apellido= ")
edad  = int(input("edad= "))
ciudad = input("ciudad= ") 
palabra_clave = input("palabra_clave= ")
comidas = ["arroz", "fideos", "pan"]
numero = int(input("número= ")) 

perfil = [nombre, apellido, edad, ciudad, palabra_clave, numero] 
print(perfil)

print(
    (nombre.startswith("a") or nombre.startswith("A"))
    and (apellido.count("o") >= 1 or apellido.count("O") >= 1)
    and not(ciudad.startswith("x"))
    and nombre.lower() != palabra_clave.lower()
    and len(apellido) > len(palabra_clave)
    and (numero >= 10 and numero <= 100)
    and not(str(numero).count("0") >=1)
    and ((len(nombre) + len(apellido)) > numero / 2)
    and comidas.count("pizza") >= 1
    and comidas[0][0] != palabra_clave[0]
)














