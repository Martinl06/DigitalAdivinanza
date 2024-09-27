import random

numero_secreto = random.randint(1,51)
adivinado = False
intentos = 0
cantidad_intentos = 7


while not adivinado and intentos < cantidad_intentos:
    
    numero = int(input("Ingrese el numero sorpresa: "))
    if numero == numero_secreto:
        print(f"Adivinaste, el numero era: {numero}")
        adivinado = True
    elif numero > numero_secreto:
        print("El numero es menor" ) 
    elif numero < numero_secreto:
        print("El numero es mayor")   
    else:
        print("No es ese, segui intentandolo")
    intentos += 1    
        
if not intentos < cantidad_intentos:
    print("Agotaste todos los intentos")