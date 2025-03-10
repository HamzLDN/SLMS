import json

def load_json(filename):
    with open(filename, "r") as file:
        return json.load(file)

def save_json(filename, data):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

def delete_user(data, username):
    key_to_delete = None
    for key, value in data.items():
        if value.get("username") == username:
            key_to_delete = key
            break

    if key_to_delete:
        del data[key_to_delete]
        print(f"Deleted user '{username}' ID: {key_to_delete}")
    else:
        print(username, 'not found!')

def remove(username, filename):
    data = load_json(filename)
    delete_user(data, username)
    save_json(filename, data)
