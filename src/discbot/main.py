import argparse
import interactions
from discbot import CONFIG
from discbot.utils import get_discord_bot

""" commands

run in dev mode:
    python src/discbot/main.py -d

monitor deployment logs:
    heroku logs --tail -a discbot
"""


parser = argparse.ArgumentParser(add_help=False)
parser.add_argument(
    "-d",
    "--dev",
    help="dev mode to test new features",
    required=False,
    default=False,
    action="store_true",
)
args = parser.parse_args()
dev_mode = args.dev

# get bots
bot = get_discord_bot()
print("Got bots")

if dev_mode:
    print("Running in dev")

else:
    print("Running in prod")


# on ready
@bot.event
async def on_ready():
    print("Bot is ready")


# handle main join_twitter_list command
@bot.command(
    name="setup",
    description="Setup the bot!",
    options=[],
)
async def setup(ctx: interactions.CommandContext):

    community_id = int(ctx.guild_id)

    if not dev_mode and community_id == CONFIG["dev_community_id"]:
        # if in prod and get a dev request, ignore it
        print("Ignoring dev request in prod")
    elif dev_mode and community_id != CONFIG["dev_community_id"]:
        # if in dev and get a prod request, ignore it
        print("Ignoring prod request in dev")
    else:
        pass
        # add logic here to handle the command


# run the bot
bot.start()
