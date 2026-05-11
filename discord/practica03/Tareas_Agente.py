import datetime 

def procesar_tareas(lista_Tareas,descripcion):
    """
    Agregar una tarea a la lista si cumple con los requisitos.
    """
    if len(descripcion) < 3:
        return "La descripción de la tarea es demasiado corta. Debe tener al menos 3 caracteres."

    # Crear el formato para tarea
    Fecha = datetime.datetime.now().strftime("%H:%M")
    Nueva_Tarea = f"{descripcion} - {Fecha}"
    lista_Tareas.append(Nueva_Tarea)
    return f"Tarea '{descripcion}' agregada a la lista."

def Listar_Tareas(lista_Tareas):
    """
    formatea la lista de tareas para su visualisación.
    """
    if not lista_Tareas:
        return "No hay tareas"
    
    #agregar una variable llamada resultado

    resultado = "Listado de tareas:\n"

    #Iterar la lista de tareas y formatear la salida
    for i, tarea in enumerate(lista_Tareas, start=1):
        resultado += f"{i}. {tarea}\n"
    return resultado 

def Eliminar_Tarea(lista_Tareas, indice):
    """
    Elimina una tarea por su número de índice.
    """
    if not indice.isdigit():
        return "Índice inválido. Por favor, introduce un número."

    indice = int(indice)-1

    #Agregamos la logica para preguntar si el elemento está en la lista

    if 0 <= indice < len(lista_Tareas):
        tarea_eliminada = lista_Tareas.pop(indice)
        return f"Tarea  eliminada: {tarea_eliminada}"

def main():
    tareas = []
    PREFIJO = "!"
    
    print("Bienvenido al gestor de tareas.")
    activa = True
    while activa:
        entrada = input(">>>").strip()

        if not entrada.startswith(PREFIJO):
            print("Error: Comando no reconocido")
            continue

    #procesamiento de la entrada
        cuerpo = entrada[len(PREFIJO):].split(maxsplit=1)
        comando = cuerpo[0].lower()
        argumento = cuerpo[1] if len(cuerpo) > 1 else ""

        #seleccion de accion
        if comando == "add":
            resultado = procesar_tareas(tareas, argumento)
            print(resultado)   
    
 