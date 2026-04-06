def calcular_puntos (puntos):
    return sum(puntos.values())

def imprimir_ronda (diccionario,ganador):
    posiciones = dict(sorted(diccionario.items(), key = lambda item: item[1], reverse=True))
    for jugador in posiciones:
        if (jugador==ganador[0]):
            continue
        print(f"      {jugador} ({diccionario[jugador]} pts)" )
    print()

def imprimir_tabla (nombres, puntos,victorias,mejor_ronda, promedios):
    print("Tabla de posiciones final:")
    print(f"{'Cocinero':<15}{'Puntaje':<15}{'Rondas ganadas':<20}{'Mejor ronda':<15}{'Promedio':<15}")
    print("-"*80)

    nombres_ordenados = sorted(nombres, key= lambda p:puntos[p], reverse=True )

    for jugador in nombres_ordenados:
        print(f"{jugador:<15}{puntos[jugador]:<15}{victorias[jugador]:<20}{mejor_ronda[jugador]:<15}{promedios[jugador]:<15}")

    print("-"*80)