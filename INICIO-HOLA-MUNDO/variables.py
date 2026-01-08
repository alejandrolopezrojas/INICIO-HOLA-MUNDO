#las variables se crean con un "=" y el valor que le queramos dar
edad= 16
nombre= "Alejandro"
altura= 1.83
#luego para imprimirlas se usa print
print(edad)
print(nombre)
print(altura)
"""tambien puedes escribirlas 
juntas y con texto en una sola linea
para esto hay que usar comas,,, entre cada cosa"""
print("hola mi nombre es", nombre, "mi edad es", edad, "y mi altura es", altura)

#podemos pasar una variable de un tipo a otra
vint = 34
vfloat = 2.34
#revisamos que tipo de variable son=
print(type(vint), type(vfloat))

#ahora usando estas funciones las podemos cambiar

vint_a_str = str(vint)
vfloat_a_bool = bool(vfloat)
print(type(vfloat_a_bool))
print(type(vint_a_str))
#como podemos ver ahora estas funciones han cambiado de tipo

"""esto es un experimento rapido,
que pasaria si queremos ver de que
tipo es lo que acabamos de hacer,
un print con variables y funciones adentro """

print(type(print("esto es una prueba", edad)))

#ahora vamos con algunas funciones del sistema

#len sirve para contar caracteres dentro de una función
texto = "adhcdqmndwncumiqhfnqwfomqwof"
num_tex = "34215246534478"

print(len(texto))
print(len(num_tex))

#tambien se pueden hacer varias variables en una sola linea

fruta, animal, x, lugar = "banano", "gato", 13.234, "floridablanca"

print("mi fruta favorita es", fruta, "mi mascota es un", animal, x, lugar)

#IMPUT, ESTO ES BASTANTE IMPORTANTE, NOS PERMITE INGRERSAR DATOS

deporte = input("¿que deporte practicas? ")

print("el deporte que", nombre, "practica es", deporte)

