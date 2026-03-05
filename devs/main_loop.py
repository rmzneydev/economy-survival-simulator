import random
from data_entry import setName, setDifficult, getResources

name = setName()
difficult = setDifficult()
resource = getResources(difficult) 




def MainLoop(): 

    # Creación de variables de prueba

    Day = 1
    GameOver = 0
    Problem = "Subió la temperatura 5°"
    consumption = 4
    recursos = 15
    lvl = 2

    # lista de días
    days = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Viernes", "Sábado", "Domingo"]

    # Escoger un día aleatorio

    current_day = random.randint(0,7)

    #Bucle while para repetir los 10 días del juego
    while Day <= 10 or GameOver == True:
        
        #Mostrar en consola el día que está, el evento y el consumo del recurso
        print("Day ", Day)
        print(Problem)
        print("has consumido", consumption, "recursos")
        

        Day += 1
        current_day += 1
        if current_day == 7:
            current_day = 0

MainLoop()








    
