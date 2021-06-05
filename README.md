# Wuerfelbecher 

Wuerfelbecher is a simple, Python 3.8+ based, Discord bot for rolling dices.

It was created during the COVID-19 pandemic, when my pen&paper roleplaying round moved online to practice social distancing and existing bots weren't reliably working. I needed to have a bot that works when we needed it most to get some escapism.
Maybe it now helps others too.

## Discord commands

Wuerfelbecher isn't limited to a particular roleplaying system and supports any sided dices. It's even bilingual, it supports the English `d` for dice as well as the German `w` for Wuerfel! 😃

Some sample commands you can try out:
* `!help` for built-in help
* `!r 3d20` will roll 3 d20
* `!r 1w6+4` will roll 1 d6 and add 4 to it
* `!r 2d6-2` will roll 2 d6, sum them up and subtract 2 from the sum
* `!r 10d6+` will roll 10 d6 and sum them up
* `!r d20 1w6+4` will roll 1 d20, as well as, roll 1 d6 and add 4 to it
* `!stats d20` will print some stats for d20 dices - BETA

Note on the `!stats` command: Of course the probability is uniform (see `dice_roller.py`) but we all know these sessions when dices don't do as we want. We had some fun looking at the stats after some of these really screwed up sessions were simply everything went wrong... 😱

## Setup

You can run Wuerfelbecher either with pure Python or use the Dockerfile to build a Linux based image.

### Prerequisites

You must have a Discord account and you must have registered a new application and obtained the bot's secret token, subsequently referred to as `<discord-bot-token>`.

See first section of https://www.freecodecamp.org/news/create-a-discord-bot-with-python/ for a simple guide of how to register a new application and make it join your Discord server.

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






