import numpy as np

# Clase Calculador
class Calculador:
    def __init__(self, array):
        self.categorias = {
            "Bajo Peso": [],
            "Saludable": [],
            "Sobrepeso": [],
            "Obesidad": [],
            "Obesidad Grave": []
        }
        self.etapas = {
            "Adultez Joven": [],
            "Edad Media": [],
            "Adultez Tardia": []
        }
        self.prima_s = {
            "Baja": [],
            "Medio": [],
            "Alto": []
        }
        self.bmis_keys = self.categorias.keys()
        self.ages_keys = self.etapas.keys()
        self.charges_keys = self.prima_s.keys()
        self.array = array

    def categorizar(self, column):
        if column == "ibm":
            for bmi in self.array:
                match bmi:
                    case bmi if bmi < 18.5:
                        self.categorias["Bajo Peso"].append(bmi)
                    case bmi if bmi >= 18.5 and bmi <= 24.9:
                        self.categorias["Saludable"].append(bmi)
                    case bmi if bmi >= 25 and bmi <= 29.9:
                        self.categorias["Sobrepeso"].append(bmi)
                    case bmi if bmi >= 30 and bmi <= 39.9:
                        self.categorias["Obesidad"].append(bmi)
                    case bmi if bmi > 40:
                        self.categorias["Obesidad Grave"].append(bmi)
            return self.categorias
        elif column == "age":
            for age in self.array:
                match age:
                    case age if age >= 18 and age <= 39:
                        self.etapas["Adultez Joven"].append(age)
                    case age if age >= 40 and age <= 59:
                        self.etapas["Edad Media"].append(age)
                    case age if age >= 60:
                        self.etapas["Adultez Tardia"].append(age)
            return self.etapas
        elif column == "charge":
            for charge in self.array:
                match charge:
                    case charge if charge >= 1_000 and charge <= 14_999:
                        self.prima_s["Baja"].append(charge)
                    case charge if charge >= 15_000 and charge <= 39_999:
                        self.prima_s["Medio"].append(charge)
                    case charge if charge >= 40_000:
                        self.prima_s["Alto"].append(charge)
            return self.prima_s

    def np_array(self, dicc, column):
        if column == "ibm":
            for clave in self.bmis_keys:
                dicc[clave] = np.array(self.categorias[clave])
        elif column == "age":
            for clave in self.ages_keys:
                dicc[clave] = np.array(self.etapas[clave])
        elif column == "charge":
            for clave in self.charges_keys:
                dicc[clave] = np.array(self.prima_s[clave])
        return dicc
    
    def print_est(self, arrays, clave):
        print("-"*25)
        print(f"Categoria: {clave}")
        print(f"Media: ", round(arrays[clave].mean(), 2))
        print(f"Varianza: ", round(arrays[clave].var(), 2))
        print(f"Desviacion Estandar: ", round(arrays[clave].std(), 2))
        print(f"Maximo Valor: {arrays[clave].max()}, Minimo Valor: {arrays[clave].min()}")

    def estadisticas(self, arrays, column):
        if column == "ibm":
            for clave in self.bmis_keys:
                self.print_est(arrays, clave)
        elif column == "age":
            for clave in self.ages_keys:
                self.print_est(arrays, clave)
        elif column == "charge":
            for clave in self.charges_keys:
                self.print_est(arrays, clave)

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
# Convirtiendo  en un arreglo de Numpy el Dataset: Medical Cost Personal Datasets.
dataset = np.genfromtxt('Practica_8/insurance.csv', delimiter=',', skip_header=1, dtype=dtype_definido)

# Extraer las columnas.
ages = dataset['age'] # Int
sexes = dataset['sex'] # String
bmis = dataset['bmi'] # Float
children = dataset['children'] # Int
smokers = dataset['smoker'] # String
regions = dataset['region'] # String
charges = dataset['charges'] # Float

def present_general(dataset, generos, smokers, regions):
    """Esto imprime una Presentacion formal de informacion"""
    print("Informacion Poblacional")
    print("Cantidad de Filas del Arreglo:", dataset.shape[0])
    print(f"Cantidad de: Hombres = {generos[1]}, Mujeres = {generos[0]}")
    print(f"Cuantos Fuman?: Si = {smokers[1]}, No = {smokers[0]}")
    print(f"Regiones de los Pacientes: {regions[0], regions[1], regions[2], regions[3]}")

def info_general(columns_num, str_columns, cant_child, cuan_child):
    """Muestra informacion General iterable por varias cantidades de valores"""
    for column, title in zip(columns_num, str_columns):
        print(f"Promedio de {title}:", round(column.mean(), 2))
    print()
    for cant, cuan, in zip(cant_child, cuan_child):
        print(f"Son {cant} personas con {cuan} niño(s)")

def menu() -> int:
    """ Imprime un menu se eleccion y regresa la opcion obtenida"""
    print("Opciones a Elegir:")
    print("1. Informacion General del Dataset")
    print("2. Estadisticos de IBM")
    print("3. Estadisticos de Edad")
    print("4. Estadisticos de Poliza")
    print("5. Salir")
    opcion = int(input("Cual opcion desea seleccionar?: "))
    return opcion

def main():
    """Sistema Principal que:
    Primero declara las variables, usa la clase Calculador y opera lo necesario
    Pasando a un bucle para entrar en que mostrar al usuario"""
    # Informacion General
    columns_num = [ages, bmis, charges] # Columnas Numericas
    str_columns = ["Edad", "BMI", "Prima del seguro ($)"] # Encabezado numerico

    # Sexes
    null, generos = np.unique(sexes, return_counts=True)

    # BMI
    ibm = Calculador(bmis)
    ibmsCategorias = ibm.categorizar("ibm")
    ibm_categorias_np = ibm.np_array(ibmsCategorias, "ibm")

    # Age
    age = Calculador(ages)
    agesCategorias = age.categorizar("age")
    age_categorias_np = age.np_array(agesCategorias, "age")

    # Charges
    charge = Calculador(charges)
    chargesCategorias = charge.categorizar("charge")
    charge_categorias_np = charge.np_array(chargesCategorias, "charge")

    # Children
    cuan_child, cant_child = np.unique(children, return_counts=True)

    # Smokers
    cuan_smokers, cant_smokers = np.unique(smokers, return_counts=True)

    # Regions
    cuan_regions, cant_regions = np.unique(regions, return_counts=True)

    while True:
        print()
        match menu():
            case 1:
                # Informacion General del Dataset.
                present_general(dataset, generos, cant_smokers, cuan_regions)
                info_general(columns_num, str_columns, cant_child, cuan_child)
            case 2:
                # Estadisticas del BMI.
                ibm.estadisticas(ibm_categorias_np, "ibm")
            case 3:
                age.estadisticas(age_categorias_np, "age")
            case 4:
                charge.estadisticas(charge_categorias_np, "charge")
            case 5:
                break
            case _:
                print("Eleccion Incorrecta.")
main()