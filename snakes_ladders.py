"""
Snake & Ladder Game - CMPSC 132 Final Project
A 2-player terminal-based game.
"""

import random
import time


# Snake mappings: head cell -> tail cell
snakes = {16: 6, 48: 30, 64: 40, 79: 19, 93: 68, 95: 24, 99: 78}

# Ladder mappings: bottom cell -> top cell
ladders = {3: 22, 11: 40, 20: 38, 28: 76, 50: 67, 63: 81, 71: 91}


def roll_dice():
    """Returns a random number between 1 and 6."""
    return random.randint(1, 6)


def print_board(pos1, pos2, name1, name2):
    """
    Prints the 10x10 board with both players' positions.
    Cells are numbered in a snake pattern (left-to-right, then right-to-left).
    """
    print()
    print("=" * 56)
    print("                  SNAKE & LADDER BOARD")
    print("=" * 56)

    # Print rows from top (cells 91-100) down to bottom (cells 1-10)
    for row in range(9, -1, -1):
        if row % 2 == 0:
            cells = list(range(row * 10 + 1, row * 10 + 11))
        else:
            cells = list(range(row * 10 + 10, row * 10, -1))

        row_str = ""
        for cell in cells:
            if cell == pos1 and cell == pos2:
                label = "BB"     # Both players on this cell
            elif cell == pos1:
                label = "P1"
            elif cell == pos2:
                label = "P2"
            elif cell in snakes:
                label = " S"     # Snake head
            elif cell in ladders:
                label = " L"     # Ladder bottom
            else:
                label = str(cell).rjust(2)
            row_str += "[" + label + "]"
        print(row_str)

    print("=" * 56)
    print(f"  S = Snake Head    L = Ladder Bottom    BB = Both Players")
    print(f"  P1 = {name1} (cell {pos1})")
    print(f"  P2 = {name2} (cell {pos2})")
    print("=" * 56)


def get_player_name(prompt, default):
    """Prompts for a name. Returns default if input is blank."""
    name = input(prompt).strip()
    if name == "":
        return default
    return name


def choose_mode():
    """
    Asks the user to pick a game mode.
    Returns True for vs Computer, False for 2-player.
    """
    print("\nGame modes:")
    print("  1. Two Players")
    print("  2. Play vs Computer")
    while True:
        choice = input("Choose mode (1 or 2): ").strip()
        if choice == "1":
            return False
        elif choice == "2":
            return True
        else:
            print("Invalid choice. Please type 1 or 2.")


def take_turn(name, position, history, is_computer=False):
    """
    Plays one turn for a player. Returns the new position,
    or None if a human player chose to quit. Each move is pushed
    onto the history stack (a list used in LIFO style).
    Computer players auto-roll after a short pause.
    """
    if is_computer:
        print(f"\n{name}'s turn. Rolling...")
        time.sleep(1.2)   # short pause so the player can follow along
    else:
        choice = input(f"\n{name}'s turn. Press ENTER to roll (or 'q' to quit): ")
        if choice.strip().lower() == "q":
            return None

    dice = roll_dice()
    print(f"{name} rolled a {dice}.")

    new_pos = position + dice

    # Overshoot rule: must land on exactly 100
    if new_pos > 100:
        print(f"Overshot 100! {name} stays at cell {position}.")
        history.append(f"{name}: rolled {dice}, stayed at {position} (overshoot)")
        return position

    print(f"{name} moves to cell {new_pos}.")

    # Check for snake or ladder
    if new_pos in snakes:
        old_pos = new_pos
        new_pos = snakes[new_pos]
        print(f"Oh no, a snake! Slid down to cell {new_pos}.")
        history.append(f"{name}: rolled {dice}, hit snake at {old_pos}, slid to {new_pos}")
    elif new_pos in ladders:
        old_pos = new_pos
        new_pos = ladders[new_pos]
        print(f"A ladder! Climbed up to cell {new_pos}.")
        history.append(f"{name}: rolled {dice}, climbed ladder at {old_pos}, up to {new_pos}")
    else:
        history.append(f"{name}: rolled {dice}, moved to {new_pos}")

    return new_pos


def show_history(history):
    """Prints the last 10 moves from the history stack."""
    print("\n----- MOVE HISTORY (last 10 moves) -----")
    if not history:
        print("  No moves yet.")
    else:
        for i, move in enumerate(history[-10:], 1):
            print(f"  {i}. {move}")
    print("-----------------------------------------")


def play_game():
    """Runs one full game from start to finish."""
    print("=" * 56)
    print("            WELCOME TO SNAKE & LADDER!")
    print("=" * 56)

    # Pick game mode
    vs_computer = choose_mode()

    # Get player names
    name1 = get_player_name("Enter Player 1's name: ", "Player 1")
    if vs_computer:
        name2 = "Computer"
    else:
        name2 = get_player_name("Enter Player 2's name: ", "Player 2")
    print(f"\n{name1} vs {name2} - first to reach 100 wins!\n")

    # Both players start at cell 0 (off the board)
    pos1 = 0
    pos2 = 0
    # Move history - using a list as a stack (DSA concept)
    history = []

    while True:
        print_board(pos1, pos2, name1, name2)

        # Player 1's turn (always human)
        new_pos = take_turn(name1, pos1, history, is_computer=False)
        if new_pos is None:
            print("\nGame ended. Thanks for playing!")
            show_history(history)
            break
        pos1 = new_pos
        if pos1 == 100:
            print_board(pos1, pos2, name1, name2)
            print(f"\n*** {name1} WINS! ***")
            show_history(history)
            break

        # Player 2's turn (computer if vs_computer is True)
        new_pos = take_turn(name2, pos2, history, is_computer=vs_computer)
        if new_pos is None:
            print("\nGame ended. Thanks for playing!")
            show_history(history)
            break
        pos2 = new_pos
        if pos2 == 100:
            print_board(pos1, pos2, name1, name2)
            print(f"\n*** {name2} WINS! ***")
            show_history(history)
            break


def main():
    """Entry point - lets users play multiple rounds in a row."""
    while True:
        play_game()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("\nThanks for playing! Goodbye.")
            break
        print("\n" + "=" * 56)
        print("Starting a new game...")
        print("=" * 56)


if __name__ == "__main__":
    main()
