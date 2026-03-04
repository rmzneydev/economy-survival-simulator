import random


event = ""
def gen_evento():
 random_event = random.randint(1, 8)

 if random_event == 1:
    event = "temperatura a 80°C"
        
 elif random_event == 2:
    event = "falla en el sistema de refrigeracion"

 elif random_event == 3:
    event = "sobrecarga electrica"

 elif random_event == 4:
    event = "incendio en sala tecnica"
    
 elif random_event == 5:
     event = "inundaciones por tuberia rota"

 elif random_event == 6:
    event = "ciberataque"

 elif random_event == 7:
    event = "colapso de la red"
    
 elif random_event == 8:
    event = "virus interno"
 print("Se presento el evento:", event)

 return [random_event, event]


# obtener = gen_evento()
# print(obtener[0])
# print(obtener[1])



