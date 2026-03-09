#entrada de datos(inicio)
#control de un centro de datos

def setName():
        
    print("----Initial configuration - data center----\n")

    print(f"\n----player----")
    name = input("Enter the player's name: ")

    return name




def setDifficult():

    print("\nSelect the difficulty level: ")
    print("1. easy")
    print("2. medium")
    print("3. hard")

    cond = False
    while not cond:
        try:   
   
          difficulty = int(input("option (1-3):  \n"))
          if difficulty ==1:
              cond = True
          
          elif difficulty ==2:
              cond = True
          
          elif difficulty ==3:
              cond = True

          else:
              print("invalid option. please select a number for one to three")
        except:
              print("invalid option. please select a number for one to three")  
    return difficulty
 
 
def getResources(difficulty):
        
    if difficulty == 1:
        server_capacity = 100
        cooling = 100
        temperature = 30    
        clients = 0
        
        print(f"level: easy\n, server_capacity: {server_capacity}\n, temperature: {temperature}\n, clients: {clients}")
    
    elif difficulty == 2:
        server_capacity = 50
        cooling = 50
        temperature = 30   
        clients = 0
        
        print(f"level: medium\n, server_capacity: {server_capacity}\n, temperature: {temperature}\n, clients: {clients}")
        
    elif difficulty == 3:
        server_capacity = 20
        temperature = 30    
        cooling = 20
        clients = 0
        
        print(f"level: hard\n, server_capacity: {server_capacity}\n, temperature: {temperature}\n, clients: {clients}")  
    
    resources = [server_capacity, cooling, clients, temperature]

    return resources

    
    

    








        
