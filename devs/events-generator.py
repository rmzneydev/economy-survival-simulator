import random

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


def gen_difficulty():
    difficulty = random.randint(1, 3)
    if difficulty == 1:
        return random.randint(5, 10)
    elif difficulty == 2:
        return random.randint(15, 30)
    elif difficulty == 3:
        return random.randint(31, 40)

probability = gen_difficulty()/len(events)


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


