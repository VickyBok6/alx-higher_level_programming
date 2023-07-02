#!/usr/bin/python3
"""
Python script that takes 2 arguments in order to solve a problem
"""
import requests
import sys

def get_commits(repository, owner):
    url = f"https://api.github.com/repos/{owner}/{repository}/commits"
    response = requests.get(url)
    
    if response.status_code == 200:
        commits = response.json()
        for commit in commits[:10]:
            sha = commit["sha"]
            author_name = commit["commit"]["author"]["name"]
            print(f"{sha}: {author_name}")
    else:
        print(f"Error: {response.status_code}")
        sys.exit(1)

if __name__ == "__main__":
    repository = sys.argv[1]
    owner = sys.argv[2]
    get_commits(repository, owner)
