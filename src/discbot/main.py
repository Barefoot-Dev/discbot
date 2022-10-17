import os
import json
import argparse
import discord
from dotenv import load_dotenv

from discbot.utils import get_discord_client
from discbot.features.dropdown import DropdownView

if __name__ == "__main__":

    # get bot
    client = get_discord_client()

    # parse args
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
    dev = args.dev

    # load config
    if dev:
        print("Loading dev config")
        with open(os.path.join(os.path.dirname(__file__), "dev.config.json"), "r") as f:
            CONFIG = json.load(f)

    else:
        print("Loading prod config")
        with open(os.path.join(os.path.dirname(__file__), "config.json"), "r") as f:
            CONFIG = json.load(f)

    @client.event
    async def on_ready():
        # runs when bot is initialized
        print(f"Logged in as {client.user} (ID: {client.user.id})")
        print("------")

    # runs when command is called
    @client.tree.command()
    async def command_name(interaction: discord.Interaction, arg_one: str):
        print(
            f"Interaction from {interaction.user} in {interaction.guild_id}/{interaction.channel_id}"
        )
        print(f"Command: {interaction.command.name}")
        print(f"Arg: {arg_one}")

        # ignore messages from self self
        if interaction.user == client.user:
            return

        # reply to the user
        await interaction.response.send_message("Hello World!")

        # runs when command is called

    @client.tree.command()
    async def trigger_dropdown(interaction: discord.Interaction):

        user_id = interaction.user.id
        await interaction.response.send_message(
            "Here's a dropdown",
            view=DropdownView(user_id=user_id, question_ix=0, restarting_quiz=True),
            ephemeral=True,
        )

    # run the bot
    load_dotenv()
    client.run(os.getenv("DISCORD_TOKEN"))
