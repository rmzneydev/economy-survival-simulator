import random

# Funcion para calcular el consumo diario, segun el evento
def calculate_consumption(number_of_event:int, difficult:int, resources:list, day:int):
    consumption = 0
    #Lista para guardar los recursos [Servidores, Refrigerracion, Clientes]
    consumption_array = []
    #Verifica si el numero del evento existe o es null

    if number_of_event >= 0:

        #Dificultad: Easy
        if difficult == 1:
            resource_id = 0
            #Verifica si es un evento existente
            if number_of_event == 1:
                for i in range(1, 4):
                    resource_before = 0
                    consumption_array.append(resource_before)

            if number_of_event >= 2 and number_of_event <= 8:
                for i in range(1, 4):
                    if day == 1 or day == 2:                        
                        consumption = 10.8
                    elif day == 6 or day == 7:
                        consumption = 11.2
                    else:
                        consumption = 10
                    ram = random.randint(1, 7)
                    if ram == 5:
                        consumption += 5
                    if i == 3:
                        resource_before = resources[resource_id] + int(consumption)
                    elif i == 1:
                        resource_before = resources[resource_id] - int(consumption)
                    else:
                        resource_before = resources[resource_id] - consumption
                    resource_id += 1
                    consumption_array.append(resource_before)
            #Verifica si es el evento nulo
            elif number_of_event == 0:
                    for i in range(1, 4):
                        resource_before = resources[resource_id] - 1
                        if i == 3:
                            resource_before = resources[resource_id] + 1
                        consumption_array.append(resource_before)
                        resource_id += 1
        #Dificultad: Medium
        elif difficult == 2:
            resource_id = 0

            if number_of_event == 1:
                for i in range(1, 4):
                    resource_before = 0
                    consumption_array.append(resource_before)
            #Verifica si es un evento existente
            if number_of_event >= 2 and number_of_event <= 8:
                for i in range(1, 4):
                    if day == 1 or day == 2:                        
                        consumption = 5.8
                    elif day == 6 or day == 7:
                        consumption = 6.2
                    else: 
                        consumption = 5
                    ram = random.randint(1, 5)
                    if ram == 3:
                        consumption += 3
                    if i == 3:
                        resource_before = resources[resource_id] + int(consumption)
                    elif i == 1:
                        resource_before = resources[resource_id] - int(consumption)
                    else:
                        resource_before = resources[resource_id] - consumption
                    resource_id += 1
                    consumption_array.append(resource_before)

            #Verifica si es el evento nulo
            elif number_of_event == 0:
                    for i in range(1, 4):
                        resource_before = resources[resource_id] - 1
                        if i == 3:
                            resource_before = resources[resource_id] + 1
                        consumption_array.append(resource_before)
                        resource_id += 1

        #Dificultad: Hard     
        elif difficult == 3:
            resource_id = 0


            if number_of_event == 1:
                for i in range(1, 4):
                    resource_before = 0
                    consumption_array.append(resource_before)
            #Verifica si es un evento existente
            if number_of_event >= 2 and number_of_event <= 8:
                for i in range(1, 4):
                    if day == 1 or day == 2:                        
                        consumption = 2.8
                    elif day == 6 or day == 7:
                        consumption = 3.2
                    else: 
                        consumption = 5
                    ram = random.randint(1, 3)
                    if ram == 2:
                        consumption += 3
                    if i == 3:
                        resource_before = resources[resource_id] + int(consumption)
                    elif i == 1:
                        resource_before = resources[resource_id] - int(consumption)
                    else:
                        resource_before = resources[resource_id] - consumption
                    resource_id += 1
                    consumption_array.append(resource_before)


            #Verifica si es el evento nulo
            elif number_of_event == 0:
                    for i in range(1, 4):
                        resource_before = resources[resource_id] - 1
                        print(resource_before)
                        if i == 3:
                            resource_before = resources[resource_id] + 1
                        consumption_array.append(resource_before)
                        resource_id += 1
    
    return consumption_array

#Funcion para aumentar la temperatura
def increase_temperature(event:int, temperature_after:int):

    #Variable de incremento
    increase = 0
    if event != 0:
        temperature_before = 0
        if event == 1:
                temperature_before = 81
        #Verifica si el evento hace parte de los primeros.(Estos suben mas la temperatura)
        if event >= 2 and event <= 4:
            increase = random.randint(8, 10)
            temperature_before = temperature_after + increase
            
        #Verifica si el evento hace parte de los primeros.(Estos suben menos la temperatura)
        if event >= 5 and event <= 8:
            increase = random.randint(5, 7)
            temperature_before = temperature_after + increase
    else:
        temperature_before = temperature_after

    return temperature_before