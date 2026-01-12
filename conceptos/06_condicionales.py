    #CONDICIONALES
condicion = True
if condicion:
    print("la condicion es true")#if ejecuta cuando una condición es

condicion2 = False
if condicion2:
    print("esta condicion no se cumplira porque es false")

    #LIMITAR CONDICIONES
"""PODEMOS AÑADIR COSAS QUE DEBEN CUMPLIRSE PARA QUE UNA CONDICIÓN SEA TRUE Y EL IF GENERE UN RESULTADO"""

condicion3 = 8 * 2
if condicion3 == 16:
    print("la condicion se ha cumplido")

if condicion3 == 24:
    print("esta condicion no se cumple ya que ""condicion3"" no es 24")
    
    #ELSE
"""cuando no se cumple la condición del ""IF"" se cumple lo que else diga"""

condicion4 = 24
if condicion4 == 16:
        print("la condicion se ha cumplido")
else:
     print("la condición no se ha cumplido")


    #CONCATENAR CONDICIONES
"""lo que habiamos aprendido en strings y operadores lo podemos aplicar todo a la vez, incluso usando un input"""

""" numero = int(input("ingrese un numero= "))
if numero > 10 and numero <100 and (numero % 2) == 0:
     print("la condición multiple es correcta")
else:
     print("la condición multiple es incorrecta") """
    
    #ELIF
"""cuando queremos añadir uno o mas casos especiales a una condición"""
     
x_elif = int(input("ingrese un numero= "))
if x_elif > 10 and x_elif <100 and  (x_elif % 2) == 0:
     print("la condición multiple es correcta")

 
    
    
    
    
    
    
    
    
    
    
    
    
