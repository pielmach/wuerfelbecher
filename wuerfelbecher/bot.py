import os

from discord.ext.commands import Bot  # type: ignore
from discord.ext.commands import Context  # type: ignore

from . import commands as wuerfelbecher_commands


def help_message() -> str:
    return """
    The Würfelbecher Bot knows about:
    > !help - This command
    > !roll *DicePattern* or !r *DicePattern* - Will roll dices according to given pattern. Multiple patterns split by a space are also possible.
    > !stats *DiceType* - Will report stats on given dice type
    > 
    > *DiceType* can be d or w followed by number of sides. Examples: d6, w20
    > *DicePattern* can be a number, followed by a *DiceType*, optionally followed (or preceded) by a positive or negative modificator, including just + or - sign. If any modifier is given, the dice results are summed up, including the modifier. Examples: 3w20, 1d6+4, 12+w6, 7d6+
    """


def get_bot_token(secret_path: str, environment_variable: str) -> str:
    """
    Strategy: First check for docker secret at secret_path, then fallback to environment_variable, then fail
    """
    if os.path.exists(secret_path):
        print("Found secret to login at {}".format(secret_path))
        return open(secret_path).read().rstrip("\n")
    elif environment_variable in os.environ:
        print("Found environment variable {} to login".format(environment_variable))
        return os.getenv(environment_variable, "ENV_VAR_WAS_UNDEFINED")
    else:
        print(
            "Failed to find access token for discord bot at {} or environment variable {}".format(
                secret_path, environment_variable
            )
        )
        raise RuntimeError(
            "Failed to find access token for discord bot at {} or environment variable {}".format(
                secret_path, environment_variable
            )
        )


def setup_bot() -> Bot:
    bot = Bot(
        command_prefix="!",
        description="Wuerfelbecher is a simple dice rolling bot for pen&paper roleplaying",
        help_command=None,
    )

    @bot.event
    async def on_ready() -> None:
        print("{0.user} online and ready to roll".format(bot))

    # TODO: consider to replace with auto-generated discord help command
    @bot.command()
    async def help(ctx: Context) -> None:
        await ctx.send(help_message())

    @bot.command()
    async def stats(ctx: Context, *args: str) -> None:
        await ctx.send(wuerfelbecher_commands.stats(" ".join(args)))

    @bot.command()
    async def roll(ctx: Context, *args: str) -> None:
        await ctx.send(ctx.author.name + ": " + wuerfelbecher_commands.roll(" ".join(args)))

    @bot.command()
    async def r(ctx: Context, *args: str) -> None:
        await ctx.send(ctx.author.name + ": " + wuerfelbecher_commands.roll(" ".join(args)))

    return bot
