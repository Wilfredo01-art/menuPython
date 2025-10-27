# Listas
# Funciones
# Excepciones

# Creando un Menu para tareas
tareas = []

# Contador incremental para asignar Ids
nextId = 1

# Creamos una función para mostrar el menú.
def menu():
    print("TASKLIST")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Marcar tarea como realizada")
    print("4. Eliminar tarea")
    print("5. Salir")

# Creamos una función para mostrar las tareas.
def listar():
    if not tareas: # Si no hay tareas no muestra nada
        print("No hay tareas")
        return
    print("\n|  ID  |  ESTADO  |  TITULO  |")
    for t in tareas: # S
        estado = "OK" if t[2] else "NOT"
        print(f"|  {t[0]:<3} |    {estado}   |   {t[1]}   |")

# Creamos una función para agregar las tareas.
def agregar():
    global nextId
    # Pedimos titulo y le quitamos espacios
    titulo = input("Titulo: ".strip())
    if not titulo:
        print("Titulo vacio")
        return
    # Agregamos al arreglo de tareas un Id, el titulo y estado
    tareas.append([nextId, titulo, False])
    nextId += 1
    print("Tarea agregada")

# Creamos una función para marcar como realizada una tarea.
def marcarTarea():
    if not tareas: # Si no hay tareas no se puede marcar como realizada ninguna
        print("No hay tareas")
        return   
    # Se pide el Id de la tarea que se desea marcar como completada, ej: Id 1 | Id 2
    try:
        tid = int(input("Id de la tarea a marcar como realizada").strip())
    except ValueError:
        print("Id invalido. Digite valores númericos")
    # Examina cual coincide con el Id dado por el usuario
    for t in tareas:
        if t[0] == tid:
            t[2] ==  True # Si alguna coincide lo marca como verdadero
            print("Tarea realizada.")
            return
    # De lo contrario si no coincide no se puede realizar
    print("No existe el Id")

# Creamos una función para eliminar las tareas que no necesitemos  
def eliminar():
    if not tareas: # Si no hay tareas no se puede eliminar ninguna
        print("No hay tareas")
        return
    # Se pide el Id de la tarea que se desea eliminar, ej: Id 1 | Id 2
    try:
        tid = int(input("Id de la tarea que desea eliminar").strip())
    except ValueError:
        print("Id invalido. Digite valores númericos.")
        return
    for i, t in enumerate(tareas): # Examina las tareas que esten guardadas
        if t[0] == tid:
            del tareas[i] # Si coincide el Id a eliminar con una tarea se elimina
            print("Tarea Eliminada")
            return
    # De lo contrario no puede eliminar
    print("No existe ese Id a eliminar")

# Hacemos un bucle para repetir nuestro menú hasta que decidamos salir 
while True:
    # Llamamos la función de Menú
    menu()
    # Pedimos que se digite la opción
    op = input("Digite la opción: ").strip()
    # Usamos condicionales para ejecutar
    if op == "1":
        agregar()
    elif op == "2":
        listar()
    elif op == "3":
        marcarTarea()
    elif op == "4":
        eliminar()
    elif op == "5":
        print("Hasta la proxima")
        break
    else:
        print("")