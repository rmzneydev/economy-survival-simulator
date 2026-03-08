# economy-survival-simulator
This project consists of a 10-day resource management simulator, where the player manages a Data Center.
def print_separator(character="-", length=40):
    """Prints a decorative line."""
    print(character * length)

def print_title(text):
    """Prints a centered and decorated title."""
    print_separator("=")
    print(f" {text.upper()} ".center(40, "="))
    print_separator("=")


def show_welcome():
    """Displays the initial message of the program."""
    print("\n" * 2)  # Blank space above
    print_title("DATA CENTER SIMULATOR")
    print("\n Welcome to the control system.")
    print(" Your mission:\n Keep the servers cool and the clients happy.")
    print(" Good luck!")
    print("\n")
    print_separator("*", 40)


def show_player_summary(name, difficulty):
    """Displays a summary of the player data."""
    print("\n[ PLAYER DATA ]")
    print_separator(".")
    
    print(f" Operator Name: {name}")
    
    difficulty_text = ""
    if difficulty == 1:
        difficulty_text = "Easy"
    elif difficulty == 2:
        difficulty_text = "Medium"
    elif difficulty == 3:
        difficulty_text = "Hard"
    else:
        difficulty_text = "Unknown"
    
    print(f" Difficulty Level: {difficulty_text}")
    print_separator(".")


def show_resources_table(servers, cooling, clients, temp):
    """
    Displays the current resources in a table format
    using basic characters (| and -).
    """
    
    temp = str(f"{temp}°C")
    cooling = str(f"{cooling:.1f}")

    print("\n[ CURRENT DATA CENTER STATUS ]")
    print("+----------------------+----------+")
    print("| RESOURCE             | VALUE    |")
    print("+----------------------+----------+")
    print(f"| Server Capacity      | {servers:<8} |")
    print(f"| Cooling              | {cooling:<8} |")
    print(f"| Current Temperature  | {temp:<8} |")
    print(f"| Connected Clients    | {clients:<8} |")
    print("+----------------------+----------+")


def show_game_over(reason):
    """Displays a visual game over message."""
    print("\n" * 3)
    print_title("GAME OVER")
    print("\n The simulator has ended.")
    
    if reason == "temperature":
        print(" Reason:\n The servers temperature exceeded 80°C and burned out.")
        print(" Check the cooling system next time.")
    elif reason == "clients":
        print(" Reason:\n Too many clients for the current server capacity.")
        print(" Significant revenue has been lost.")
    else:
        print(f" Simulation ended due to: \n{reason}")
        
    print("\n Thanks for playing.")
    print_separator("=")
    print("\n")
