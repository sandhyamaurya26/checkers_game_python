# MASTER CHECKERS – AI GAME

**Interactive Checkers Game with Two Player and AI Mode**

- Two Player (Human vs Human)
- Player vs AI Mode
- Strategic AI Decision Making
- Built using Python and Pygame

---

## Project Title

**Checkers AI Game** – Interactive game with Two Player and AI

---

## Introduction

The **Checkers AI Game** is a modern digital version of the classic board game Checkers, designed to combine entertainment with artificial intelligence. In this game, players move their pieces diagonally across the board and capture opponent pieces by jumping over them. The primary objective is to eliminate all opponent pieces or block them from making any legal moves.

By converting the traditional board game into a digital format, players can enjoy checkers anytime and anywhere without requiring a physical board.

The integration of artificial intelligence makes the game more engaging. The AI opponent analyzes possible moves, plans strategies, and adapts to different play styles. This ensures challenging gameplay for both beginners and experienced players while also serving as an educational learning tool.

### Video Link for Game:
[Click here to watch the gameplay video](https://drive.google.com/file/d/1arpGgKGknQ6jIhjvuE9FMR9mlJqQuAMw/view?usp=sharing)

### Game Screenshot:
<p align="center">
  <img src="https://drive.google.com/uc?export=view&id=1eJ0q3-iwZGQ6BiDmvCu_GXWUJrIlWSFO" alt="Checkers Game Screenshot" width="400">
</p>

---

## Objectives

- Develop an interactive and intelligent Checkers game
- Implement strategic AI logic for competitive gameplay
- Design a clean and user-friendly graphical interface
- Support Player vs Player and Player vs AI modes
- Track game progress, scores, and turns in real time
- Provide restart and replay options without closing the application

---

## Libraries and Modules Used

| Library | Purpose |
|---------|---------|
| **Pygame** | For game window creation, board rendering, animations, and user input handling |
| **sys** | For program exit and system-level operations |
| **random** | For basic AI move selection and beginner difficulty levels |

---

## Features

- Intelligent AI using Minimax with Alpha-Beta Pruning
- Interactive Pygame-based graphical user interface
- Two Player (Human vs Human) gameplay mode
- Player vs AI gameplay mode with strategic decision-making
- Strict move validation based on official Checkers rules
- Mandatory captures and automatic king promotion
- Real-time score and turn status display
- Restart and replay functionality
- Optional game history tracking
- Cross-platform compatibility (Windows, Linux, macOS)

---

## Game Flow – Master Checkers

### 1. Start Screen
- Options: Two Player, VS Computer, Exit

### 2. Game Initialization
- 8×8 board setup with initial placement of pieces
- Side panel displays mode, turn indicator, scoreboard, restart and back options

### 3. Player Turn
- Player selects and moves a valid piece
- Mandatory captures are enforced

### 4. AI Turn
- AI analyzes the board and selects the best possible move
- Turn indicator updates automatically

### 5. Move Validation
- Invalid moves are ignored
- Pieces reaching the last row are promoted to King

### 6. Scoring System
- Each capture increases the player's score
- Scoreboard updates in real time

### 7. Game Over Conditions
- A player has no valid moves left or all pieces are captured

### 8. Result Screen
- Displays the winner or draw result
- Options to restart or exit the game

### 9. Game Reset
- Restart resets board and scores
- Back option returns to the start menu

---

## Conclusion

The **Master Checkers Game** project successfully demonstrates the development of a classic board game using Python and Pygame. With support for two-player and AI-based gameplay, real-time score tracking, and strict rule enforcement, the game delivers a smooth and competitive experience.

This project highlights important programming concepts such as:
- Game logic implementation
- Artificial intelligence decision-making
- Event-driven programming
- State management
- Graphical user interface development

Overall, it serves as both an entertaining application and a valuable learning project in Python-based game development.

---

**If you found this project helpful, please give it a star!** 
