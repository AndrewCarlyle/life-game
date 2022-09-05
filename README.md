# life-game
Python project to simulate the game of life, and test how different variables affect the simulation.

Current rules/game logic:
1. A player can only eat one "food" per turn, even if their location has more than one
2. A player dies if their energy gets to zero, or their hunger gets to 10
3. All players currently limited to reproducing once / turn, new players cannot reproduce in their first turn
4. Parents and their children cannot fight
5. New child players currently spawn at a random location, this can be toggled using RANDOM_NEW_PLAYER_LOCATION in world.py

TODO:
- Add water to work in a similar way as food currently does? --> Also means adding thirst attribute
- Cap child attributes at 10? (with minimum of 0 as well?)
