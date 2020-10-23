
"""
Este programa consiste en un Minijuego escolar para poner aprueba tus conocimientos en diferentes
materias
"""
import random
"""
Mande a llamar random el cual me permitira en mis funciones cosas y variables de manera aleatoria
"""

def geografia(e, correcta):
    """
    Esta función hace preguntas aleatorias acerca de las capitales de México
    """
    P1=[["Ciudad de México", "Toluca", "Ciudad de México","Querétaro"],
        ["Toluca", "Toluca", "Ciudad de México", "Chihuahua"],
        ["Colima", "Ciudad de México", "Colima", "Hermosillo"],
        ["Querétaro", "Querétaro", "Mexicali","Toluca"],
        ["Jalisco", "Jalapa", "León", "Jalisco"],
        ["Mexicalli", "Culiacan", "Chihuaha", "Morelia"]]
    R1=["Ciudad de México", "Estado de México", "Colima", "Querétaro", "Guadalajara", "Baja California"]
    print("De las siguientes opciones, cuál es la capital de",R1[e])
    for x in range(1,4,1):
        print(P1[e][x])
    RG=str(input("Escribe el nombre de la respuesta correcta"))
    RC=P1[e][0]
    if(RG==RC):
        print("Correcto")
        correcta=correcta + 1
    else:
        print("Incorrecto")
        correcta=correcta
    return correcta


def suma(x, correcta):
    """
    Esta función hace operaciones de suma con numeros aleatorios
    """
    y=random.choice((1,2,3,4,5,6,7,8,9,10))
    print("Cuanto es la suma de", x, " + ", y)
    resultado=int(input("Coloca tu resultado"))
    c=x+y
    if(c==resultado):
        print("respuesta correcta")
        correcta=correcta + 1
    else:
        print("Respuesta incorrecta, necesitas repasar sumas")
        correcta=correcta
    return correcta    
        
    
    

def division(x2, correcta):
    """
    Esta función hace operaciones de división con numeros aleatorios
    """
    y=random.choice((1,2,3,4,5,6,7,8,9,10,20,30,40,50))
    print("Cuanto es la división de", x2, " / " , y)
    resultado=float(input("Coloca tu resultado"))
    c=x2/y
    
    if(c==resultado):
        print("respuesta correcta")
        correcta=correcta + 1
    else:
        print("Respuesta incorrecta")
        correcta=correcta
    return correcta


        
        
def multiplicación(x3, correcta):
    """
    Esta función hace operaciones de multiplicación con numeros aleatorios
    """
    y=random.choice((2,4,6,8,9,10,11,12,13,14,15))
    print("Cuanto es la multiplicación de", x3, " * ", y)
    resultado=int(input("Coloca tu resultado"))
    c=x3*y
    
    if(c==resultado):
        print("Respuesta correcta")
        correcta=correcta + 1
    else:
        print("Respuesta incorrecta")
        correcta=correcta
    return correcta

        

    
        
def resta(x4, correcta):
    """
    En esta función hacemos operaciones de resta con numeros aleatorios
    """
    y=random.choice((1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20))
    print("Cuanto es la resta de", x4, "-", y)
    resultado=int(input("Coloca tu resultado"))
    c=x4-y
    
    if(c==resultado):
        print("Respuesta correcta")
        correcta=correcta + 1
    else:
        print("Respuesta incorrecta")
        correcta=correcta
    return correcta


    
"""
Aquí metimos nuestro primer menu donde se le indica al usuario que coloque su nombre
y ademas eliga el nivel de dificultad que le gustaría poner
"""
Nombre=str(input("Escribe tu nombre"))
x=random.choice((2,4,6,8,10,12))
print("El programa cuenta con 1 nivel de dificultad y un modo examen")
Nivel=int(input("Selecciona 1 para practicar y 2 para el modo examen"))

if(Nivel==1):
    """
    En caso de que se elija el nivel 1, te dara a escoger que tema quieres practicar, donde
    se te pedira que eligas una opción
    """
    print("Temas: 1=Suma     2=Resta      3=División       4=Multiplicación  5=Geografía")
    tema=int(input("selecciona un Tema"))
    correcta=0
    if(tema==1):
        """
        Si el tema es el 1 te imprimira 5 sumas
        """
        cont=0
        while (cont<5):
            x=random.choice((2,4,6,8,10,12,23,53,65,29,42,51,46,73))
            suma(x, correcta)
            cont=cont+1
        
    elif(tema==3):
        """
        Si el tema es el 3 te imprimira 5 divisiones
        """
        cont=0
        while (cont<5):
            x2=random.choice((1,2,3,4,5,6,7,8,9,10,20,30,40,50))
            division(x2, correcta)
            cont=cont+1
            
        
    elif(tema==4):
        """
        Si el tema es el 4 te imprimira 5 multiplicaciones
        """
        cont=0
        while(cont<5):
            x3=random.choice((1,2,3,4,5,6,7,8,9,10,20,30,40,50))
            multiplicación(x3, correcta)
            cont=cont+1
            
            
            
    elif(tema==2):
        """
        Si el tema es el 2 te imprimira 5 restas
        """
        cont=0
        while(cont<5):
            x4=random.choice((1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20))
            resta(x4, correcta)
            cont=cont+1
            
            
    elif(tema==5):
        """
        Si el tema es el 5 te imprimira 5 preguntas de geografía
        """
        cont=0
        while(cont<5):
            e=random.choice((0,1,2,3))
            geografia(e, correcta)
            cont=cont+1
            
            
        
if(Nivel==2):
    """
    En caso de elegir el nivel 2, te hara 10 preguntas 2 de cada tema donde se te evaluara de acuerdo
    a tu desempeño y se te dara una calificación al final conforme a los aciertos que hayas tenido
    """
    print("EL total")
    print("Se te hará en total 10 preguntas donde se evaluaran tus habilidades")
    np=0
    correcta=0
    Pt=0
    while(np<2):
        e=random.choice((0,1,2,3))
        x=random.choice((2,4,6,8,10,12,14,15,16,17,18,19,20,34,65,78,96,53,13,57,90,23,24,25,26,27,28,29,46))
        x2=random.choice((2,4,6,8,10,12,14,15,16,17,18,19,20,35,40,25))
        x3=random.choice((2,4,6,8,10,12,14,15,16,17,18,60,37,62,87,23,65,57,))
        x4=random.choice((2,4,6,8,10,12,14,15,16,17,18,34,35,36,37,75,85,39,57))
        P1=suma(x, correcta)
        P2=division(x2, correcta)
        P3=multiplicación(x3, correcta)
        P4=resta(x4, correcta)
        P5=geografia(e, correcta)
        Pt=(P1+P2+P3+P4+P5)+Pt
        np=np+1
    correcta=Pt
    Calificacion=correcta*10
    if Calificacion>=90:
        print("Excelente")
        print("Tu calificación fue de ", Calificacion)
    else:
        print("Tu calificación fue de ", Calificacion)