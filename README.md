# life-game
Python project to simulate the game of life, and test how different variables affect the simulation.

Current rules/game logic:
1. A player can only eat one "food" per turn, even if their location has more than one
2. A player dies if their energy gets to zero, or their hunger gets to 10

TODO:
- Update movement energy so that energy lost is based on % of speed used, rather than distance moved? --> reward faster players
- Use a simple GUI to display the world/players
- Add water to work in a similar way as food currently does?
- Add way to prevent player from reproducing multiple times in one turn
- Cap child attributes at 10? (with minimum of 0 as well?)
