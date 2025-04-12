# El directorio de los clientes de una empresa

# 1. Inicializar Variables.
dicc = {}
text = "nif;nombre;email;teléfono;descuento\n01234567L;Luis;González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena;Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José;Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen;Sánchez;carmen@mail.com;667677855;15.7"

# 2. Declaracion de Funciones.
def process_text(text):
  list_clientes = text.split("\n")
  colum_rows_list = []
  for i in list_clientes:
    colum_rows_list.append(i.split(";"))
  return colum_rows_list

def create_db(list_iter, columns):
  dicc = {list_iter[0]: {columns[1]: list_iter[1], columns[2]: list_iter[2], columns[3]: list_iter[3], columns[4]: list_iter[4]}}
  return dicc

def update_dicc(dicc, list_clean):
  for i in range(1, 5):
    dicc.update(create_db(list_clean[i], list_clean[0]))
  return dicc

# 3. Ejecucion de Funciones.
list_clean = process_text(text)
update_dicc(dicc, list_clean)
print(dicc)