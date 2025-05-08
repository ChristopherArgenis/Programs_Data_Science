import numpy as np

# Arreglo para manejar los tipos de datos para las columnas.
dtype_definido = np.dtype([
    ('age', int),
    ('sex', 'U10'),  # Suponemos cadenas de hasta 10 caracteres para el sexo
    ('bmi', float),
    ('children', int),
    ('smoker', 'U3'),  # 'yes' o 'no'
    ('region', 'U10'), # Suponemos cadenas de hasta 10 caracteres para la región
    ('charges', float)
])

# Se agarra un Dataset de Kaggle.
# Conviriendo en un arreglo de Numpy el Dataset: Medical Cost Personal Datasets.
dataset = np.genfromtxt('Practica_8/insurance.csv', delimiter=',', skip_header=1, dtype=dtype_definido)

# Informacion General
print("Filas Totales del Arreglo:", dataset.shape[0])
print("Lista de Tipos de datos:", dataset.dtype)

# Extraer las columnas.
ages = dataset['age'] # Int
sexes = dataset['sex'] # String
bmis = dataset['bmi'] # Float
children = dataset['children'] # Int
smokers = dataset['smoker'] # String
regions = dataset['region'] # String
charges = dataset['charges'] # Float

# Operaciones
