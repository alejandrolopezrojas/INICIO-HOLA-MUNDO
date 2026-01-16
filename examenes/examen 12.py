num = input("ingrese dato= ")

if  num == ("") or num.isspace():
    print("vacio")
elif num == "0":
    print("0")
elif num.isnumeric():
    print("positivo")
elif num.isalpha():
    print("texto")
elif num.isalnum():
    print("mixto")
elif num.count(".") == 1 and num.replace(".", "").isnumeric:
    print("decimal valido")
elif num.startswith("-") and num.replace("-", "").isnumeric():
    print("negativo")
elif not num.isnumeric() and not num.isalpha():
    print("formato invalido")




    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    