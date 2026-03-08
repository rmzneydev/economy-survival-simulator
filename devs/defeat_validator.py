from console_interface import show_game_over

def GameOver(servers, cooling, clients, temperature):
    # Evento Critico
    if temperature > 80:
        show_game_over("temperature")
        return True
    
    # Servidores
    elif servers <= 0:
        show_game_over("All servers stopped working")
        return True

    # Refrigeracion 
    elif cooling <= 0:
        show_game_over("The cooling system collapsed")
        return True

    # Clientes
    elif clients >= servers:
        show_game_over("clients")
        return True  

    else:
        return False 
