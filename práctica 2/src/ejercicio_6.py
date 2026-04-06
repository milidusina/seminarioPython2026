def conta_hashtags (texto):
    dicci_hashtags = {}
    for frase in texto:
        linea = frase.split()
        for palabra in linea:
            if (palabra.startswith("#")):
                if (palabra not in dicci_hashtags):
                    dicci_hashtags[palabra]= 1
                else:
                    contador = dicci_hashtags[palabra] + 1
                    dicci_hashtags[palabra] = contador
    return dicci_hashtags