#punto 1
""" num = input("ingrese dato= ")

if  num == ("") or num.isspace():
    print("vacio")
elif num.count(".") == 1 and num.replace(".", "").isnumeric():
    print("decimal valido")
elif num.startswith("-") and num.replace("-", "").isnumeric():
    print("negativo")
elif num == "0":
    print("0")
elif num.isnumeric():
    print("positivo")
elif num.isalpha():
    print("texto")
elif num.isalnum():
    print("mixto")
else:
    print("formato invalido") """

#punto 2
""" edad = input("edad= ")
if edad == "" or edad.isspace():
    print("Edad vacía" )   
elif not edad.isnumeric():
    print("edad invalida")
elif edad.count("-") == 1 and edad.replace("-", "").isnumeric():
    print("edad invalida")
elif edad.count(".") == 1 and edad.replace(".", "").isnumeric():
    print("edad invalida")
elif int(edad) < 18 or int(edad) > 120:
    print("acceso denegado")
elif edad == "18":
    print("acceso permitido")
else:
    print("acceso permitido") """

#punto 3
""" user = input("user= ")
password = input("password= ")
if user == "" or user.isspace() or password == "" or password.isspace():
    print("user y/o contraseña esta vacio")
elif user == "admin" and password == "1234":
    print("acceso total")
elif user.isalpha() and password.isnumeric():
    print("valido")
elif user.isnumeric():
    print("usuario invalido")
elif password.isalpha():
    print("password invalida")
else:
    print("formato invalido") """

#punto 4
a = input("a= ")
b = input("b= ")

if a == "" or a.isspace() or b == "" or b.isspace():
    print(" ""A"" y/o ""B"" vacios")
elif b == "0" or b == "0.0":
    print("divición invalida")
elif (a.isnumeric and b.isnumeric) or a.count(".") == 1 and a.replace(".", "").isnumeric() or b.count(".") == 1 and b.replace(".", "").isnumeric() and ((a + b).count("-") == 2 or (a + b).count("-") == 0):
        print("el resultado de la divición es= ", float(a) / float(b))
        if a.startswith("-") == 1 and a.replace("-", "") or b.startswith("-") == 1 and b.replace("-", "") and not (a + b).count("-") == 2:    
            print("resultado negativo")
else:
    print("formato invalido")

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    