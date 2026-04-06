def validar_alumno (alumno):
    nombre = alumno["name"]
    nota = alumno["grade"]
    estado = alumno["status"]
    
    if (nombre == None) or (nombre.strip() == ""):
        return None
    if (nota == None) or (nota == "") or (str(nota).isdigit() == False):
        return None
    
    nombre_nuevo = nombre.strip().title()
    nota_nueva = int(nota)
    estado_nuevo = estado.strip().title()
    return {"name": nombre_nuevo, "grade": nota_nueva, "status": estado_nuevo}

def imprimir_alumnos (listaA):
    print("Registros limpios de alumnos:  ")
    print(f"{'Nombre':<20}{'Nota':<10}{'Estado':<15}")
    print("-" * 45)
    for alumno in listaA:
        print(f"{alumno['name']:<20} {alumno['grade']:<10} {alumno['status']:<15}")
    print("-" * 45)
    print(f"Total de alumnos válidos: {len(listaA)}")