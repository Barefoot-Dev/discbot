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

    # get token from env
    dotenv.load_dotenv()
    token = os.getenv("DISCORD_TOKEN")

    r = requests.get(url, headers={"Authorization": f"Bot {token}"})

    if r.ok:
        print("Commands")
        for command in r.json():
            print("\nName:", command["name"])
            print("ID:", command["id"])
    else:
        print("error", r.status_code)
        print(r.text)
