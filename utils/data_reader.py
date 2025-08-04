import json
import os

def load_user_data(user_type):
    path = os.path.join(os.path.dirname(__file__), '..', 'data', 'login_users.json')
    with open(path, 'r') as file:
        data = json.load(file)
    return data[user_type]
