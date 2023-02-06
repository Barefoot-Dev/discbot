# Discord Bot template

A python-based Discord bot that can be hosted on Heroku.
More info -> https://devcenter.heroku.com/articles/getting-started-with-python.

# Set up

**1. Create a Discord bot**

1. Set up an application **and** bot in the [Developer Portal](https://discord.com/developers/applications
)
2. In the Portal, turn on 'Message Content Intent'

**2. Install this repo**

`pip install -e .`


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

**Update the cloud isntance**

`git push heroku main`

**Ensure it is running**

`heroku ps:scale web=1`

**Monitor the cloud instance**

`heroku logs --tail -a <app-name>`

**Create config / environment vars**

`heroku config:set -a \<app-name> \<key>=\<value>`

**Create a postgres database**

1. Add the Heroku Postgres add-on
2. Go to the project's settings and get the DATABASE_URL, put it in your local .env.
3. `pip install sqlalchemy psycopg2-binary`