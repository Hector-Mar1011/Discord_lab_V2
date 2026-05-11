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