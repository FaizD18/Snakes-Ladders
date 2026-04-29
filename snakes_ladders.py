"""
Snake & Ladder Game - CMPSC 132 Final Project
A 2-player terminal-based game.
"""

import random


# Snake mappings: head cell -> tail cell
snakes = {16: 6, 48: 30, 64: 40, 79: 19, 93: 68, 95: 24, 99: 78}

# Ladder mappings: bottom cell -> top cell
ladders = {3: 22, 11: 40, 20: 38, 28: 76, 50: 67, 63: 81, 71: 91}


def roll_dice():
    """Returns a random number between 1 and 6."""
    return random.randint(1, 6)


def take_turn(player_num, position):
    """
    Plays one turn for a player. Returns the new position,
    or None if the player chose to quit.
    """
    choice = input(f"\nPlayer {player_num}'s turn. Press ENTER to roll (or 'q' to quit): ")
    if choice.strip().lower() == "q":
        return None

    dice = roll_dice()
    print(f"Player {player_num} rolled a {dice}.")

    new_pos = position + dice

    # Overshoot rule: must land on exactly 100
    if new_pos > 100:
        print(f"Overshot 100! Player {player_num} stays at cell {position}.")
        return position

    print(f"Player {player_num} moves to cell {new_pos}.")

    # Check for snake or ladder
    if new_pos in snakes:
        new_pos = snakes[new_pos]
        print(f"Oh no, a snake! Slid down to cell {new_pos}.")
    elif new_pos in ladders:
        new_pos = ladders[new_pos]
        print(f"A ladder! Climbed up to cell {new_pos}.")

    return new_pos


def main():
    """Main game loop."""
    print("=" * 40)
    print("    SNAKE & LADDER GAME")
    print("=" * 40)

    # Both players start at cell 0 (off the board)
    pos1 = 0
    pos2 = 0

    while True:
        # Player 1's turn
        new_pos = take_turn(1, pos1)
        if new_pos is None:
            print("\nGame ended. Thanks for playing!")
            break
        pos1 = new_pos
        print(f"Player 1 is at {pos1}, Player 2 is at {pos2}")
        if pos1 == 100:
            print("\n*** Player 1 WINS! ***")
            break

        # Player 2's turn
        new_pos = take_turn(2, pos2)
        if new_pos is None:
            print("\nGame ended. Thanks for playing!")
            break
        pos2 = new_pos
        print(f"Player 1 is at {pos1}, Player 2 is at {pos2}")
        if pos2 == 100:
            print("\n*** Player 2 WINS! ***")
            break


if __name__ == "__main__":
    main()
