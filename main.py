import requests

NAME = "maglovskiNenad"
URL = f"https://api.github.com/users/{NAME}/events"

req = requests.get(URL)

data = req.json()

for name in data:

    commits = f"https://api.github.com/repos/"
    f"{NAME}/{name["repo"]["name"]}/commits?author={NAME}"

a = requests.get(commits)
d = a.json()
print(d)
