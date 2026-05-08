# 💣 Cannon

A Python implementation of a cannon shooting game, built using the `turtle` graphics library and the `freegames` package. By Gael Leyva and Emma Sofía García.

## Overview

The player fires a projectile from the left side of the screen by clicking anywhere on the window. Targets drift in from the right and fall slowly due to gravity. The goal is to hit as many targets as possible. Targets that leave the screen reappear on the right side, so the game goes on indefinitely.

## Requirements

- Python 3.x
- [`freegames`](https://pypi.org/project/freegames/) library

Use a virtual environment to create an isolated workspace for a project’s dependencies and Python version.
This prevents package conflicts between projects and keeps your system installation clean.

```bash
sudo apt -get install python3-all-venv
python3 -m venv ./games/
source ./games/bin/activate
```

Install the dependency with:

```bash
python3 -m pip install freegames
```

## How to Run

```bash
python3 cannon.py
```

## Controls

| Input | Action |
|---|---|
| `Mouse click` | Fire the projectile toward the clicked position |

## Changes from the Original

### 1. Score counter
A score is tracked and displayed on screen. Each time the projectile hits a target, the score increases by one.

### 2. Gravity variation
The gravitational pull on the projectile was tuned, affecting the arc and range of each shot.

### 3. Gravity applied to targets
Targets are no longer purely horizontal — they now also fall slowly downward as they travel across the screen, making them harder to predict and hit.

### 4. Adjustable ball speed
The projectile's launch speed is calculated from the click position, and the speed multiplier was adjusted to change how fast the ball travels across the screen.

### 5. Endless game
Targets no longer disappear when they leave the screen. Instead, they reposition themselves back to the right edge at a new random height, keeping the game going indefinitely.
