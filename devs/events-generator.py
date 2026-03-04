import random


event = ""
def gen_evento():
 random_event = random.randint(1, 9)

 if random_event == 1:
    event = "temperature to 80°C"
        
 elif random_event == 2:
    event = "failure in the cooling system"

 elif random_event == 3:
    event = "electrical overload"

 elif random_event == 4:
    event = "fire in technical room"
    
 elif random_event == 5:
    event = "flooding due to broken pipe"

 elif random_event == 6:
    event = "cyber attack"

 elif random_event == 7:
    event = "network collapse"
    
 elif random_event == 8:
    event = "internal virus"

 elif random_event == 9:
    event = "quiet day"
 print("The event was presented:", event)

 return [random_event, event]


