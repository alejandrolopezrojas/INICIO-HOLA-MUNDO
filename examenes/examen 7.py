#punto 1
nombre = "alejandro"
edad = "lopez"
estatura = "rojas"
print(f"nombre= {nombre} edad= {edad} estatura= {estatura}")

#punto 2
num1 = int(input("a= "))
num2 = int(input("b= "))

print("suma\t", num1 + num2,
      "\nresta\t", num1 - num2,
      "\nmulti\t", num1 * num2,
      "\ndiv\t", num1 / num2,
      "\n\t", num1 > num2)

#punto 3
palabra = "programación"
print(palabra[0])
print(palabra[-1])
print(palabra[0:3])
print(palabra[::-1])

#punto 4
texto = "PyTHon"
print(texto.lower())
print(texto.upper())
print(texto.count("o"))

#punto 5
pal = input("escriba la palabra= ")
print(pal)
print(len(pal))
print((len(pal)%2)==0)

#punto 6
persona = ["alejandro", "lopez", 16, 1.83]
print(persona)
print(persona[1])
print(persona[-1])
print(len(persona))

#punto 7
persona.append("floridablanca")
persona.insert(0, "colombia")
persona[3] = 18
persona.pop(-2)
print(persona)

#punto 8
pais, nombre, apellido, edad, lugar = persona
print(f"{apellido} {nombre} {edad}")



















