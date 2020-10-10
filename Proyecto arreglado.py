import random

e=random.choice((0,1,2,3))
def geografia(e):
    P1=[["Ciudad de México", "Toluca", "Ciudad de México","Querétaro"],
    ["Toluca", "Toluca", "Ciudad de México", "Chihuahua"],
    ["Colima", "Ciudad de México", "Colima", "Hermosillo"],
    ["Querétaro", "Hermosillo", "Mexicali","Toluca"]]
    R1=["Ciudad de México", "Estado de México", "Colima", "Querétaro"]
    print("De las siguientes opciones, cuál es la capital de",R1[e])
    for x in range(1,4,1):
        print(P1[e][x])
    RG=str(input("Escribe el nombre de la respuesta correcta"))
    RC=P1[e][0]
    if(RG==RC):
        print("Correcto")
    else:
        print("falso")


def suma(x):
    y=random.choice((1,2,3,4,5,6,7,8,9,10))
    print("Cuanto es la suma de", x, " + ", y)
    resultado=int(input("Coloca tu resultado"))
    c=x+y

    if(c==resultado):
        print("respuesta correcta")
    else:
        print("Respuesta incorrecta, necesitas repasar sumas")
    

def division(x):
    y=random.choice((1,2,3,4,5,6,7,8,9,10,20,30,40,50))
    print("Cuanto es la división de", x, " / " , y)
    resultado=float(input("Coloca tu resultado"))
    c=x/y
    
    if(c==resultado):
        print("respuesta correcta")
    else:
        print("Respuesta incorrecta")
        
        
def multiplicación(x):
    y=random.choice((2,4,6,8,9,10,11,12,13,14,15))
    print("Cuanto es la multiplicación de", x, " * ", y)
    resultado=int(input("Coloca tu resultado"))
    c=x*y
    
    if(c==resultado):
        print("Respuesta correcta")
    else:
        print("Respuesta incorrecta")
        
def resta(x):
    y=random.choice((1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20))
    print("Cuanto es la resta de", x, "-", y)
    resultado=int(input("Coloca tu resultado"))
    c=x-y
    
    if(c==resultado):
        print("Respuesta correcta")
    else:
        print("Respuesta incorrecta")

Nombre=str(input("Escribe tu nombre"))
x=random.choice((2,4,6,8,10,12))
print("El programa cuenta con 2 dificultades siendo 1 el fácil y 2 el dificil")
Nivel=int(input("Selecciona Nivel de dificultad y coloca '4' para salir"))

if(Nivel==1):
    print("Temas: 1=Suma     2=Resta      3=División       4=Multiplicación")
    tema=int(input("selecciona un Tema"))
    if(tema==1):
        print(suma(x))
    elif(tema==3):
        print(division(x))
    elif(tema==4):
        print(multiplicación(x))
    elif(tema==2):
        print(resta(x))
        
        
        
        
        
