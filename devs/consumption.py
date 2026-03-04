random_event = int(input("Numero de evento -> "))
lvl = int(input("Dificultad -> "))
resourc = [0, 1, 2, 3]

resourc[1] = int(input("capacidad de servidores -> "))
resourc[2]= int(input("refrigeracion -> "))
resourc[3] = int(input("clientes -> "))

consumption = random_event * 2

if random_event <= 4:
    if lvl == 1:
        for i in range(1, 4):
            consumption = random_event * 2 * i
            resourc[i] = resourc[i] - consumption
    if lvl == 2:
        for i in range(1, 4):
            consumption = random_event * 3 * i
            resourc[i] = resourc[i] - consumption
    if lvl == 3:
        for i in range(1, 4):
            consumption = random_event * 4 * i
            resourc[i] = resourc[i] - consumption
    
    print("Servidores: ", resourc[1])
    print("Refrigeracion: ", resourc[2])
    print("Clientes: ", resourc[3])