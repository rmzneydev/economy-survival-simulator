#entrada de datos(inicio)
#control de un centro de datos

def data_entry():
        
    print("----Initial configuration - data center----\n")

    print(f"\n----player----")
    name = str(input("Enter the player's name: "))
        

    print("\nSelect the difficulty level: ")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")

    cond = False
    while not cond:
        try:
            difficulty = int(input("Option (1-3):  \n"))
            if difficulty ==1:
                cond=True
            elif difficulty ==2:
                cond=True
            elif difficulty ==3:
                cond=True
            else:
                print("Invalid option. Please select a number for one to three")    
        except:
            print("Invalid option. Please select a number for one to three")

    server_capacity = 0
    temperature = 0    
    clients = 0   
        
        #asignacion de recursos segun dificultad

    if difficulty == 1:
        server_capacity = 100
        temperature = 30    
        clients = 100  
        
        print(f"level: easy\n, server_capacity: {server_capacity}\n, temperature: {temperature}\n, clients: {clients}")
    
    elif difficulty == 2:
        server_capacity = 50
        temperature = 50    
        clients = 50  
        
        print(f"level: Medium\n, server_capacity: {server_capacity}\n, temperature: {temperature}\n, clients: {clients}")
        
    elif difficulty == 3:
        server_capacity = 20
        temperature = 70    
        clients = 20  
        
        print(f"level: Hard\n, server_capacity: {server_capacity}\n, temperature: {temperature}\n, clients: {clients}")    

    resources = [server_capacity, temperature, clients]
    return resources
data_entry()




# print("\n----INITIAL SUMMARY----\n")


# print(f"----player----\n") 
# print(f"name: {name} , level: {difficulty}")
 
 

    

    








        