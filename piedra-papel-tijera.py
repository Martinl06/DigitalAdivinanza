print("--------------------------------------")
print("Bienvenidos al piedra, papel o tijera")

jugador1 = input("Ingrese su nombre: ")
jugador2 = input("Ingrese su nombre: ")



intentos = 0
max_intentos = 3
juego = False

while not juego and intentos < max_intentos:
    eleccion1 = input("Que elijes?? piedra, papel o tijera??: ").lower()
    eleccion2 = input("Que elijes?? piedra, papel o tijera??: ").lower()
    
    condicion1 = eleccion1 == "piedra" and eleccion2 == "tijera"
    condicion2 = eleccion1 == "papel"  and eleccion2 == "piedra"
    condicion3 = eleccion1 == "tijera" and eleccion2 == "papel"
    
    if eleccion1 == eleccion2:
            print("Empataron")
    elif condicion1 or condicion2 or condicion3:
            print(f"Ha ganado el jugador: {jugador1}")
    else:
            print(f"Ha ganado el jugador: {jugador2}")

    intentos += 1  

if not intentos < max_intentos:
    print("El juego ha terminado")