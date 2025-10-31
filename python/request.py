import requests

response = requests.get("https://api.github.com/users/mcerdeno2021")

if response.status_code == 200:
    data = response.json()
    print(data["login"], data["public_repos"])
else:
    print("Failed to fetch data:", response.status_code)