import time
import random
import json
import os

STATE_FILE = "state.json"

# Load state
def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r") as f:
            return json.load(f)
    else:
        return {
            "energy": 100,
            "tasks_completed": 0,
            "last_action": None,
            "score": 0
        }

# Save state
def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=4)

# Decision logic
def decide_action(state):
    if state["energy"] < 30:
        return "rest"
    elif state["tasks_completed"] % 5 == 0 and state["tasks_completed"] != 0:
        return "explore"
    else:
        return random.choice(["work", "explore"])

# Reward system
def calculate_reward(action):
    if action == "work":
        return 10
    elif action == "explore":
        return 5
    elif action == "rest":
        return -2
    return 0

# Perform action
def perform_action(action, state):
    reward = calculate_reward(action)

    if action == "work":
        state["tasks_completed"] += 1
        state["energy"] -= 20
    elif action == "explore":
        state["energy"] -= 10
    elif action == "rest":
        state["energy"] += 25

    # Clamp energy
    state["energy"] = max(0, min(100, state["energy"]))

    # Update score
    state["score"] += reward
    state["last_action"] = action

    return state, reward

# Logging
def log_state(state, reward):
    print(
        f"[Agent] Action: {state['last_action']} | "
        f"Energy: {state['energy']} | "
        f"Tasks: {state['tasks_completed']} | "
        f"Reward: {reward} | "
        f"Score: {state['score']}"
    )

# Main loop
def run_agent():
    state = load_state()
    print("Agent started. Press CTRL+C to stop.\n")

    try:
        while True:
            action = decide_action(state)
            state, reward = perform_action(action, state)
            save_state(state)
            log_state(state, reward)
            time.sleep(2)

    except KeyboardInterrupt:
        print("\nAgent stopped. State saved.")

if __name__ == "__main__":
    run_agent()
