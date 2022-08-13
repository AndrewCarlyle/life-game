# life-game
Python project to simulate the game of life, and test how different variables affect the simulation.

Current rules/game logic:
1. A player can only eat one "food" per turn, even if their location has more than one
2. A player dies if their energy gets to zero, or their hunger gets to 10
3. All players currently limited to reproducing once / turn, new players cannot reproduce in their first turn

TODO:
- Update movement energy so that energy lost is based on % of speed used, rather than distance moved? --> reward faster players
- Use a simple GUI to display the world/players
- Add water to work in a similar way as food currently does?
- Add way to prevent player from reproducing multiple times in one turn
- Cap child attributes at 10? (with minimum of 0 as well?)
- Add list so that players don't interact with the same player in the same turn, clear list at end of turn
- Keep track of parents and stop children from fighting parents?
- Round values in average stats function
