import random
from data_entry import setName, setDifficult, getResources
from events_generator import get_events
from consumption import calculate_consumption, increase_temperature
from defeat_validator import GameOver
from console_interface import show_welcome, show_resources_table, print_title, show_player_summary

def MainLoop(): 

    show_welcome() #  Bienvenida
    name = setName() #  Nombre
    difficult = setDifficult()#  Dificultad

    show_player_summary(name, difficult) # Muestra el nombre y dificultad
    
    resource = getResources(difficult) # Obtener Recursos

    # lista de días
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    current_day = random.randint(0,6) # Escoger un día aleatorio

    input("<Press any key to start simulation>\n")
    
    Day = 1 # dia de inicio de simulacion 
    game_over = False

    # Bucle while para repetir los 10 días del juego
    while Day <= 10 and game_over == False:

        # Mostrar en consola el día que está, el evento y el consumo del recurso
        print("Simulation Day #", Day, ": ", days[current_day])
        event = get_events(difficult) # Eventos
        number_of_event = event[0] # Numero de evento
        name_of_event = event[1] # Nombre del evento
        print("Events: ", name_of_event)

        # consumo de recursos
        consumption = calculate_consumption(number_of_event, difficult, resource, current_day)
        # estado de temperatura
        temperature_before = increase_temperature(number_of_event, resource[3])
        # agregar temperatura a la lista
        consumption.append(temperature_before)
        resource = consumption # actualizar recursos

        servers = resource[0] # servidores
        cooling = resource[1] # refrigeracion
        clients = resource[2] # clientes
        temperature = resource[3] # temperatura

        show_resources_table(servers, cooling, clients, temperature) # tabla recursos actualizada
        
        game_over = GameOver(servers, cooling, clients, temperature)

        if game_over == False: ## si el juego no se ha terminado

            # Condicional para los dias de la SEMANA
            if current_day == 6:
                current_day = 0
            else:
                current_day +=1

            # Condicional para los dias de la SIMULACION
            if Day < 10:
                input("\n<Press any key to go to the next day>\n")
            elif Day == 10:
                print_title("Congratulations! You won! \n You completed the simulation\n without any critical events.")
            
            Day += 1

MainLoop()








    
