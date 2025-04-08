# Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y su frecuencia. 
# Escribir otra función que reciba el diccionario generado con la función anterior y devuelva una tupla con la palabra más repetida y su frecuencia.

# Libreria para la verificacion de la puntuacion de signos.
import string

def contar_frecuencia_palabras(cadena):
    # 1. Cadena a minúsculas para un conteo uniforme.
    cadena = cadena.lower()

    # 2. Eliminar signos de puntuación.
    cadena = cadena.translate(str.maketrans('', '', string.punctuation))

    # 3. Dividir la cadena en palabras usando los espacios como delimitadores.
    palabras = cadena.split()

    # 4. Crear un diccionario para almacenar la frecuencia de cada palabra.
    frecuencia = {}

    # 5. Iterar sobre las palabras y actualizar su frecuencia en el diccionario.
    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1

    # 6. Devolver el diccionario de frecuencias.
    return frecuencia

def encontrar_palabra_mas_frecuente(diccionario_frecuencias):
    # 1. Inicializar variables para almacenar la palabra más frecuente y su frecuencia.
    palabra_mas_frecuente = None
    max_frecuencia = 0

    # 2. Iterar sobre los ítems (clave-valor) del diccionario.
    for palabra, frecuencia in diccionario_frecuencias.items():
        # 3. Comparar la frecuencia actual con la frecuencia máxima encontrada hasta ahora.
        if frecuencia > max_frecuencia:
            max_frecuencia = frecuencia
            palabra_mas_frecuente = palabra

    # 4. Devolver la palabra más frecuente y su frecuencia en una tupla.
    return (palabra_mas_frecuente, max_frecuencia)

# Ejemplo de uso:
texto = "Este es un ejemplo de texto. Este texto tiene varias palabras repetidas, como este y texto."
frecuencias = contar_frecuencia_palabras(texto)
print("Frecuencia de cada palabra:", frecuencias)

palabra_mas_comun, frecuencia_maxima = encontrar_palabra_mas_frecuente(frecuencias)
print("\nPalabra más repetida:", palabra_mas_comun)
print("Frecuencia:", frecuencia_maxima)