import json

def load_data(path):
    try:
        with open(path) as f:
            return json.load(f)
    except FileNotFoundError:
        print("Could not find the skills. Make sure it's in the same folder")
        return None
    except json.JSONDecodeError:
        print("skills.json exists but isn't valid JSON")
        return None