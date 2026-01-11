nombre = input("nombre= ")
apellido = input("apellido= ")
edad  = int(input("edad= "))
ciudad = input("ciudad= ")
palabra_clave = input("palabra_clave= ")
numero  = int(input("número= "))

print(
    len(nombre) >=4
    and (len(apellido) % 2) == 1
    and edad >= 16
    and float(ciudad)
    and (len(palabra_clave)%2) == 0
    and nombre != palabra_clave
    and nombre[0] < apellido[0]
    and apellido[-1] > palabra_clave[-1]
    and (numero >= 10 and numero <=100)
    and (str(numero[-1]) != "0" and str(numero[-1]) != "5")
    and (len(nombre) + len(apellido) > numero / 2)
    and nombre[0] != palabra_clave[0]  
)




















