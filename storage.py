# storage.py

import json
#function to save file
def save_to_file(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f)
#this function will load data in json format in the file: r stands for read only rule
def load_from_file(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
