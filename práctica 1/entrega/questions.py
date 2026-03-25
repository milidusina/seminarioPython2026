import random
import string

categorias = {"tipos de datos":["entero","cadena","lista"],
              "lenguajes": ["python","kotlin","java"],
              "conceptos basicos": ["programa","variable","bucle","funcion"],
              }
letras_admitidas = string.ascii_lowercase

#inicio del juego
print("¡Bienvenido al Ahorcado!")
print("Las categorias a elegir son:   ")
for i in categorias.keys():
    print(i)

#seleccion de categoria
while True:
    mi_categ=input("\n Ingrese su categoria:  ")
    if (mi_categ in categorias):
        palabras = random.sample(categorias[mi_categ],len(categorias[mi_categ]))
        break
    else:
        print("La categoria seleccionada no existe. Intente de nuevo:")

#cantidad de rondas según la cantidad de palabras de la categoría
for word in palabras:
    attempts = 6
    guessed = []
    while attempts > 0:
    # Mostrar progreso: letras adivinadas y guiones para las que faltan
        progress = ""
        for letter in word:
            if letter in guessed:
                progress += letter + " "
            else:
                progress += "_ "
        print(progress)
        # Verificar si el jugador ya adivinó la palabra completa
        if "_" not in progress:
            print("¡Ganaste!")
            break
        print(f"Intentos restantes: {attempts}")
        print(f"Letras usadas: {', '.join(guessed)}")

        letter = input("Ingresá una letra: ")

        if len(letter)!=1 or (letter not in letras_admitidas):
            print("Entrada no válida")
        elif letter in guessed:
            print("Ya usaste esa letra.")
        elif letter in word:
            guessed.append(letter)
            print("¡Bien! Esa letra está en la palabra.")
        else:
            guessed.append(letter)
            attempts -= 1
            print("Esa letra no está en la palabra.")
        print()
    else:
        print(f"¡Perdiste! La palabra era: {word}")
    print(f"El puntaje obtenido es de: {attempts}")