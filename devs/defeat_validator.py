def GameOver(servers, cooling, clients, temperature):
    # If servers reach 0
    if servers <= 0:
        print("All servers stopped working")
        print("You lost")
        return False

    # If cooling reaches 0
    if cooling <= 0:
        print("The cooling system collapsed")
        print("You lost")
        return False

    # If clients are greater than or equal to servers
    if clients >= servers:
        print("You lost all your clients")
        print("You lost")
        return False

    # Critical temperature event
    if temperature > 80:
        print("Temperature higher than 80°C")
        print("SERVERS BURNED")
        print("You lost")
        return False

GameOver(7, 5, 6, 60)