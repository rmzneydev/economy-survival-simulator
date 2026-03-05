import random

# Funcion para calcular el consumo diario, segun el evento
def calculate_consumption(number_of_event:int, difficult:int, resources:list):
    consumption = 0
    #Lista para guardar los recursos [Servidores, Refrigerracion, Clientes]
    consumption_array = []
    #Verifica si el numero del evento existe o es null

    if number_of_event:

        #Dificultad: Easy
        if difficult == 1:
            resource_id = 0
            #Verifica si es un evento existente
            if number_of_event >= 1 and number_of_event <= 8:
                for i in range(1, 4):
                    consumption = 10
                    ram = random.randint(1, 7)
                    if ram == 5:
                        consumption += 5
                    if i == 3:
                        resource_before = resources[resource_id] + consumption
                    else:
                        resource_before = resources[resource_id] - consumption
                    resource_id += 1
                    consumption_array.append(resource_before)
            #Verifica si es el evento nulo
            elif number_of_event > 8:
                    for i in range(1, 4):
                        resource_before = resources[resource_id] - 1
                        if i == 3:
                            resource_before = resources[resource_id] + 1
                        consumption_array.append(resource_before)
                        resource_id += 1
        #Dificultad: Medium
        elif difficult == 2:
            resource_id = 0

            #Verifica si es un evento existente
            if number_of_event >= 1 and number_of_event <= 8:
                for i in range(1, 4):
                    consumption = 5
                    ram = random.randint(1, 5)
                    if ram == 3:
                        consumption += 3
                    if i == 3:
                        resource_before = resources[resource_id] + consumption
                    else:
                        resource_before = resources[resource_id] - consumption
                    resource_id += 1
                    consumption_array.append(resource_before)

            #Verifica si es el evento nulo
            elif number_of_event > 8:
                    for i in range(1, 4):
                        resource_before = resources[resource_id] - 1
                        if i == 3:
                            resource_before = resources[resource_id] + 1
                        consumption_array.append(resource_before)
                        resource_id += 1

        #Dificultad: Hard     
        elif difficult == 3:
            resource_id = 0

            #Verifica si es un evento existente
            if number_of_event >= 1 and number_of_event <= 8:
                for i in range(1, 4):
                    consumption = 2
                    ram = random.randint(1, 3)
                    if ram == 2:
                        consumption += 3
                    if i == 3:
                        resource_before = resources[resource_id] + consumption
                    else:
                        resource_before = resources[resource_id] - consumption
                    resource_id += 1
                    consumption_array.append(resource_before)

            #Verifica si es el evento nulo
            elif number_of_event > 8:
                    for i in range(1, 4):
                        resource_before = resources[resource_id] - 1
                        if i == 3:
                            resource_before = resources[resource_id] + 1
                        consumption_array.append(resource_before)
                        resource_id += 1
    
    return consumption_array

#Funcion para aumentar la temperatura
def increase_temperature(event:int, temperature_after:int):

    #Variable de incremento
    increase = 0
    #Verifica si el evento hace parte de los primeros.(Estos suben mas la temperatura)
    if event >= 1 and event <= 4:
        increase = random.randint(8, 10)
        temperature_before = temperature_after - increase
        
    #Verifica si el evento hace parte de los primeros.(Estos suben menos la temperatura)
    if event >= 5 and event <= 8:
        increase = random.randint(5, 7)
        temperature_before = temperature_after - increase

    return temperature_before

num = int(input("Evento -> "))
dif = int(input("Difficult -> "))
rec_list = [50, 50, 0]
print(calculate_consumption(num, dif, rec_list))