goles = {}
enfermeria = ["Rocha", "Batres", "Cupillar"]

while True:
    print("\n--- MENÚ DEL EQUIPO ---")
    print("1. Anotar goles")
    print("2. Consultar Jugador")
    print("3. Informe de Equipo")
    print("4. Salir")

    try:
        opcion = int(input("Seleccione una opción: "))
    except ValueError:
        print(">> Error: Por favor, ingresa un número válido.")
        continue

    if opcion == 1:
        jugador = input("¿Qué jugador quieres añadir?: ").strip().title()

        if jugador in enfermeria:
            print(f">> ¡Atención! {jugador} está en la enfermería y no puede jugar.")
        else:
            while True:
                try:
                    gol = int(input(f"¿Cuántos goles anotó {jugador}?: "))
                    if gol < 0:
                        print("No se pueden anotar goles negativos.")
                        continue

                    if jugador in goles:
                        goles[jugador] += gol
                    else:
                        goles[jugador] = gol

                    print(f">> Goles actualizados. {jugador} lleva {goles[jugador]} en total.")
                    break
                except ValueError:
                    print(">> Error: Tiene que ingresar un número entero.")

    elif opcion == 2:
        ver_jugador = input("¿Qué jugador quieres ver?: ").strip().title()
        cantidad = goles.get(ver_jugador)

        if cantidad is not None:
            print(f">> El jugador {ver_jugador} tiene {cantidad} goles.")
        else:
            print(">> El jugador no está en la lista de goleadores.")

    elif opcion == 3:
        if not goles:
            print(">> Aún no se han registrado goles.")
        else:
            print("\n--- INFORME ---")
            total = sum(goles.values())
            for j, g in goles.items():
                print(f"- {j}: {g} goles")
            print(f"----------------\nTOTAL DEL EQUIPO: {total} goles")

    elif opcion == 4:
        print("Saliendo de la aplicación...")
        break

    else:
        print(">> Opción no válida, intenta del 1 al 4.")
