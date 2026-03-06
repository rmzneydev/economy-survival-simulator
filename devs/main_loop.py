import random
from data_entry import setName, setDifficult, getResources
from events_generator import get_events
from consumption import calculate_consumption, increase_temperature



def MainLoop(): 

    # Creación de variables de prueba
    name = setName()
    difficult = setDifficult()
    resource = getResources(difficult) 

    Day = 1
    GameOver = 0
    # Problem = "Subió la temperatura 5°"
    # consumption = 4
    # recursos = 15
    # lvl = 2

    # lista de días
    days = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    # Escoger un día aleatorio

    current_day = random.randint(0,6)

    #Bucle while para repetir los 10 días del juego
    while Day <= 10 or GameOver == True:

        #Mostrar en consola el día que está, el evento y el consumo del recurso
        print("Day", Day, ": ", days[current_day])
        event = get_events(difficult)
        print("Events: ", event[1])
        number_of_event = event[0]
      
        
        consumption = calculate_consumption(number_of_event, difficult, resource, current_day)
        temperature_before = increase_temperature(number_of_event, resource[3])
        consumption.append(temperature_before)
        resource = consumption
                      



        

        Day += 1
        if current_day == 6:
            current_day = 0
        else:
            current_day +=1

MainLoop()








    
