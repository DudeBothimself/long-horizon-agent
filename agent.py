import time
import random
import json
import os

STATE_FILE = "state.json"

# Load state from file or initialize default state
def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r") as f:
            return json.load(f)
    else:
        return {
            "energy": 100,
            "tasks_completed": 0,
            "last_action": None
        }

# Save state to file
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

# Perform action and update state
def perform_action(action, state):
    if action == "work":
        state["tasks_completed"] += 1
        state["energy"] -= 20
    elif action == "explore":
        state["energy"] -= 10
    elif action == "rest":
        state["energy"] += 25

    # Clamp energy between 0 and 100
    state["energy"] = max(0, min(100, state["energy"]))
    state["last_action"] = action

    return state

# Log current state
def log_state(state):
    print(
        f"[Agent] Action: {state['last_action']} | "
        f"Energy: {state['energy']} | "
        f"Tasks Completed: {state['tasks_completed']}"
    )

# Main loop
def run_agent():
    state = load_state()
    print("Agent started. Press CTRL+C to stop.\n")

    try:
        while True:
            action = decide_action(state)
            state = perform_action(action, state)
            save_state(state)
            log_state(state)
            time.sleep(2)

    except KeyboardInterrupt:
        print("\nAgent stopped. State saved.")

if __name__ == "__main__":
    run_agent()
