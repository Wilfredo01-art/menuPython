# Listas
# Funciones
# Excepciones

# Menu
tareas = []

# Contador incremental para asignar Ids
nextId = 1

def menu():
    print("TASKLIST")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Marcar tarea como realizada")
    print("4. Eliminar tarea")
    print("5. Salir")

def listar():
    if not tareas:
        print("No hay tareas")
        return
    
    print("\n|  ID  |  ESTADO  |  TITULO  |")
    for t in tareas:
        estado = "OK" if t[2] else "NOT"
        print(f"|  {t[0]:<3} |    {estado}   |   {t[1]}   |")

def agregar():
    global nextId
    
    titulo = input("Titulo: ".strip())
    if not titulo:
        print("Titulo vacio")
        return
    tareas.append([nextId, titulo, False])
    nextId += 1
    print("Tarea agregada")
    
def marcarTarea():
    if not tareas:
        print("No hay tareas")
        return   
    try:
        tid = int(input("Id de la tarea a marcar como realizada").strip())
    except ValueError:
        print("Id invalido. Digite valores númericos")
        
    for t in tareas:
        if t[0] == tid:
            t[2] = True
            print("Tarea realizada.")
            return
    print("No existe el Id")
    
def eliminar():
    if not tareas:
        print("No hay tareas")
        return 
    try:
        tid = int(input("Id de la tarea que desea eliminar").strip())
    except ValueError:
        print("Id invalido. Digite valores númericos.")
        return
    for i, t in enumerate(tareas):
        if t[0] == tid:
            del tareas[i]
            print("Tarea Eliminada")
            return
    print("No existe ese Id a eliminar")
    
while True:
    menu()
    
    op = input("Digite la opción: ").strip()
    
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
    else:
        print("")