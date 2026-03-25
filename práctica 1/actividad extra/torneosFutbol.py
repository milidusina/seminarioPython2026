torneo = {}
def calcular_puntaje(p1,p2):
    """devuelve el puntaje que obtuvo el partido pasado como primer parametro"""
    if (p1 == p2):
        puntaje=1
    elif (p1 > p2):
        puntaje =3
    else:
        puntaje =0
    return puntaje

print("-------TORNEO DE FÚTBOL-------")
while True:
    print(""" MENÚ:
        1.  Agregar un equipo
        2.  Registrar un resultado  
        3.  Mostrar tabla posiciones
        4.  Eliminar equipo
        5.  Salir del programa
          """)
    choice = input("Seleccione una opción: ")
    if (choice == "1"):
        equipo = input("Ingrese el nombre del equipo:    ").title()
        if (equipo in torneo):
            print("El equipo ya forma parte del torneo \n")
        else:
            torneo[equipo]=0
        #inicializamos los equipos con puntaje cero
    elif (choice == "2"):
        equipoLocal = input("Ingrese el equipo local:   ").strip().title()
        equipoVisitante = input("Ingrese el equipo visitante:   ").strip().title()

        if (equipoLocal in torneo) and (equipoVisitante in torneo):
            while True:
                marcador= input("Ingrese el marcador (ejemplo: 4 - 2):   ")
         
                if "-" in marcador:
                    goles = marcador.split("-")
                    gol_l= (goles[0]).strip()
                    gol_v= (goles[1]).strip()

                    if gol_l.isdigit() and gol_v.isdigit():
                        gol_l= int(gol_l)
                        gol_v= int(gol_v)
                        puntajeLocal = calcular_puntaje(gol_l,gol_v)
                        torneo[equipoLocal] += puntajeLocal
                        puntajeVisitante = calcular_puntaje(gol_v,gol_l)
                        torneo[equipoVisitante] += puntajeVisitante
                        print("Datos guardados con éxito")
                        break
                    else:
                        print("Error. Marcador inválido. Debes ingresar solo números \n")
                else:
                    print("Error. Marcador inválido. Debes usar un guión entre los puntajes (ej: 4 - 1):  \n")
        else:
            print("Uno de los equipos ingresados no existe, no esta registrado en el torneo. \n Seleccione la opción 1 y agregue el equipo")
    elif (choice == "3"):
        print("\n Lista de equipos ordenados según cantidad de puntos")
        torneo_ordenado = sorted(torneo.items(), key=lambda item:item[1], reverse= True)
        for equipo, puntos in torneo_ordenado:
            print(f"Equipo: {equipo} | Puntos: {puntos}")
    elif (choice == "4"):
        equipo_eliminado = input("Ingrese el nombre del equipo que quiere eliminar:  ").title()
        if (equipo_eliminado in torneo):
            del torneo[equipo_eliminado]
            print (f"\n El equipo {equipo_eliminado} ha sido eliminado del torneo")
        else:
            print(f"\n El equipo {equipo_eliminado} no se ha encontrado registrado en el torneo. No se ha podido eliminar")
    elif (choice == "5"):
        break
    else:
        print("Opción inválida, intente de nuevo:   ")