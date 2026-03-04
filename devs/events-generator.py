import random

def gen_evento():
 random_event = random.randint(1, 8)

 if random_event == 1:
    return [random_event, "temperatura a 80°C"]
        
 elif random_event == 2:
    return [random_event, "falla en el sistema de refrigeracion"]

 elif random_event == 3:
    return [random_event, "sobrecarga electrica"]

 elif random_event == 4:
    return [random_event, "incendio en sala tecnica"]
    
 elif random_event == 5:
     return [random_event, "inundaciones por tuberia rota"]

 elif random_event == 6:
    return [random_event, "ciberataque"]

 elif random_event == 7:
    return [random_event, "colapso de la red"]
    
 elif random_event == 8:
    return [random_event, "virus interno"]




 
print(gen_evento())


