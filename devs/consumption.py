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

num = int(input("Evento -> "))
dif = int(input("Difficult -> "))
rec_list = [50, 50, 0]
print(calculate_consumption(num, dif, rec_list))