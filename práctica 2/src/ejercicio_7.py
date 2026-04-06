import random

def amigo_invisible (lista_personas):
    nombres = [n.title().strip() for n in lista_personas.split(",")]
    while True:
        valido = True
        personas = nombres.copy()
        dicci = dict.fromkeys(nombres)
        
        for i in dicci:    
            if (len(personas) == 0) & (personas[0] == i):
                valido = False
                break

            elegido = random.choice(personas)
            while (elegido == i):
                elegido = random.choice(personas)
            dicci[i] = elegido
            personas.remove(elegido)
        
        if valido:
            return dicci
    
