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




