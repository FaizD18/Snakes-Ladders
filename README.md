# Snake & Ladder Game
CMPSC 132 Final Project

## Description
A 2-player terminal-based Snake & Ladder game written in Python. Players take turns rolling a dice and racing to land on cell 100 exactly. Snakes send you down, ladders send you up.

## How to Run
1. Make sure Python 3 is installed.
2. Open a terminal in this folder.
3. Run:
   ```
   python3 snakes_ladders.py
   ```
4. Press ENTER each turn to roll the dice.

## Rules
- Both players start at cell 0
- Roll a dice (1-6) and move forward that many cells
- Land on a snake head -> slide down to its tail
- Land on a ladder bottom -> climb up to its top
- Must land on exactly 100 to win (overshooting keeps you in place)
