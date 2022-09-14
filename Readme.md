# Hosted Discord Bot w/ Heroku

A customisable Discord bot written in Python, that can be hosted on Heroku.
More info -> https://devcenter.heroku.com/articles/getting-started-with-python.

N.B. The bot is not yet fully sentient, don't trust it to make you coffee.

# Set up

**1. Create a Discord bot**

1. Set up an application **and** bot in the [Developer Portal](https://discord.com/developers/applications
)
2. Add the bot's DISCORD_TOKEN to `.env`
3. Add the app id to `config.json`

**2. Install this repo**

`pip install -e .`


# Usage: this repo

**Create a new slash command for your bot.**

`python make_command.py`

**Delete an existing slash command**

`python delete_command.py`

Now write functions in `main.py` to respond to the commands!

**Run locally**

`python src/discbot/main.py`

Pass `-d` when running locally to use `dev.config.json` when testing new features.

# Set up: Heroku
We'll host the Bot on Heroku

**1. Install Heroku-CLI**

`curl https://cli-assets.heroku.com/install-ubuntu.sh | sh`

**2. Login**

`heroku login`

**3. Create an app**

`heroku create`

View the newly created app in the [Heroku dashboard](https://dashboard.heroku.com).


# Usage: Heroku
You can use Heroku's CLI to...

**Update the cloud isntance **

`git push heroku main`

**Ensure it is running**

`heroku ps:scale web=1`

**Monitor the cloud instance **

`heroku logs --tail -a <app-name>`

**Create config / environment vars**

`heroku config:set -a \<app-name> \<key>=\<value>`



