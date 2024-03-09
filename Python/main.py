import json
import subprocess

def clone_github_repos(username):
    # Fetch the list of repositories using GitHub API
    response = subprocess.run(['curl', f'https://api.github.com/users/{username}/repos'], capture_output=True, text=True)
    
    if response.returncode != 0:
        print("Failed to fetch repositories.")
        return
    
    # Parse the JSON response
    repos = json.loads(response.stdout)
    
    # Clone each repository
    for repo in repos:
        clone_url = repo['clone_url']
        subprocess.run(['git', 'clone', clone_url])

# Replace 'codewithsadee' with the GitHub username you want to clone the repositories from
clone_github_repos('username')

