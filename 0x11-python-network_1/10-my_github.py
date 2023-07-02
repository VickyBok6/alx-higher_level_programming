#!/usr/bin/python3
"""
Python script that takes your GitHub credentials and uses the GitHub API to display your id
"""

import requests
import sys

def get_user_id(username, token):
    url = f"https://api.github.com/users/{VickyBok6}"
    headers = {"Authorization": f"token {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}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        user_data = response.json()
        user_id = user_data["id"]
        return user_id
    else:
        print("Failed to retrieve user ID.")
        return None

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    user_id = get_user_id(username, token)
    if user_id:
        print(f"User ID: {user_id}")
