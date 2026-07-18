import requests

def fetch_user(username):
    try:
        response = requests.get(f"https://api.github.com/users/{username}")
    except requests.exceptions.ConnectionError:
        print("Could not connect to server")
        return None
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"fetch_user failed for '{username}': status {response.status_code}")
        return None

if __name__ == "__main__":
    print(fetch_user('AUmstattd'))
    print(fetch_user('oaisndai'))