#  Escriba un programa Python utilizando funciones, que genere una lista de n número aleatorios (en cualquier rango) y que cree un diccionario cuyas claves sean desde el número 1 hasta el número indicado (n), y los valores sean los cuadrados de los números aleatorios generados.
# Al final imprima el contenido de la lista de aleatorios y los valores del diccionario.

# 1. Importar la bilbioteca necesaria.
import random

# 2. Declaracion de Funciones.
def generador(n, limit):
  list_random = []
  diccionario = {}
  for i in range(1, n+1):
    num_random = random.randint(1, limit)
    list_random.append(num_random)
    diccionario[num_random] = num_random**2
  return diccionario

def Eleccion():
  n = int(input("Cuanto numeros aleatorio seran?: "))
  limit = int(input("Hasta que rango seran los numeros?: "))
  print("\nDiccionario de Numeros Aleatorio con sus cuadrados.")
  return generador(n, limit)

# 3. Ejecucion de Funcion Principal -> Eleccion()
Eleccion()