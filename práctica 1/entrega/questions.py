import random
import string
words = [
    "python",
    "programa",
    "variable",
    "funcion",
    "bucle",
    "cadena",
    "entero",
    "lista",
    "kotlin",
    "java",
]
categorias = {"Tipos de datos ":["entero","cadena","lista"],
              "Lenguajes": ["python","kotlin","java"],
              "Conceptos basicos": ["programa","variable","bucle","funcion"],
              }
guessed = []
attempts = 6
letras_admitidas = string.ascii_lowercase
puntaje = 0

#inicio del juego
print("¡Bienvenido al Ahorcado!")
print("Las categorias a elegir son:   ")
for i in categorias.keys():
    print(i)
print()

while True:
    mi_categ=input("Ingrese su categoria:  ")
    if (mi_categ in categorias):
        word = random.choice(categorias[mi_categ])
        break
    else:
        print("La categoria seleccionada no existe. Intente de nuevo:")

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
        puntaje += 6
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
        puntaje -= 1
        print("Esa letra no está en la palabra.")
    print()
else:
    puntaje = 0
    print(f"¡Perdiste! La palabra era: {word}")
print(f"El puntaje obtenido es de: {puntaje}")