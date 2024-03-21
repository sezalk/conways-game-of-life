# Game of Life

This is an implementation of Conway's Game of Life using Pygame.

## Instructions

1. Run the script.
2. Click on the grid to toggle cells on/off.
3. Press the SPACE key to start/pause the simulation.
4. Press the 'c' key to clear the grid.
5. Press the 'g' key to generate a random pattern.

## Rules

The Game of Life is a cellular automaton devised by the British mathematician John Horton Conway in 1970. It is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input. The game consists of a grid of cells, each of which can be in one of two possible states, alive or dead. The game evolves in turns, following these rules:

1. Any live cell with fewer than two live neighbors dies, as if by underpopulation.
2. Any live cell with two or three live neighbors lives on to the next generation.
3. Any live cell with more than three live neighbors dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

## Controls

- **Mouse Click**: Toggle cell state.
- **SPACE**: Start/Pause simulation.
- **c**: Clear the grid.
- **g**: Generate a random pattern.

## Dependencies

- Python 3.x
- Pygame

## How to Run

1. Make sure you have Python installed.
2. Install Pygame by running `pip install pygame`.
3. Run the script using `python conwaysgameoflife.py`.

Enjoy the simulation!
