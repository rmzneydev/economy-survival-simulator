servidores = 0
refrigeracion= 0
clientes = 0
temperatura = 80

# Si los servidores llegan a 0
if servidores <= 0:
    print(" Todos los servidores dejaron de funcionar")
    derrota = True

# Si la refrigeración llega a 0
if refrigeracion <= 0:
    print(" El sistema de refrigeración colapsó")
    derrota = True

# Si los clientes llegan a 0
if clientes <= 0:
    print(" Perdiste todos los clientes")
    derrota = True

# Evento crítico de temperatura
if temperatura > 80:
    print("Temperatura mayor a 80°C")
    print("SERVIDORES QUEMADOS")
    derrota = True
    