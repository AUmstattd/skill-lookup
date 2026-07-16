import requests

def fetch_user(username):
    response = requests.get(f"https://api.github.com/users/{username}")
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"fetch_user failed for '{username}': status {response.status_code}")
        return None

print(fetch_user('AUmstattd'))
print(fetch_user('oaisndai'))