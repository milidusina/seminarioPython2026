# tenemos q poner la solucion en un codigo 
# dentro de una funcion, asi podemos
# llamarla desde jupyter y ejecutarla
# las funciones de cada ejer conviene hacerlas
# en archivos independientes

#el notebook nos permite ejecutar la solucion

def cifrado_cesar (texto, desplazamiento):
    resultado = ""
    for char in texto:
        if char.isalpha():
                if (char.isupper()):
                     start = ord('A')
                else: #si es minuscula
                     start = ord('a')
                pos_actual = ord(char) - start     
                #nos devuelve la posicion de la letra, siendo 'a' o 'A' la cero
                
                nueva_pos = (pos_actual + desplazamiento) %26     
                #le sumamos el desplazamiento q nos piden, y %26 por si nos pasamos de la ultima posicion
                #volver a la primera = primer letra (a)

                resultado += chr(nueva_pos + start)
                #ahora q hicimos el desplazamiento le devolvemos su valor para usar el codigo ascii
        else:
             resultado += char
    return resultado
