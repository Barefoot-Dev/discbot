import os
import time
import requests
import interactions
from dotenv import load_dotenv
from sqlalchemy import sql, types, insert, values, table, column, and_, create_engine
from sqlalchemy.sql.expression import delete
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

# from sqlalchemy.orm import Session, registry
from sqlalchemy.engine import reflection

load_dotenv()


def get_discord_bot():
    return interactions.Client(
        token=os.getenv("DISCORD_TOKEN"),
        intents=interactions.Intents.DEFAULT
        | interactions.Intents.GUILD_MESSAGE_CONTENT,
    )


def get_http_client():
    return interactions.HTTPClient(token=os.getenv("DISCORD_TOKEN"))


async def send_dm(user_id, message, client):
    user = await client.fetch_user(user_id)
    print("Got user", user)
    await user.create_dm()
    await user.send(message)
