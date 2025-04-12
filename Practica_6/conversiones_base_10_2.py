# Escribir un programa con funciones que convierta un número decimal en binario y de binario a decimal.
def decimal_a_binario(decimal):
  # Verificadores.
    if not isinstance(decimal, int):
        print("Error: La entrada debe ser un número entero.")
        return None
    if decimal == 0:
        return '0'

    # Inicializacion de varibles para la conversion.
    binario = ''
    # Conversion.
    while decimal > 0:
        residuo = decimal % 2
        binario = str(residuo) + binario  # Anteponer el resto
        decimal //= 2
    return binario

def binario_a_decimal(binario):
  # Verificadores.
    if not isinstance(binario, str):
        print("Error: La entrada debe ser una cadena.")
        return None
    for digito in binario:
        if digito not in '01':
            print("Error: La cadena contiene caracteres no binarios.")
            return None

    # Inicializacion de varibles para la conversion.
    decimal = 0
    potencia = 0
    # Conversion.
    for digito in reversed(binario):
        if digito == '1':
            decimal += 2 ** potencia
        potencia += 1
    return decimal

# Ejemplo de uso:
numero_decimal = 25
binario_equivalente = decimal_a_binario(numero_decimal)
print(f"El número decimal {numero_decimal} en binario es: {binario_equivalente}")

numero_binario = "110101"
decimal_equivalente = binario_a_decimal(numero_binario)
print(f"El número binario {numero_binario} en decimal es: {decimal_equivalente}")

# Ejemplos con casos borde y errores:
print(f"Binario de 0: {decimal_a_binario(0)}")
print(f"Decimal de '0': {binario_a_decimal('0')}")
print(f"Binario de 10.5: {decimal_a_binario(10.5)}")
print(f"Decimal de '102': {binario_a_decimal('102')}")