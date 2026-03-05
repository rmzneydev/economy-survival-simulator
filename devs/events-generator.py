import random


def get_events(difficulty):
      
   events = [
         "Temperature > 80Â°C",
         "Failure in the cooling system",
         "Electrical overload",
         "Fire in technical room",
         "Flooding due to broken pipe",
         "Cyberattack",
         "Network collapse",
         "Internal virus"
         ]

   probability = 0
   
   if difficulty == 1:
      probability = random.randint(5, 10)
   elif difficulty == 2:
      probability = random.randint(15, 30)
   elif difficulty == 3:
      probability = random.randint(31, 40)

   base_probability = probability / len(events)


   accumulate=0
   rangos=[]


   for i in range (len(events)):
      accumulate += probability
      rangos.append(accumulate)
      

   random_num = random.randint(1, 100) 

   range_accumulate=0
   event="quiet day"

   for i in range (len(rangos)):
      if random_num>=range_accumulate and random_num<=rangos[i]:
         event= events[i]
         range_accumulate=rangos[i]   
         print(event)
         print(range_accumulate)                     


