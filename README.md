# Wuerfelbecher 

Wuerfelbecher is a simple, Python 3.8+ based, Discord bot for rolling dices.

It was created during the COVID-19 pandemic, when my pen&paper roleplaying round moved online to practice social distancing and existing bots weren't reliably working. I needed to have a bot that works when we needed it most to get some escapism.
Hopefully it now helps others too.

## Prerequisites

You must have a Discord account and you must have registered a new application and obtained the bot's secret token, subsequently referred to as `<discord-bot-token>`. 

See first section of https://www.freecodecamp.org/news/create-a-discord-bot-with-python/ for a simple guide of how to register a new application and make it join your Discord server.

## Setup

You can run Wuerfelbecher either with pure Python or use the Dockerfile to build a Linux based image.

### Running from your local machine with Python only

```bash
export DISCORD_BOT_TOKEN=<discord-bot-token>
pip install -r requirements.txt.pinned
python wuerfelbecher_bot.py
```

### Building Docker image and running as a container

```bash
echo <discord-bot-token> > discord_bot_token.secret
docker-compose up --build
```

## Tests

Wuerfelbecher was developed using TDD. If you want to tweak it to your needs, below will run all tests and determine code coverage for you.

```bash
pip install -r requirements.txt.pinned
pip install coverage
coverage run --source=wuerfelbecher -m unittest -v && coverage report -m
```






