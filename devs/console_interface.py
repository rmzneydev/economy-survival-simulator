 #interface.py - Point 6: Console Interface


# -- HELPER FUNCTIONS (For decoration) --

def print_separator(character="-", length=40):
    """Prints a decorative line."""
    print(character * length)

def print_title(text):
    """Prints a centered and decorated title."""
    print_separator("=")
    print(f" {text.upper()} ".center(40, "="))
    print_separator("=")


# -- MAIN FUNCTIONS --

def show_welcome():
    """Displays the initial message of the program."""
    print("\n" * 2)  # Blank space above
    print_title("DATA CENTER SIMULATOR")
    print("\n Welcome to the control system.")
    print(" Your mission: Keep the servers cool and the clients happy.")
    print(" Good luck!")
    print("\n")
    print_separator("*", 40)


def show_player_summary(name, difficulty):
    """Displays a summary of the player data."""
    print("\n[ PLAYER DATA ]")
    print_separator(".")
    
    # Using f-strings to insert variables
    print(f" Operator Name: {name}")
    
    # Translate the difficulty number to text
    difficulty_text = ""
    if difficulty == "1":
        difficulty_text = "Easy"
    elif difficulty == "2":
        difficulty_text = "Medium"
    elif difficulty == "3":
        difficulty_text = "Hard"
    else:
        difficulty_text = "Unknown"
    
    print(f" Difficulty Level: {difficulty_text}")
    print_separator(".")


def show_resources_table(servers, temp, clients):
    """
    Displays the current resources in a table format
    using basic characters (| and -).
    """
    print("\n[ CURRENT DATA CENTER STATUS ]")
    
    # Table design with dashes and bars
    print("+----------------------+----------+")
    print("| RESOURCE             | VALUE    |")
    print("+----------------------+----------+")
    
    # Servers row
    print(f"| Server Capacity      | {servers:<8} |")
    
    # Temperature row (with visual warning if too high)
    temp_warning = ""
    if temp > 70:
        temp_warning = "!! HOT !!"
    
    print(f"| Current Temperature  | {temp:<8} C | {temp_warning}")
    
    # Clients row
    print(f"| Connected Clients    | {clients:<8} |")
    
    # Final line
    print("+----------------------+----------+")


def show_game_over(reason):
    """Displays a visual game over message."""
    print("\n" * 3)
    print_title("GAME OVER")
    print("\n The simulator has ended.")
    
    if reason == "temperature":
        print(" CRITICAL! The servers exceeded 80°C and burned out.")
        print(" Check the cooling system next time.")
    elif reason == "clients":
        print(" WARNING! Too many clients for the current capacity.")
        print(" Significant revenue has been lost.")
    else:
        print(f" Simulation ended due to: {reason}")
        
    print("\n Thanks for playing.")
    print_separator("=")
    print("\n")


# # -- QUICK TEST (Optional) --
# # If you run this file directly, you will see how the interface looks.
# if __name__ == "__main__":
#     show_welcome()
#     show_player_summary("Sam", "2")
#     show_resources_table(100, 30, 100)  # Everything OK
#     # show_resources_table(50, 75, 120)  # Example with high temperature
#     # show_game_over("temperature")
