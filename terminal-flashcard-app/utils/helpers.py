def load_json(file_path):
    import json
    with open(file_path, 'r') as file:
        return json.load(file)

def format_output(text):
    return f"\n{text}\n"

def get_user_input(prompt):
    return input(format_output(prompt))