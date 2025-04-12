# 1. Escriba un programa Python, donde declare un diccionario para guardar los nombres y precios de las distintas frutas (al menos 5).
# El programa pedirá el nombre de la fruta y la cantidad que el cliente desea comprar y nos mostrará el precio final del pedido a partir de los datos guardados en el diccionario.  
# Si la fruta no existe nos dará un error.
# Tras cada consulta el programa nos preguntará si queremos hacer otra consulta

# 1. Declaracion de Funciones.
def calculate_total_price(inventario, fruta):
  cantidad = int(input("¿Cuantas quiere comprar? "))
  precio_total = inventario[fruta] * cantidad
  print(f"El precio total de {cantidad} {fruta}(s) es {precio_total}")
  return precio_total

def Entrada(inventario):
  print("Bienvenido a la tienda de frutas")
  print("Estos son los productos disponibles:")
  for fruta, precio in inventario.items():
    print(f"{fruta}: ${precio}")

def ciclo(inventario):
  precio_final = 0
  while True:
    fruta = input("¿Cual es la fruta que quiere comprar? ")
    if fruta in inventario:
      precio_parcial = calculate_total_price(inventario, fruta)
      precio_final += precio_parcial
      salida = input("Seria todo?: (Si/No)")
      if salida == "Si":
        break
    else:
      print("La fruta no esta disponible")
  return precio_final

def app():
  inventario = { "manzana": 2.5, "banana": 1.0, "naranja": 1.5, "uva": 3.0, "pera": 2.0 }
  Entrada(inventario)
  precio_mandado = ciclo(inventario)
  print(f"El precio total de la compra es {precio_mandado}")
  print("Gracias por su Compra.")

# 2. Ejecucion de la Funcion Principal -> app().
app()