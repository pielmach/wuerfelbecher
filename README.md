# Wuerfelbecher 

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/3368bcddeb8b4d3a93fae7a32e24496e)](https://app.codacy.com/gh/pielmach/wuerfelbecher?utm_source=github.com&utm_medium=referral&utm_content=pielmach/wuerfelbecher&utm_campaign=Badge_Grade_Settings)
[![Build Status](https://github.com/pielmach/wuerfelbecher/actions/workflows/main.yml/badge.svg?branch=master)](https://github.com/pielmach/wuerfelbecher/actions)
[![codecov](https://codecov.io/gh/pielmach/wuerfelbecher/branch/master/graph/badge.svg)](https://codecov.io/gh/pielmach/wuerfelbecher)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)

Wuerfelbecher is a simple, Python 3.8+ based, Discord bot for rolling dices.

It was created during the COVID-19 pandemic, when my pen&paper roleplaying round moved online to practice social distancing and existing bots weren't reliably working. I needed to have a bot that works when we needed it most to get some escapism.
Maybe it now helps others too.

## Discord commands

Wuerfelbecher isn't limited to a particular roleplaying system and supports any sided dices. It's even bilingual, it supports the English `d` for dice as well as the German `w` for Wuerfel! 😃

Some sample commands you can try out:
*   `!help` for built-in help
*   `!r 3d20` will roll 3 d20
*   `!r 1w6+4` will roll 1 d6 and add 4 to it
*   `!r 2d6-2` will roll 2 d6, sum them up and subtract 2 from the sum
*   `!r 10d6+` will roll 10 d6 and sum them up
*   `!r d20 1w6+4` will roll 1 d20, as well as, roll 1 d6 and add 4 to it
*   `!stats d20` will print some stats for d20 dices - BETA

Note on the `!stats` command: Of course the probability is uniform (see `dice_roller.py`) but we all know these sessions when dices don't do as we want. We had some fun looking at the stats after some of these really screwed up sessions were simply everything went wrong... 😱

## Setup

You can run Wuerfelbecher either with pure Python or use the Dockerfile to build a Linux based image.

### Prerequisites

You must have a Discord account and you must have registered a new application and obtained the bot's secret token, subsequently referred to as `<discord-bot-token>`.

See first section of https://www.freecodecamp.org/news/create-a-discord-bot-with-python/ for a simple guide of how to register a new application and make it join your Discord server.

### Running from your local machine with Python only

```bash
# if run locally we read the access token from the environment
export DISCORD_BOT_TOKEN=<discord-bot-token>
pip install -r requirements.txt
python wuerfelbecher_bot.py
```

### Building Docker image and running as a container

```bash
# edit docker-compose.yml to inject access token via environment instead of using docker secrets
echo <discord-bot-token> > discord_bot_token.secret
docker-compose up --build
```

### Running in Azure

If you want to run the bot in Azure, rather than your local machine, you can use the provided [Terraform](https://www.terraform.io/) config (`wuerfelbecher_azure.tf`) to setup an Azure Container Instance that runs the officially released Docker images.

```bash
# read the access token from the environment or skip this command and enter it manually when running the apply
export TF_VAR_discord_bot_token=<discord-bot-token>
terraform init
terraform apply
```

## Code-Style and Tests

Wuerfelbecher was developed using TDD and formatted using isort and black. If you want to tweak it to your needs, below will run all formatters, tests and determine code coverage for you.

```bash
pip install -r requirements.txt
pip install flake8 black isort mypy pytest pytest-cov
# auto-sort imports
isort .
# auto-format code
black --line-length=127 .
# flake8 as run in GitHub action: stop the build if there are Python syntax errors or undefined names
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
# flake8 as run in GitHub action: exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
# type checking with mypy
mypy --disallow-untyped-defs wuerfelbecher/
# execute tests and obtain code coverage
pytest --cov=wuerfelbecher --cov-report=term-missing tests/
```
