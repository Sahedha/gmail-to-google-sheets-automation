import json
from config import STATE_FILE

def load_state():
    try:
        with open(STATE_FILE, "r") as f:
            return set(json.load(f))
    except FileNotFoundError:
        return set()

def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(list(state), f)
