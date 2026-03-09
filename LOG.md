# LOG.md
```markdown
# Daily Scrums Log
Proyect: Data Center Control
Product owner: Sharon Meriño
Scrum Master: Neyder Ramirez
Dev 1: Samuel Pertuz
Dev 2: Andres Elle
Dev 3: Camilo Coronado
Dev 4: Plinio Acuña
Dev 5: Jhosep Ahumada
Dev 6: Jhonatan Rodriguez

## 📆 Day 1: – Initial Planning

* What was done?
 - The scope of the simulator was defined (10 days of management).
 - The 8 roles were assigned.
 - The repository was created on GitHub.
 - The Kanban board was configured (To Do / In Progress / Done).
 - Each developer created their branch.

* What will be done tomorrow?
 - Start base development of each module.
 - Define the structure of shared global variables.

* Locks:
 - None.

## 📆 Day 2: - Base Development
* Dev 1: Implemented name and difficulty capture.
* Dev 2: Created basic structure of the 10-day while loop.
* Dev 3: Investigated the use of random.
  - Impediment: Defining common global variables.
  - Solution: It was agreed to standardize variable names.
* Dev 4: Analyze the project's population and size.
* Dev 5: Define defeat conditions and design critical temperature validation (>80°C).
* Dev 6: Designed output:
  - Impediment: A permissions issue  on the reposiroty
  - Solution: It was resolved by accepting the repository invitation as a contributor.

## 📆 Day 3: 
Meeting with the client where they requested the use of functions in the code.
* Dev 1: Translating and implementinga change in the code logic.
* Dev 2: Add the while loop to a function and update the branch on GitHub.
* Dev 3: Remove unnecessay events and add function to the code.
* Dev 4: Add a function to decrase resources based on the event, and a function to increase temperature based on the event.
* Dev 5: Add more conditionals and translate.
* Dev 6: Improving the code logic and translating.

## 📆 Day 4:
We met with the client, we agreed to change the delivery date, but with new requirements for code changes.
* Dev 1: Added more funtions to their code. 
* Dev 2: Refactored the loop logic to align with new specification.
* Dev 3: Added changes requested by the client to the code.
* Dev 4: Made changes to the code to meet the new requirements. 
* Dev 5: Resolved a bug related to a specific variable. 
* Dev 6: Completed UI development and is currently optimizing the design.

## 📆 Day 5:
We delivered the mvp and a meeting was held with the client to present the updates.

## 📆 Day 6:
We had a meeting on Discord to finalize some code details:
* Dev 1: Changed lowercase to uppercase letters.
* Dev 2: Imported functions from other files, translated the days into English, added an input prompt for the user to start the simulation, and added conditionals to check if the game is over.
* Dev 3: Changed the probability range for the difficulty levels and added comments to the code.
* Dev 5: Imported functions from other files to display a game-over message and added a conditional for the critical event to prevent the game from continuing when the temperature is over 80°C.
* Dev 6: Modified the code so the show_player_summary function only takes the difficulty as an integer, added the cooling variable to display it in the table, and added line breaks for longer texts.


## 📆 Day 7:
The documentation was completed, and the code was tested to ensure there are no errors.
