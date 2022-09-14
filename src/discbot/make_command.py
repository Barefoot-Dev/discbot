import os
import json
import requests
import dotenv

if __name__ == "__main__":

    # load config
    with open(os.path.join(os.path.dirname(__file__), "config.json"), "r") as f:
        CONFIG = json.load(f)

    discord_app_id = CONFIG["discord_app_id"]
    url = f"https://discord.com/api/v10/applications/{discord_app_id}/commands"

    json = {
        "name": "command_name",  # main.py function name
        "type": 1,
        "description": "command description",
        "options": [
            {
                "name": "arg_one",  # main.py function arg
                "description": "description of command_argument_one",
                "type": 3,
                "required": True,
            }
        ],
    }

    # get token from env
    dotenv.load_dotenv()
    token = os.getenv("DISCORD_TOKEN")

    r = requests.post(url, headers={"Authorization": f"Bot {token}"}, json=json)

    if r.ok:
        print("Command created")
        print("Name:", r.json()["name"])
        print("ID:", r.json()["id"])  # used in delete_command.py
    else:
        print("error", r.status_code)
        print(r.text)
