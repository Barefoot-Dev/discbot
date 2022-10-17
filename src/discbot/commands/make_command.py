import os
import json
import requests
import dotenv
from pathlib import Path

if __name__ == "__main__":

    # load config
    config_path = Path(__file__).parents[1] / "config.json"
    with open(str(config_path), "r") as f:
        CONFIG = json.load(f)

    discord_app_id = CONFIG["discord_app_id"]
    url = f"https://discord.com/api/v10/applications/{discord_app_id}/commands"

    json = {
        "name": "joinfamily",
        "type": 1,
        "description": "Join the Kozoku family!",
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
