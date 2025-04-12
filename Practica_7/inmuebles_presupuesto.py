# 1. Inicializacion de Variables.
lista_inmueble = [{'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
{'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'},
{'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},
{'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'},
{'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}]

# 2. Formulas a Aplicar.

# Formula para obtener precios dependiendo la Zona
# Zona A: precio = (metros * 1000 + habitaciones * 5000 + garaje * 15000) * (1-antiguedad/100)
# Zona B: precio = (metros * 1000 + habitaciones * 5000 + garaje * 15000) * (1-antiguedad/100) * 1.5

# 3. Funciones.
def precio_inmueble(lista_inmueble):
  for i in lista_inmueble:
    antiguedad = 2025 - i["año"]
    precio = (i["metros"] * 1000 + i["habitaciones"] * 5000 + int(i["garaje"]) * 15000) * (1-antiguedad/100)
    if i["zona"] == "A":
      i["precio"] = precio
    else:
      i["precio"] = precio * 1.5
  return lista_inmueble

def presupuestar(lista_inmueble, presupuesto):
  lista_filtrada = []
  for i in lista_inmueble:
    if i["precio"] <= presupuesto:
      lista_filtrada.append(i)
  return lista_filtrada

def interfaz(lista_inmueble):
  presupuesto = int(input("Digame el Presupuesto que tiene para el piso: "))
  list_with_price = precio_inmueble(lista_inmueble)
  opciones = presupuestar(list_with_price, presupuesto)
  if opciones == []:
    print("No hay opciones disponibles")
  else:
    print(f"Las opciones disponibles son: {len(opciones)}")
    for i in opciones:
      print(i)

# 4. Ejecucion Final.
interfaz(lista_inmueble)