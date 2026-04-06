import this

def cant_lineas (texto):
    lineas= texto.splitlines()
    cant_lin = len(lineas)
    return cant_lin

def cant_palabras (texto):
    palabras= texto.split();
    cant_pal= len(palabras)
    return cant_pal

def promedio_palabras (texto):
    promedio= cant_palabras(texto) / cant_lineas(texto);
    return promedio

def lineas_mayor_prom (texto):
    nueva_lista = []
    promedio = promedio_palabras(texto)
    lineas = texto.splitlines()
    for lin in lineas:
        cant_palabra= len(lin.split())
        if cant_palabra > promedio:
            nueva_lista.append(lin)
    return nueva_lista
