import json
import os

CHECKPOINT_FILE = "outputs/checkpoint.json"

def save_state(step_name, metadata=None):
    state = {
        "last_completed_step": step_name,
        "metadata": metadata or {}
    }
    with open(CHECKPOINT_FILE, "w") as f:
        json.dump(state, f, indent=4)

def load_state():
    if not os.path.exists(CHECKPOINT_FILE):
        return None
    with open(CHECKPOINT_FILE, "r") as f:
        return json.load(f)

def clear_state():
    if os.path.exists(CHECKPOINT_FILE):
        os.remove(CHECKPOINT_FILE)
