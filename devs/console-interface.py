
# interfaz.py - Punto 6: Interfaz de Consola


# -- FUNCIONES DE AYUDA (Para decorar) --

def imprimir_separador(caracter="-", largo=40):
    """Imprime una línea decorativa."""
    print(caracter * largo)

def imprimir_titulo(texto):
    """Imprime un título centrado y decorado."""
    imprimir_separador("=")
    print(f" {texto.upper()} ".center(40, "="))
    imprimir_separador("=")


# -- FUNCIONES PRINCIPALES --

def mostrar_bienvenida():
    """Muestra el mensaje inicial del programa."""
    print("\n" * 2) # Espacio en blanco arriba
    imprimir_titulo("SIMULADOR DATA CENTER")
    print("\n Bienvenido/a al sistema de control.")
    print(" Tu misión: Mantener los servidores frescos y a los clientes felices.")
    print(" ¡Mucha suerte!")
    print("\n")
    imprimir_separador("*", 40)


def mostrar_resumen_jugador(nombre, dificultad):
    """Muestra un resumen de los datos del jugador."""
    print("\n[ DATOS DEL JUGADOR ]")
    imprimir_separador(".")
    # Usamos f-strings para insertar las variables
    print(f" Nombre del Operador: {nombre}")
    
    # Traducimos el número de dificultad a texto
    texto_dif = ""
    if dificultad == "1": texto_dif = "Fácil"
    elif dificultad == "2": texto_dif = "Medio"
    elif dificultad == "3": texto_dif = "Difícil"
    else: texto_dif = "Desconocida"
    
    print(f" Nivel de Dificultad: {texto_dif}")
    imprimir_separador(".")


def mostrar_tabla_recursos(servidores, temp, clientes):
    """
    Muestra los recursos actuales en formato de tabla
    usando caracteres básicos (| y -).
    """
    print("\n[ ESTADO ACTUAL DEL CENTRO DE DATOS ]")
    
    # Diseño de la tabla con guiones y barras
    print("+----------------------+----------+")
    print("| RECURSO              | VALOR    |")
    print("+----------------------+----------+")
    
    # Fila de Servidores
    # :<20 alinea a la izquierda en 20 espacios
    # :>8 alinea a la derecha en 8 espacios
    print(f"| Capacidad Servidores | {servidores:<8} |")
    
    # Fila de Temperatura (con aviso visual si está alta)
    aviso_temp = ""
    if temp > 70:
        aviso_temp = "!! CALIENTE !!"
    
    print(f"| Temperatura Actual   | {temp:<8} C | {aviso_temp}")
    
    # Fila de Clientes
    print(f"| Clientes Conectados  | {clientes:<8} |")
    
    # Línea final
    print("+----------------------+----------+")


def mostrar_fin_juego(causa):
    """Muestra un mensaje visual de fin de juego."""
    print("\n" * 3)
    imprimir_titulo("GAME OVER")
    print("\n El simulador ha terminado.")
    
    if causa == "temperatura":
        print(" ¡CRÍTICO! Los servidores superaron los 80°C y se quemaron.")
        print(" Revisa el sistema de refrigeración la próxima vez.")
    elif causa == "clientes":
        print(" ¡AVISO! Demasiados clientes para la capacidad actual.")
        print(" Se han perdido ingresos importantes.")
    else:
        print(f" Fin de la simulación por: {causa}")
        
    print("\n Gracias por jugar.")
    imprimir_separador("=")
    print("\n")


# -- PRUEBA RAPIDA (Opcional) --
# Si ejecutas este archivo directamente, verás cómo quedan los dibujos.
if __name__ == "__main__":
    mostrar_bienvenida()
    mostrar_resumen_jugador("Sam", "2")
    mostrar_tabla_recursos(100, 30, 100) # Todo bien
    # mostrar_tabla_recursos(50, 75, 120)  # Ejemplo con temperatura alta
    # mostrar_fin_juego("temperatura")