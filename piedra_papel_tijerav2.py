# piedra_papel_tijera.py
# Juego simple contra la computadora: primera versión

import random

opciones = ["piedra", "papel", "tijera"]

print("¡Bienvenido! Vamos a jugar a Piedra, Papel o Tijera.")
print("Escribí tu jugada (piedra/papel/tijera).")

ronda = 1
puntos_usuario = 0
puntos_pc = 0
rondas_totales = int(input("Cuantas rondas quiere jugar? Eliga un numero entre 1 y 100.")) #Variable agregada para terminar antes
while rondas_totales <= 0 or rondas_totales >= 100:
        print("Entrada inválida de rondas.")
        rondas_totales = int(input("Cuantas rondas quiere jugar?")) #Variable agregada para terminar antes

dif = int(rondas_totales / 2) + 1 #Aca puse la diferencia para saber cuando terminar antes el while.

while ronda <= rondas_totales: #HICE ESTA MODIFICACIÓN QUE HACE QUE LA PARTIDA SEA AL MEJOR DE 5.

    print(f"\nRonda {ronda}")
    jugada_usuario = input("Tu jugada: ").strip().lower()

    opcionCorrecta = True
    while opcionCorrecta: #WHILE HECHO PARA VOLVER A ELEGIR OPCION SIN VOLVER AL WHILE DE ARRIBA SIN CONTINUE.
        if jugada_usuario not in opciones:
            print("Entrada no válida. Debe ser piedra, papel o tijera.")
            jugada_usuario = input("Tu jugada: ").strip().lower()
        else:
            opcionCorrecta = False #SI DA FALSE ES XQ LA OPCION ELEGIDA ESTA EN LA LISTA DE MOVIMIENTOS.
       

    jugada_pc = random.choice(opciones)
    print(f"La computadora eligió: {jugada_pc}")

    if jugada_usuario == jugada_pc:
        print("Empate.")
    elif (jugada_usuario == "piedra" and jugada_pc == "tijera") or \
         (jugada_usuario == "papel" and jugada_pc == "piedra") or \
         (jugada_usuario == "tijera" and jugada_pc == "papel"):
        print("¡Ganaste la ronda!")
        puntos_usuario += 1
    else:
        print("Perdiste la ronda.")
        puntos_pc += 1

    if puntos_usuario == dif or puntos_pc == dif: #Con este if voy verificando cuando alguno ya no alcanze al otro.
        print("La partida termina por diferencia de puntos.")
        break #Si se ejecuta el break termina el bucle del while.

    ronda += 1

print("\n=== Resultado final ===")
print(f"Puntos del Usuario: {puntos_usuario} | Puntos de la PC: {puntos_pc}")

if puntos_usuario > puntos_pc:
    print("¡Felicidades! Ganaste el juego.")
elif puntos_usuario < puntos_pc:
    print("La computadora ganó el juego.")
else:
    print("Empate total.")