from data_entry import setDifficult
from defeat_validator import GameOver

def run_product_owner_tests():
    print("="*50)
    print("  PRODUCT OWNER OFFICIAL TEST SUITE - GROUP 4  ")
    print("="*50)


    print("="*60)
    print("\n[TEST 1] Temperature Limit test (Critical Event)")
    servers = 100
    cooling = 100
    clients = 10
    temperature = 80.1
    print("Assuming our resources are: ")
    print(f"(Servers: {servers})")
    print(f"(Cooling: {cooling})")
    print(f"(Clients: {clients})")
    print(f"Then what happens if (Temperature is: {temperature}°C)")
    input("<Press enter to check test>\n")
    
    if GameOver(servers, cooling, clients, temperature):
        print(f"[Success]: System catches overheat at temperature > 80°C.")
    else:
        print(f"[Fail]: System ignored overheat at temperature > 80°C.")
    
    print("="*60)
    print("\n[TEST 2] Server Scalability Logic")

    print("Assuming our resources are: ")
    clients = 100
    servers = 99
    temperature = 50
    print(f"(Servers: {servers})")
    print(f"(Cooling: {cooling})")
    print(f"(Temperature: {clients})")
    print(f"Then what happens if we have this (Number of clients: {servers}) ")
    input("<Press enter to check test>\n")
    
    if GameOver(servers, cooling, clients, temperature):
        print(f"[Success]: Game ends when clients ({clients}) > servers ({servers}).")
    else:
        print("[Fail] System allowed illegal client load.")

   
    print("="*60)
    print("\n[TEST 3] Total System Collapse (0 Resources)")
    print("Assuming our resources are: ")
    clients = 60
    servers = 100
    cooling = 0
    print(f"(Servers: {servers})")
    print(f"(Clients: {clients})")
    print(f"(Temperature: {clients})")
    print(f"Then what happens if we have this (Cooling value: {cooling})")
    input("<Press enter to check test>\n")
    
    if GameOver(servers, cooling, clients, temperature):
        print("[Success]: Cooling at 0 stops the program.")
    else:
        print("[Fail]: Program continued with 0 cooling.")

    
    print("="*60)
    print("\n[TEST 4] Input Validation (Manual Check)")
    print("What happens if user enter a negative difficulty?")
    print("- The program must NOT crash.")
    print("- It must display: 'invalid option. please select a number for one to three'.")
    print("- It must keep asking until you enter 1, 2, or 3.\n So lest Try It")
    setDifficult()
    

    

    print("\n" + "="*50)
    print("                TESTING COMPLETE                ")
    print("="*50)

if __name__ == "__main__":
    run_product_owner_tests()