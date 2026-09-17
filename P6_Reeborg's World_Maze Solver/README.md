# Reeborg's World — Maze Solver

An algorithmic Python challenge completed using **Reeborg's World**. The objective was to navigate Reeborg through a maze and reach the goal using conditional logic, loops, and a wall-following algorithm.

## Project Overview

This challenge focuses on algorithmic problem solving rather than simply executing a predefined sequence of movements.

Instead of manually specifying the path through the maze, the program continuously checks Reeborg's surroundings and determines the next action based on the available paths.

The solution uses the **right-hand rule**, also known as the **wall-following algorithm**.

## Algorithm

The robot follows this decision process:

1. Check whether the right side is clear.
2. If the right side is clear:
   - Turn right.
   - Move forward.
3. Otherwise, check whether the front is clear.
4. If the front is clear:
   - Move forward.
5. If neither the right side nor the front is clear:
   - Turn left.
6. Repeat until Reeborg reaches the goal.

This can be represented as:

```text
                Start
                  │
                  ▼
           Is the goal reached?
             /           \
           Yes            No
            │              │
           Stop      Is the right clear?
                       /          \
                     Yes           No
                      │             │
                 Turn right    Is front clear?
                      │          /       \
                    Move       Yes        No
                                │          │
                              Move     Turn left
                                           │
                                           ▼
                                      Repeat
