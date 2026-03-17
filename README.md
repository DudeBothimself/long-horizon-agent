# long-horizon-agent

Inspired by long-horizon agent architectures used in modern AI systems.

---

## Overview

This project implements a simple long-running autonomous agent that continuously observes state, makes decisions, and adapts over time.

The goal is to simulate foundational concepts behind long-horizon AI systems, including:

- State tracking  
- Decision-making loops  
- Feedback-driven behavior  
- Continuous execution  

---

## Features

- Persistent state tracking using JSON  
- Decision logic based on environment conditions  
- Continuous execution loop  
- Action logging for system analysis  

---

## Tech Stack

- Python  
- JSON (state persistence)

---

## How It Works

The agent operates in a continuous loop:

1. Observes its current state  
2. Selects an action based on predefined logic  
3. Updates internal state  
4. Logs the action and results  
5. Repeats indefinitely  

---

## Example Output

```text
[Agent] Action: work | Energy: 80 | Tasks Completed: 1
[Agent] Action: explore | Energy: 70 | Tasks Completed: 1
[Agent] Action: rest | Energy: 95 | Tasks Completed: 1
```
