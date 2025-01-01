import requests
import time


def show_activity(user):
    URL = f"https://api.github.com/users/{user}/events"

    req = requests.get(URL)

    data = req.json()

    for name in data:
        push = name["type"]
        name_repo = name["repo"]["name"]
        user = name["actor"]["login"]
        match push:
            case "PushEvent":
                print(f"- Pushed {len(name["payload"]["commits"])}"
                      f" commits to {name_repo}.\n")
            case "WatchEvent":
                print(f"- Started wathcing {name_repo}\n")
            case "PullRequestEvent":
                print(f"- Has {name["payload"]["number"]} pull request\n")
            case "CreateEvent":
                print(f"- {name["payload"]["description"]}\n")


while True:
    answer = input()
    user_input = answer.split(" ")
    if user_input[0] == "github-activity":
        show_activity(user_input[1])
        time.sleep(30)
    elif answer == "q":
        break
    else:
        print("Error,try command 'github-activity' <username> ")
