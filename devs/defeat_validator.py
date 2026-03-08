def GameOver(servers, cooling, clients, temperature):
    # If servers reach 0
    if servers <= 0:
        print("All servers stopped working")
        print("You lost")
        return True

    # elif cooling reaches 0
    elif cooling <= 0:
        print("The cooling system collapsed")
        print("You lost")
        return True

    # elif clients are greater than or equal to servers
    elif clients >= servers:
        print("You lost all your clients")
        print("You lost")
        return True

    # Critical temperature event
    elif temperature > 80:
        print("Temperature higher than 80°C")
        print("SERVERS BURNED")
        print("You lost")
        return True

    else:
        return False
