import json
import os

MEM_FILE = "memory.json"

def load_memory():
    if not os.path.exists(MEM_FILE):
        return []
    with open(MEM_FILE, "r") as f:
        return json.load(f)

def save_memory(data):
    with open(MEM_FILE, "w") as f:
        json.dump(data, f, indent=2)

def add_memory(task, result):
    data = load_memory()
    data.append({
        "task": task,
        "result": result
    })
    save_memory(data)

