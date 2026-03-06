# Economy Survival Simulator
## Data Center Management
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

## How to Run the Project
From the terminal:

clone the repository
```bash
git clone https://github.com/rmzneydev/economy-survival-simulator.git
cd economy-survival-simulator
```
Since it's still in development, it's necessary to use Git.
And then choose the dev branch.
```bash
git switch dev
cd devs
```
To start playing run the following command:
```bash
pyhton main_loop.py
```


## Failure Conditions
- Temperature > 80°C
- Server Capacity = 0
- Cooling = 0
- Clients = 0

## Final Objective
To survive 10 days while maintaining a balance between:
- Customer demand
- Operational capacity
- Thermal control
