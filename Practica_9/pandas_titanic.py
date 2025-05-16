import pandas as pd

# Cargar datos
print("Generar un DataFrame con los datos del archivo.")
df = pd.read_csv("Practica_9/titanic.csv")
print(df)

# Dimensiones y estructura del DataFrame
print("Mostrar por pantalla las dimensiones del DataFrame.")
print(df.shape)

print("Mostrar por pantalla el número de datos que contiene.")
print(df.size)

print("Mostrar por pantalla los nombres de sus columnas.")
print(df.columns)

print("Mostrar por pantalla los nombres de sus filas (índices).")
print(df.index)

print("Mostrar por pantalla los tipos de datos de las columnas.")
print(df.dtypes)

print("Mostrar por pantalla las 10 primeras filas.")
print(df.head(10))

print("Mostrar por pantalla las 10 últimas filas.")
print(df.tail(10))

# Pasajero con ID 148
print("Mostrar por pantalla los datos del pasajero con identificador 148.")
print(df.loc[148])

# Filas pares
print("Mostrar por pantalla las filas pares del DataFrame.")
print(df.iloc[::2])

# Nombres de personas en primera clase ordenadas alfabéticamente
print("Mostrar por pantalla los nombres de las personas que iban en primera clase ordenadas alfabéticamente.")
print(df[df['Pclass'] == 1]['Name'].sort_values())

# Porcentaje de sobrevivientes y fallecidos
print("Mostrar por pantalla el porcentaje de personas que sobrevivieron y murieron.")
print(df['Survived'].value_counts(normalize=True) * 100)

# Porcentaje de sobrevivientes por clase
print("Mostrar por pantalla el porcentaje de personas que sobrevivieron en cada clase.")
print(df.groupby('Pclass')['Survived'].mean() * 100)

# Eliminar pasajeros sin edad
print("Eliminar del DataFrame los pasajeros con edad desconocida.")
df = df.dropna(subset=['Age'])
print(df)

# Edad media de mujeres por clase
print("Mostrar por pantalla la edad media de las mujeres que viajaban en cada clase.")
print(df[df['Sex'] == 'female'].groupby('Pclass')['Age'].mean())

# Nueva columna: ¿menor de edad?
print("Añadir una nueva columna booleana para ver si el pasajero era menor de edad o no.")
df['Menor'] = df['Age'] < 18
print(df[['Age', 'Menor']])

# Porcentaje de menores y mayores que sobrevivieron por clase
print("Mostrar por pantalla el porcentaje de menores y mayores de edad que sobrevivieron en cada clase.")
print(df.groupby(['Pclass', 'Menor'])['Survived'].mean() * 100)