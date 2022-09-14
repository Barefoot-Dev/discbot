import os
import json
import requests
import dotenv

if __name__ == "__main__":

    # load config
    with open(os.path.join(os.path.dirname(__file__), "config.json"), "r") as f:
        CONFIG = json.load(f)

    discord_app_id = CONFIG["discord_app_id"]
    command_id = 00000  # command to delete!

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
