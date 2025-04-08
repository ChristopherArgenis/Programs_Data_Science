# Escribir un programa que permita gestionar la base de datos de clientes de una empresa.
# Los clientes se guardarán en un diccionario en el que la clave de cada cliente será su NIF,
# y el valor será otro diccionario con los datos del cliente (nombre, dirección, teléfono, correo, preferente), 
# donde preferente tendrá el valor True si se trata de un cliente preferente.

def agregar_cliente(base_de_datos):
    # Al usuario se le pide el NIF del cliente.
    nif = input("Ingrese el NIF del cliente: ")
    # Verificar si el NIF ya esta registrado.
    if nif in base_de_datos:
        # Si ya lo esta, entonces avisar al usuario.
        print("Ya existe un cliente con ese NIF.")
        return
    # En caso de ser un NIF unico y nuevo. ->
    # Se solicitan los siguientes datos.
    nombre = input("Ingrese el nombre del cliente: ")
    direccion = input("Ingrese la dirección del cliente: ")
    telefono = input("Ingrese el teléfono del cliente: ")
    correo = input("Ingrese el correo electrónico del cliente: ")
    # Un ciclo hasta que este resuelto lo siguiente.
    while True:
        # Preguntando al usuario si el clientes es preferente o no.
        preferente_str = input("¿Es cliente preferente? (True/False): ").lower()
        # Verificar si es uno de los siguientes resultados.
        if preferente_str in ['true', 'false']:
            # Usando Comprehensions pára almacenar el booleano.
            preferente = True if preferente_str == 'true' else False
            # Cerrar ciclo.
            break
        else:
            # En caso de no responder correctamente. ->
            # Asi hasta que conteste correctamente.
            print("Por favor, ingrese 'True' o 'False'.")

    # JSON que almacena los datos registrados del cliente.
    cliente = {
        'nombre': nombre,
        'direccion': direccion,
        'telefono': telefono,
        'correo': correo,
        'preferente': preferente
    }

    # Se almacena el json del cliente en la BD.
    base_de_datos[nif] = cliente
    # Mensaje de confirmacion al usuario de que fue registrado exitosamente el cliente.
    print(f"Cliente con NIF {nif} agregado correctamente.")

def eliminar_cliente(base_de_datos):
    # Se pide al usuario el NIF del usuario a querer eliminar.
    nif_eliminar = input("Ingrese el NIF del cliente a eliminar: ")
    # Se verifica si esta en la Base de datos.
    if nif_eliminar in base_de_datos:
        # Se elimina el cliente dado su NIF.
        del base_de_datos[nif_eliminar]
        # Se confirma con un mensaje la eliminacion del cliente.
        print(f"Cliente con NIF {nif_eliminar} eliminado correctamente.")
    # Dado que no esta en la Base de datos, se muesta el siguiente mensaje al usuario.
    else:
        print(f"No se encontró ningún cliente con el NIF {nif_eliminar}.")

def mostrar_cliente(base_de_datos):
    # Se pide al usuario el NIF del usuario a querer mostrar.
    nif_mostrar = input("Ingrese el NIF del cliente a mostrar: ")
    # Se verifica si esta en la Base de datos
    if nif_mostrar in base_de_datos:
        # Se muestra el cliente dado su NIF y se muestran los datos del mismo.
        cliente = base_de_datos[nif_mostrar]
        print(f"\nDatos del cliente con NIF {nif_mostrar}:")
        for clave, valor in cliente.items():
            print(f"{clave.capitalize()}: {valor}")
    # Dado que no esta en la Base de datos, se muesta el siguiente mensaje al usuario.
    else:
        print(f"No se encontró ningún cliente con el NIF {nif_mostrar}.")

def listar_clientes(base_de_datos):
    # Verificar si la Base de datos esta vacia.
    # Para avisar al usuario, por si acaso.
    if not base_de_datos:
        print("La base de datos de clientes está vacía.")
        return
    # Impresion de la lista de clientes siempre que haya al menos uno.
    print("\n--- Lista de todos los clientes ---")
    for nif, cliente in base_de_datos.items():
        print(f"NIF: {nif}")
        for clave, valor in cliente.items():
            print(f"  {clave.capitalize()}: {valor}")
        print("-" * 20)

def listar_clientes_preferentes(base_de_datos):
    # JSON de clientes preferentes usando: Comprehensions
    clientes_preferentes = {nif: cliente for nif, cliente in base_de_datos.items() if cliente['preferente']}
    # Por si no existen los clientes preferentes se da un aviso al usuario.
    if not clientes_preferentes:
        print("No hay clientes preferentes en la base de datos.")
        return
    # Impresion de la lista de clientes preferentes siempre que haya al menos uno.
    print("\n--- Lista de clientes preferentes ---")
    # Uso de for para iterar en cada uno de ellos.
    for nif, cliente in clientes_preferentes.items():
        print(f"NIF: {nif}")
        for clave, valor in cliente.items():
            print(f"  {clave.capitalize()}: {valor}")
        print("-" * 20)

def menu():
    """
    Muestra el menú principal de la aplicación.
    """
    # Opciones de Requerimiento.
    print("\n--- Gestión de Base de Datos de Clientes ---")
    print("1. Añadir cliente")
    print("2. Eliminar cliente")
    print("3. Mostrar cliente")
    print("4. Listar todos los clientes")
    print("5. Listar clientes preferentes")
    print("6. Salir")

def main():
    """
    Función principal que ejecuta el programa.
    """
    # Base de Datos JSON.
    base_de_datos_clientes = {}

    # Ciclo para la Aplicacion en Consola.
    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregar_cliente(base_de_datos_clientes)
        elif opcion == '2':
            eliminar_cliente(base_de_datos_clientes)
        elif opcion == '3':
            mostrar_cliente(base_de_datos_clientes)
        elif opcion == '4':
            listar_clientes(base_de_datos_clientes)
        elif opcion == '5':
            listar_clientes_preferentes(base_de_datos_clientes)
        elif opcion == '6':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()