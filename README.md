# economy-survival-simulator
This project consists of a 10-day resource management simulator, where the player manages a Data Center.

# Survival Economy Simulator
## Group 4 – Data Center Management
---
## Project Description
This project consists of a 10-day resource management simulator where the player manages a data center.

The objective is to keep the servers operational by controlling:
- Server Capacity
- Cooling
- Clients
  
The program is developed using only:
- `while` loops
- `if/else` statements
- `print`

## Game Rules

1. The player selects a name and difficulty level.

2. The simulation lasts 10 days.

3. Random events can occur each day.

4. If the temperature exceeds **80°C**, the servers will crash (Game Over).

5. If a resource reaches 0, the game ends.

6. If there are more clients than server capacity, revenue is lost.

## Game Resources
- **Server Capacity**
- **Cooling (Temperature Control)**
- **Clients**
- **System Temperature**

## Random Events
Generated with `random.randint()`:
- Storm (affects cooling)
- Theft (reduces resources)
- Bonanza (increases customers)
