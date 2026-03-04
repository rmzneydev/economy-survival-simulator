def GameOver(servidores, refrigeracion, clientes, temperatura):
    # Si los servidores llegan a 0
    if servidores <= 0:
        print(" Todos los servidores dejaron de funcionar")
        print("Perdiste")
        return False

    # Si la refrigeración llega a 0
    if refrigeracion <= 0:
        print(" El sistema de refrigeración colapsó")
        print("Perdiste")
        return False

    # Si los clientes llegan a 0
    if clientes <= 0:
        print(" Perdiste todos los clientes")
        print("Perdiste")
        return False

    # Evento crítico de temperatura
    if temperatura > 80:
        print("Temperatura mayor a 80°C")
        print("SERVIDORES QUEMADOS")
        print("Perdiste")
        return False

GameOver(7, 5, 6, 60)