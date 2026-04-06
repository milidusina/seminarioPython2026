import textwrap

def sacar_spoiler (review):
    entrada = input("Ingrese las palabras spoiler (separadas por coma):").split(",")
    entrada_spoiler = [s.strip().lower() for s in entrada]
    palabras = [p.strip() for p in review.split()]

    lista_resultado= []
    for palabra in palabras:
        if palabra.strip(",.").lower() in entrada_spoiler:
            lista_resultado.append("*" * len(palabra))
        else:
            lista_resultado.append(palabra)
    resultado = " ".join(lista_resultado)
    res = textwrap.fill(resultado, width = 70)
    return res

