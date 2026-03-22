# ⚔️Terminal-Souls⚔️
Terminal-Souls is a turn-based RPG combat game played entirely in the terminal. The hero's fate depends on your strategy: will you play it safe with standard attacks, risk it all on a special ability, or heal to survive another round?

# Technical Features
- **Randomized Combat Engine:** Damage values are calculated within dynamic ranges using Python's random library.
- **Critical Hit System:** A 10% chance to double the damage output on any given attack.
- **Enemy AI:** The opponent isn't just a punching bag; if its health drops below 20%, it will prioritize healing automatically.
- **Console Visual Interface:** Features dynamic health bars that update in real-time using ASCII characters: [█████─────].
- **High-Stakes Special Ability:** A powerful move with massive damage potential but a 50% chance of complete failure.

# 🎮 How to Play
Upon starting, you will be prompted to name your hero and your nemesis. Every turn, you can choose one of the following actions:
1. Attack: Consistent and reliable damage.
2. Heal: Restore health using one of your limited potions.
3. Special Ability: A devastating strike that might miss.

Available Commands
When prompted, type the action exactly as shown:
- Attack
- Heal
- Special ability

# 🛠️ Project Structure
The project is modularized for better organization and readability:  
- bucle.py: The entry point containing the game loop and win/loss logic.
- constantes.py: Global configuration values (Initial HP, critical rates, etc.).
- funciones.py: Mathematical logic, damage generation, and UI rendering (health bars).
- funciones_3_4.py: Specific turn-handling logic for both the player and the enemy.

