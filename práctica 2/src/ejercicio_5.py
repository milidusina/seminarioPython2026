def calcular_costo (zona, peso):
    zonas_validas = ["local", "regional", "nacional"]

    if (zona.lower() in zonas_validas):
        match zona.lower():
            case "local":
                if (peso <= 1.0):
                    return 500
                elif(peso > 1.0) and (peso < 5.0):
                    return 1000
                else:
                    return 2000
            case "regional":
                if (peso < 1.0):
                    return 1000
                elif(peso > 1.0) and (peso < 5.0):
                    return 2500
                else:
                    return 4500
            case "nacional":
                if (peso < 1.0):
                    return 2000
                elif(peso > 1.0) and (peso < 5.0):
                    return 5000
                else:
                    return 8000
    else:
        print("Zona no válida. Las zonas disponibles son: local, regional, nacional.")
    