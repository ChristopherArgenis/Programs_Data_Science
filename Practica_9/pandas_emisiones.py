import pandas as pd

# Leer archivos CSV
print("Generar un DataFrame con los datos de los cuatro archivos.")
archivos = ['Practica_9/emisiones-2016.csv', 'Practica_9/emisiones-2017.csv', 'Practica_9/emisiones-2018.csv', 'Practica_9/emisiones-2019.csv']
df = pd.concat([pd.read_csv(archivo, sep=';') for archivo in archivos], ignore_index=True)
print(df)

# Filtrar columnas relevantes
print("Filtrar las columnas del DataFrame para quedarse con las columnas ESTACION, MAGNITUD, AÑO, MES y las correspondientes a los días D01, D02, etc.")
columnas_dias = [col for col in df.columns if col.startswith('D')]
columnas = ['ESTACION', 'MAGNITUD', 'ANO', 'MES'] + columnas_dias
df = df[columnas]
print(df)

# Reestructurar el DataFrame
print("Reestructurar el DataFrame para que los valores de los contaminantes de las columnas de los días aparezcan en una única columna.")
df = df.melt(id_vars=['ESTACION', 'MAGNITUD', 'ANO', 'MES'], var_name='DIA', value_name='VALOR')
df['DIA'] = df['DIA'].str.extract('D(\d+)').astype(int)
print(df)

# Añadir una columna de Fecha
print("Añadir una columna con la fecha a partir de la concatenación del año, el mes y el día.")
df['FECHA'] = pd.to_datetime(
    df[['ANO', 'MES', 'DIA']].rename(columns={'ANO': 'year', 'MES': 'month', 'DIA': 'day'}),
    errors='coerce'
)
print(df[['ANO', 'MES', 'DIA', 'FECHA']])

# Eliminar fechas no válidas y ordenar
print("Eliminar las filas con fechas no válidas (utilizar la función isnat del módulo numpy) y ordenar el DataFrame por estaciones contaminantes y fecha.")
df = df[~pd.isna(df['FECHA'])]
df = df.sort_values(by=['ESTACION', 'MAGNITUD', 'FECHA'])
print(df)

# Estaciones y contaminantes disponibles
print("Mostrar por pantalla las estaciones y los contaminantes disponibles en el DataFrame.")
print("Estaciones:", df['ESTACION'].unique())
print("Contaminantes:", df['MAGNITUD'].unique())

# Función: emisiones por estación, contaminante y fechas
print("Crear una función que reciba una estación, un contaminante y un rango de fechas y devuelva una serie con las emisiones del contaminante dado en la estación y rango de fechas dado.")
def emisiones_estacion_contaminante_fecha(estacion, contaminante, fecha_inicio, fecha_fin):
    filtro = (
        (df['ESTACION'] == estacion) &
        (df['MAGNITUD'] == contaminante) &
        (df['FECHA'] >= fecha_inicio) &
        (df['FECHA'] <= fecha_fin)
    )

    datos_filtrados = df.loc[filtro, ['FECHA', 'VALOR']].dropna()

    if datos_filtrados.empty:
        print("No se encontraron datos para los parámetros especificados.")
        return pd.Series(dtype='float64')

    return datos_filtrados.set_index('FECHA')['VALOR']

print(emisiones_estacion_contaminante_fecha(4, 1, '2018-01-01', '2018-01-10'))

# Resumen descriptivo por contaminante
print("Mostrar un resumen descriptivo (mínimo, máximo, media, etc.) para cada contaminante.")
print(df.groupby('MAGNITUD')['VALOR'].describe())

# Función: resumen descriptivo por estación y contaminante
print("Crear una función que reciba una estación y un contaminante y devuelva un resumen descriptivo de las emisiones del contaminante indicado en la estación indicada.")
def resumen_estacion_contaminante(estacion, contaminante):
    filtro = (df['ESTACION'] == estacion) & (df['MAGNITUD'] == contaminante)
    return df.loc[filtro, 'VALOR'].describe()

print(resumen_estacion_contaminante(4, 1))

# Función: Emisiones medias mensuales por contaminante y año
print("Crear una función que devuelva las emisiones medias mensuales de un contaminante y un año dados para todas las estaciones.")
def emisiones_mensuales(contaminante, año):
    filtro = (df['MAGNITUD'] == contaminante) & (df['ANO'] == año)
    return df.loc[filtro].groupby(['ESTACION', 'MES'])['VALOR'].mean().unstack()

print(emisiones_mensuales(1, 2019))

# Funcion: Medias mensuales de los distintos tipos de contaminantes
print("Crear un función que reciba una estación de medición y devuelva un DataFrame con las medias mensuales de los distintos tipos de contaminantes.")
def medias_mensuales_estacion(estacion):
    df_filtrado = df[df['ESTACION'] == estacion].copy()
    df_filtrado['VALOR'] = pd.to_numeric(df_filtrado['VALOR'], errors='coerce')
    df_filtrado = df_filtrado.dropna(subset=['VALOR'])
    return df_filtrado.groupby(['MAGNITUD', 'MES'])['VALOR'].mean().unstack()

print(medias_mensuales_estacion(4))