import os
import discord
from discord import app_commands

# taken from: https://github.com/Rapptz/discord.py/blob/master/examples/app_commands/basic.py
class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        # A CommandTree is a special type that holds all the application command
        # state required to make it work. This is a separate class because it
        # allows all the extra state to be opt-in.
        # Whenever you want to work with application commands, your tree is used
        # to store and work with them.
        # Note: When using commands.Bot instead of discord.Client, the bot will
        # maintain its own tree instead.
        self.tree = app_commands.CommandTree(self)


def get_discord_bot():
    intents = discord.Intents.default()
    intents.message_content = True
    client = MyClient(intents=intents)
    return client