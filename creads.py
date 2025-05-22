import requests
from requests.auth import HTTPBasicAuth

default_creds = [
    ("admin", "admin"),
    ("admin", "password"),
    ("root", "toor")
]

def check_default_credentials(ip):
    for username, password in default_creds:
        try:
            response = requests.get(f"http://{ip}", auth=HTTPBasicAuth(username, password), timeout=5)
            if response.status_code == 200:
                print(f"Device {ip} is using default credentials: {username}/{password}")
                return True
        except requests.RequestException:
            pass
    return False

# Example usage:
check_default_credentials("192.168.1.100")
