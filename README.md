# jasper_twitchchat
A basic twitch chat connector that redirects information to a rasa instance.

# How to Install Locally
Ensure you are working out of a python venv:

`python -m venv .venv` to create one

Then you can activate it with `source .venv/bin/activate` if on linux for example.

Now you can install the requirements:

`pip install requirements.txt`

# How To Use Locally
Now that you have it installed you can use it by filling out the .env from the .env.example information then run the bot via:

From your activated virtual env:

`python bot.py` and you should see some output saying it connected and the user it connected as.

# Testing The Bot
You can test the bot by going to twitch chat and doing `!hello` and seeing if it responds hello.
