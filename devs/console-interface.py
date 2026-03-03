#Proyecto de Data Center
#interfaz.py
Dia= 1 
servidores = 50
refrigeracion= 100
clientes= 10
temperatura = 80

print("\n" + " "  + "-" *40)
print(" ESTADO DEL DATA CENTER - DIA", Dia)
print("" + "-"*40)

#fila de servidores

print(" Recursos       | valor")
print(" " + "-"*40)
print("  Servidores    | ", servidores )
print(" Refrigeracion  | ", refrigeracion)
print(" Clientes       |",  clientes)
print(" " + "-"*40)

#Sección de Temperatura y Alerta
print(" TEMPERATURA ACTUAL | ", temperatura, "°C" )

#Una barra de carga simple con corchetes y asteriscos
#si la temperatura es 80, mostrará 10 asteriscos

barra = "*" * int(temperatura / 8)
espacio_vacio = "" * (10 - len(barra))

print(" Nivel Critico: [" + barra +  espacio_vacio + "]")

if temperatura > 75:
      print("!!! ADVERTENCIA: RIESGO DE QUEMA !!!")
print("" + "-"*40 + "\n")     