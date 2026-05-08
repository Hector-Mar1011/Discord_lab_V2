import datetime

def analizar_comando(entrada_usuario):
    """
    segunda fase del Agente: procesamiento de comandos y lógica dinamica.
    Aquí el alumno aprednde a separar la 'acción' de los datos."""

    mensaje = entrada_usuario.lower().strip()

    #Simulación de comandos prefijos(como se usan en Discord !Ayuda, !Ejemlo)
    
    if mensaje.startswith("!"):
        partes = mensaje.split(" ", 1)  # Dividir en comando y argumento
        comando = partes[0]
        argumento = partes[1] if len(partes) > 1 else None

        #Logica de comandos
        if comando == "!definir":
            return buscar_en_diccionario(argumento)
        
        elif comando == "!validar":
            return validar_variable(argumento)
        
        elif comando == "!hora":
            ahora = datetime.datetime.now().strftime("%H:%M:%S")
            return f"La hora actual del servidor es: {ahora}"
        
        elif comando == "!ayuda":
            return ("Comandos disponibles:\n"
                    "!definir [termino] - Busca la definición de un término en el diccionario.\n"
                    "!validar [nombre] - Valida si un nombre de variable es correcto.\n"
                    "!hora - Muestra la hora actual del servidor.\n"
                    "!ayuda - Muestra esta ayuda.")

def buscar_en_diccionario(termino):


def validar_variable(nombre):
