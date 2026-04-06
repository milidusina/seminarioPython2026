def duracion_playlist (playlist):
    minTotal = 0
    segTotal = 0
    for dicci in playlist:
        duracion_cancion = dicci["duration"].split(":")
        min= int(duracion_cancion[0])
        seg = int(duracion_cancion[1])
        minTotal += min
        segTotal += seg
    segundos= segTotal % 60
    minutos = (segTotal // 60) + minTotal
    duracionTotal = (f"{minutos}m {segundos:02d}s")
    return duracionTotal



def shorter_song (playlist):
    #las duraciones estan en segundos para simplificar
    minimo = 99999
    for dicci in playlist:
        duracion_cancion = dicci["duration"].split(":")
        #duracion = int(duracion_cancion[1]) + ((int(duracion_cancion[0]))*60)
        s = int(duracion_cancion[1])
        m = int(duracion_cancion[0])
        duracion = s + ( m * 60)
        if (duracion < minimo):
            cancion_min = dicci["title"]
            minimo = duracion
    minu = minimo // 60
    seg = minimo % 60
    minutos_segundos = f"({minu}:{seg:02d})"
    cancion = [cancion_min, minutos_segundos]
    return cancion

def longer_song (playlist):
    maximo = 0
    for dicci in playlist:
        duracion_cancion = dicci["duration"].split(":")
        #duracion = int(duracion_cancion[1]) + (int(duracion_cancion[0])*60)
        s = int(duracion_cancion[1])
        m = int(duracion_cancion[0])
        duracion = s + ( m * 60)
        if (duracion > maximo):
            cancion_max = dicci["title"]
            maximo = duracion
    minu = maximo // 60
    seg = maximo % 60
    minutos_segundos = f"({minu}:{seg:02d})"
    cancion = [cancion_max, minutos_segundos]
    return cancion