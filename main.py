import requests


def show_activity(user):
    URL = f"https://api.github.com/users/{user}/events"

    req = requests.get(URL)

    data = req.json()
    try:
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
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP Error:{http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Error connection: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timed out error:{timeout_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Error: {req_err}")


while True:
    answer = input()
    user_input = answer.split(" ")
    if user_input[0] == "github-activity":
        show_activity(user_input[1])
    elif answer == "q":
        break
    else:
        print("Error,try command 'github-activity' <username> ")
