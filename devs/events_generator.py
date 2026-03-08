import random

def get_events(difficulty):
      # Lista de posibles eventos que pueden ocurrir  
   events = [
         "Temperature > 80°C",
         "Failure in the cooling system",
         "Electrical overload",
         "Fire in technical room",
         "Flooding due to broken pipe",
         "Cyberattack",
         "Network collapse",
         "Internal virus"
         ]

   probability = 0 # probabilidad total de que ocurra un evento

   if difficulty == 1:
      probability = random.randint(5, 10)
   elif difficulty == 2:
      probability = random.randint(15, 30)
   elif difficulty == 3:
      probability = random.randint(30, 40)
    # Se divide la probabilidad total entre la cantidad de eventos
   base_probability = probability / len(events)

   accumulate=0  # Acumulador de probabilidades 
   range_event=[] # Lista donde se guardarán los rangos acumulados

 # Se generan rangos acumulados de probabilidad para cada evento
   for i in range (len(events)):
      accumulate += base_probability  # Se suma la probabilidad base
      range_event.append(accumulate) # Se guarda el valor acumulado
      

   random_num = random.randint(1, 100) 

   range_accumulate=0
   event="quiet day" # Evento por defecto (si no ocurre nada)

   for i in range (len(range_event)):
     if random_num>=range_accumulate and random_num<=range_event[i]:
       # Si cae en el rango, se retorna el número de evento y su descripción
      return [i+1, event]
   range_accumulate=range_event[i]   
   # Si no cayó en ningún rango, significa que no ocurrió ningún evento
   return 0, event


