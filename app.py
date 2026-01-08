goles = {}
enfermeria = ["rocha", "batres", "cupillar"]

while True:
    print("\n----### MENU DEL EQUIPO ###----")
    print("Opcion 1: Anotar goles.")
    print("Opcion 2: Consultar jugador.")
    print("Opcion 3: Informe del equipo.")
    print("Opcion 4: Salir")
    
    try:
        opcion_input = input("Elige una opcion: ")
        opcion = int(opcion_input)
    except ValueError:
        print("Por favor, introduce un número válido.")
        continue

    if opcion == 1:
        jugador = input("Introduce el nombre de un jugador: ")
        if jugador in goles:
            print("Ese jugador ya existe. Actualizando sus goles.")
            while True:
                try:
                    golesJ = int(input("Introduce el NUEVO numero de goles: "))
                    goles[jugador] = golesJ
                    break
                except ValueError:
                    print("Valor no valido.")
        elif jugador in enfermeria:
            print("Ese jugador no puede marcar goles, esta lesionado.")
        elif jugador not in goles:
            while True:
                try:
                    golesJ = int(input("Introduce el numero de goles: "))
                    goles[jugador] = golesJ
                    break
                except ValueError:
                    print("Valor no valido, introduce un numero entero por favor.")
        
        print(f"Estado actual: {goles}")

    elif opcion == 2:
        while True:
            jugadorP = input("Introduce el nombre del jugador a consultar: ")
            if jugadorP not in goles:
                print("Ese jugador no ha marcado goles o no está en el registro.")
                break 
            else:
                # CORREGIDO: Usamos la variable num_goles para no romper el diccionario
                print(f"--> {jugadorP} ha marcado {goles[jugadorP]} goles.")
                break

    elif opcion == 3:
        totalgoles = 0
        print("--- INFORME ---")
        for jugador, num_goles in goles.items():
            print(f"{jugador} ---- {num_goles}")
            totalgoles = totalgoles + num_goles
        print(f"El equipo ha marcado un total de {totalgoles} goles esta temporada.")

    elif opcion == 4:
        print("Saliendo del menu del equipo, bye.")
        break
