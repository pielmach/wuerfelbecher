import os

from discord.ext.commands import Bot  # type: ignore
from discord.ext.commands import Context  # type: ignore
from discord.ext.commands import DefaultHelpCommand  # type: ignore

from . import commands as wuerfelbecher_commands


def get_bot_token(path_to_file: str, environment_variable: str) -> str:
    """Strategy: First check for docker secret at path_to_file, then fallback to environment_variable, then fail."""
    if os.path.exists(path_to_file):
        print("Found secret to login at {}".format(path_to_file))
        return open(path_to_file).read().rstrip("\n")
    elif environment_variable in os.environ:
        print("Found environment variable {} to login".format(environment_variable))
        return os.getenv(environment_variable, "ENV_VAR_WAS_UNDEFINED")
    else:
        print(
            "Failed to find access token for discord bot at {} or environment variable {}".format(
                path_to_file, environment_variable
            )
        )
        raise RuntimeError(
            "Failed to find access token for discord bot at {} or environment variable {}".format(
                path_to_file, environment_variable
            )
        )


def setup_bot() -> Bot:
    bot = Bot(
        command_prefix="!",
        description="Wuerfelbecher is a simple dice rolling bot for pen & paper roleplaying",
        help_command=DefaultHelpCommand(no_category="Available commands"),
    )

    @bot.event
    async def on_ready() -> None:
        print("{0.user} online and ready to roll".format(bot))

    @bot.command(
        brief="Report statistics for a given dice type.",
        description="Report statistics for a given dice type.",
        usage="DiceType",
        help="DiceType can be d or w followed by number of sides the dice has. Examples are d6 or w20.",
    )
    async def stats(ctx: Context, *args: str) -> None:
        await ctx.send(wuerfelbecher_commands.stats(" ".join(args)))

    @bot.command(
        brief="Roll dices according to a given dice pattern. Use r as a short alias.",
        description="Roll dices according to a given dice pattern. Multiple patterns split by a space are also possible to roll at once.",
        usage="DicePattern",
        help="DicePattern can be a number, followed by a DiceType, optionally followed (or preceded) by a positive or negative modificator, including just + or - sign. If any modifier is given, the dice results are summed up, including the modifier. Examples are 3w20, 1d6+4, 12+w6, or 7d6+.\n\nDiceType can be d or w followed by number of sides the dice has. Examples are d6 or w20.",
        aliases=["r"],
    )
    async def roll(ctx: Context, *args: str) -> None:
        await ctx.send(ctx.author.display_name + ": " + wuerfelbecher_commands.roll(" ".join(args)))

    return bot
