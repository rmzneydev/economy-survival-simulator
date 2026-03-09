# Data Center Control Simulator

[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![GitHub contributors](https://img.shields.io/github/contributors/rmzneydev/economy-survival-simulator)](https://github.com/rmzneydev/economy-survival-simulator/graphs/contributors)

Welcome to the **Data Center Control Simulator**. This is a console-based simulation project, developed in Python, that puts you in charge of a data center. Your mission, should you choose to accept it, is to manage resources for 10 days to keep the servers operational, the temperature under control, and the clients happy.

The project was developed as part of a collaborative exercise, applying agile methodologies, Git workflows (with branches and pull requests), and structured programming principles in Python.

## Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Game Mechanics](#game-mechanics)
  - [Resources](#resources)
  - [Difficulty Levels](#difficulty-levels)
  - [Events](#events)
  - [Win/Loss Conditions](#winloss-conditions)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [How to Play](#how-to-play)
- [Project Structure](#project-structure)
- [Development Team](#development-team)
- [License](#license)

## Overview

**Data Center Control Simulator** is a turn-based resource management game developed as a collaborative learning project. Players must balance server capacity, cooling systems, and client demand while managing temperature fluctuations and random events. The game features three difficulty levels and multiple failure scenarios, making each playthrough unique.

**The challenge:** Survive 10 days without:
- Exceeding 80°C temperature
- Running out of server capacity
- Losing all cooling capability
- Overwhelming your servers with clients

## Key Features

- **Turn-based gameplay:** Make strategic decisions over 10 simulated days
- **Dynamic temperature system:** Watch how events affect your server room climate
- **Real-time resource tracking:** Monitor servers, cooling, clients, and temperature
- **Random event generator:** Face unexpected challenges daily
- **Three difficulty levels:** Easy (100/100), Medium (50/50), Hard (20/20) starting resources
- **Clean console interface:** User-friendly tables and visual feedback
- **Multiple endings:** Different failure scenarios and a victory condition

## Game Mechanics

### Resources

| Resource | Description | Critical Threshold |
|----------|-------------|-------------------|
| **Server Capacity** | Available processing power | ≤ 0 or overwhelmed by clients |
| **Cooling** | Cooling system efficiency | ≤ 0 |
| **Temperature** | Server room heat level | > 80°C |
| **Clients** | Current service demand | ≥ Server Capacity |

### Difficulty Levels

| Level | Starting Servers | Starting Cooling | Starting Temperature | Event Probability |
|-------|-----------------|------------------|---------------------|-------------------|
| **Easy (1)** | 100 | 100 | 30°C | 5-10% |
| **Medium (2)** | 50 | 50 | 30°C | 15-30% |
| **Hard (3)** | 20 | 20 | 30°C | 30-40% |

### Events

The game features 8 possible events plus "quiet days":

| # | Event Name | Effect |
|---|------------|--------|
| 0 | Quiet Day | Minimal resource changes |
| 1 | Temperature > 80°C | Critical failure |
| 2 | Cooling System Failure | Reduces cooling efficiency |
| 3 | Electrical Overload | Damages servers |
| 4 | Fire in Technical Room | Severe temperature increase |
| 5 | Flooding | Damages cooling system |
| 6 | Cyberattack | Increases client load |
| 7 | Network Collapse | Server overload |
| 8 | Internal Virus | Complex resource drain |

### Win/Loss Conditions

**Game Over triggers:**
- Temperature exceeds 80°C
- Server capacity reaches 0
- Cooling system fails (≤ 0)
- Clients overwhelm servers (clients ≥ servers)

**Victory condition:**
- Successfully manage all resources for 10 days without any critical events.

## Getting Started

### Prerequisites

- Python 3.x or higher
- Git (for cloning the repository)

Verify your Python installation:
```bash
python --version
```
### Installation
- Clone the repository:
```bash
git clone https://github.com/rmzneydev/economy-survival-simulator.git
```
- Navigate to the project directory:
```bash
cd economy-survival-simulator/data-center-control
```
- Run the game:
```bash
python3 main_loop.py
```

### How to Play

1. Launch the game: python main_loop.py
2. Enter your name: Choose your operator identifier
3. Select difficulty: Enter 1 (Easy), 2 (Medium), or 3 (Hard)
4. Press any key to start the simulation
5. Review daily status: Check the resource table after each day
6. Press any key to advance to the next day
7. Survive 10 days or face the consequences!

### Project Structure
```bash
data-center-control/
│
├── main_loop.py              # Main game loop and orchestration
├── data_entry.py             # User input and initial configuration
├── events_generator.py        # Random event generation system
├── consumption.py             # Resource consumption calculations
├── defeat_validator.py        # Game over condition checks
├── console_interface.py       # All display and UI functions
│
├── test.py             # Product Owner's test cases
│
├── LOG.md                 # Daily Scrum logs
│
└── README.md                  # This file
```

### Development Team

This project follows a collaborative structure inspired by **Agile
development**.


| Role | Responsibility | Module | Name |
|------------|--------|--------|--------|
| Dev 1|            Data Input System | data_entry.py | [Samuel ](https://github.com/smlprtz992-dot)
| Dev 2|            Main Simulation Loop | main_loop.py | [Andres E.](https://github.com/dresanelles)
| Dev 3|            Event Generator | events_generator.py | [Camilo C.](https://github.com/CAMC2901)
| Dev 4|            Resource Consumption Logic | consumption.py | [Plinio A.](https://github.com/ChristianCode89)
| Dev 5|            Defeat Validator | defeat_validator.py | [Jhosep A.](https://github.com/jhosep-1997)
| Dev 6|            Console Interface | console_interface.py | [Jhonatan R-](https://github.com/rodriguezvjhona-droid)
| Scrum Master|     Documentation and README | LOG.md /README.MD | [Neyder R.](https://github.com/rmzneydev)
| Product Owner|    Testing and validation | tests.py | [Sharon M.](https://github.com/Zolagos)

------------------------------------------------------------------------
