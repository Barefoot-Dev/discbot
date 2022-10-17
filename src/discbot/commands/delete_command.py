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
    command_id = 1028974526505156668  # command to delete!

    url = f"https://discord.com/api/v10/applications/{discord_app_id}/commands/{command_id}"

    # get token from env
    dotenv.load_dotenv()
    token = os.getenv("DISCORD_TOKEN")

    # For authorization, you can use either your bot token
    headers = {"Authorization": f"Bot {token}"}

    r = requests.delete(url, headers=headers)

    if r.ok:
        print("Command deleted")
    else:
        print("error", r.status_code)
        print(r.text)
