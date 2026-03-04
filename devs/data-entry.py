#entrada de datos(inicio)
#control de un centro de datos

def data_entry():
        
    print("----Initial configuration - data center----\n")

    print(f"\n----player----")
    name = str(input("Enter the player's name: "))
        

    print("\nSelect the difficulty level: ")
    print("1. easy")
    print("2. medium")
    print("3. hard")
        
    difficulty = input("option (1-3):  \n")

    server_capacity = 0
    temperature = 0    
    clients = 0   
        
        #asignacion de recursos segun dificultad

    if difficulty == "1":
        server_capacity = 100
        temperature = 30    
        clients = 100  
        
        print(f"level: easy\n, server_capacity: {server_capacity}\n, temperature: {temperature}\n, clients: {clients}")
    
    elif difficulty == "2":
        server_capacity = 50
        temperature = 50    
        clients = 50  
        
        print(f"level: medium\n, server_capacity: {server_capacity}\n, temperature: {temperature}\n, clients: {clients}")
        
    elif difficulty == "3":
        server_capacity = 20
        temperature = 70    
        clients = 20  
        
        print(f"level: hard\n, server_capacity: {server_capacity}\n, temperature: {temperature}\n, clients: {clients}")    
    
        
        
    else:
        server_capacity = 50
        temperature = 50    
        clients = 50 
        difficulty = "2"
        print("Invalid option. Medium difficulty will be assigned by default. ")
        print(f"level: medium\n, server_capacity: {server_capacity}\n, temperature: {temperature}\n, clients: {clients}")

    resources = [server_capacity, temperature, clients]
    return resources





# print("\n----INITIAL SUMMARY----\n")


# print(f"----player----\n") 
# print(f"name: {name} , level: {difficulty}")
 
 

    

    








        