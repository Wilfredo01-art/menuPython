# Se pide generar un menú para organizar tareas a tráves de funciones

# Se crea un array para las tareas
tareas = []

# Contador incremental para asingar Ids
nextId = 1

# Creamos el menú
def menu():
    print("\n¡Bienvenido a Listas inteligentes!")
    print("1. Agregar tarea.")
    print("2. Agregar nota a la tarea.")
    print("3. Modificar tarea.")
    print("4. Eliminar tarea.")
    print("5. Mostrar lista de tareas")
    print("6. Marcar tarea como realizada.")
    print("7. Salir\n")
    
# Creamos función para agregar tarea.
def agregarTarea():
    global nextId
    # Pedimos titulo y le quitamos espacios
    tarea = input(f"Ingresa la tarea N°{nextId}:  ".strip())
    if not tarea:
        print("No has registrado la tarea correctamente.")
        return
    # Agregamos al arreglo de tareas un Id, el titulo y estado
    tareas.append([nextId, tarea, False, None])
    nextId += 1
    print("Has agregado la tarea correctamente")
    
# Creamos una función para agregar una nota a la tarea.
def agregarNota():
    if not tareas: # Si no hay tareas no se puede agregar nota a ninguna
        print("No hay tareas")
        return
    # Se pide el Id de la tarea que se desea agregar nota, ej: Id 1 | Id 2
    try:
        idUsuario = int(input("Id de la tarea que desea agregar nota: ").strip())
    except ValueError:
        print("Id invalido. Digite valores númericos.")
        return
    for i, t in enumerate(tareas): # Examina las tareas que esten guardadas
        if t[0] == idUsuario:
            notaUsuario = input("Agrega la nota de la tarea: ")
            t[3] = notaUsuario.strip()
            print("Nota agregada correctamente.")
            return
    # De lo contrario no puede agregar nota
    print("\nNo existe ese Id de tarea.\n")

# Creamos un función para modificar la tarea.
def modificarTarea():
    if not tareas: # Si no hay tareas no se puede modificar ninguna
        print("No hay tareas")
        return
    # Se pide el Id de la tarea que se desea modificar, ej: Id 1 | Id 2
    try:
        idUsuario = int(input("Id de la tarea que desea modificar: ").strip())
    except ValueError:
        print("Id invalido. Digite valores númericos.")
        return
    for i, t in enumerate(tareas): # Examina las tareas que esten guardadas
        if t[0] == idUsuario:
            tarea = input("Ingresa el titulo de la tarea a modificar.")
            t[1] = tarea.strip()
            print("Tarea modificada correctamente.")
            return
    # De lo contrario no puede modificar la tarea
    print("\nNo existe ese Id de tarea.\n")

# Creamos una función para eliminar las tareas que no necesitemos 
def eliminarTarea():
    if not tareas: # Si no hay tareas no se puede eliminar ninguna
        print("No hay tareas")
        return
    # Se pide el Id de la tarea que se desea eliminar, ej: Id 1 | Id 2
    try:
        idUsuario = int(input("Id de la tarea que desea eliminar").strip())
    except ValueError:
        print("Id invalido. Digite valores númericos.")
        return
    for i, t in enumerate(tareas): # Examina las tareas que esten guardadas
        if t[0] == idUsuario:
            del tareas[i] # Si coincide el Id a eliminar con una tarea se elimina
            print("Tarea Eliminada")
            return
    # De lo contrario no puede eliminar
    print("No existe ese Id a eliminar")

# Creamos una función para mostrar la lista de tareas
def listarTareas():
    if not tareas: # Si no hay tareas no muestra nada
        print("No hay tareas")
        return
    print("\n|  ID  |  ESTADO  |  TITULO  |   NOTA   ")
    for t in tareas:
        estado = "OK" if t[2] else "NOT"
        nota = "Sin nota" if t[3] == None else t[3]
        print(f"|  {t[0]:<3} |    {estado}   |   {t[1]}   |   {nota}")

# Creamos una función para marcar como realizada una tarea.
def marcarTarea():
    if not tareas: # Si no hay tareas no se puede marcar como realizada ninguna
        print("No hay tareas")
        return   
    # Se pide el Id de la tarea que se desea marcar como completada, ej: Id 1 | Id 2
    try:
        idUsuario = int(input("Id de la tarea a marcar como realizada").strip())
    except ValueError:
        print("Id invalido. Digite valores númericos")
    # Examina cual coincide con el Id dado por el usuario
    for t in tareas:
        if t[0] == idUsuario:
            t[2] =  True # Si alguna coincide lo marca como verdadero
            print("Tarea realizada.")
            return
    # De lo contrario si no coincide no se puede realizar
    print("No existe el Id")

# Hacemos un bucle para repetir nuestro menú hasta que decidamos salir 
while True:
    # Llamamos la función de Menú
    menu()
    # Pedimos que se digite la opción
    op = input("Digite la opción: ").strip()
    print("")
    # Usamos condicionales para ejecutar
    if op == "1":
        agregarTarea()
    elif op == "2":
        agregarNota()
    elif op == "3":
        modificarTarea()
    elif op == "4":
        eliminarTarea()
    elif op == "5":
        listarTareas()
    elif op == "6":
        marcarTarea()
    elif op == "7":
        print("Hasta la proxima")
        break
    else:
        print("Ingresa un opción correcta")