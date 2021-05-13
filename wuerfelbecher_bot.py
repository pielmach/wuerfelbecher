import discord
from discord.ext import commands
import os
import wuerfelbecher

def help_message() -> str:
    return '''
    The Würfelbecher Bot knows about:
    > !help - This command
    > !roll *DicePattern* or !r *DicePattern* - Will roll dices according to given pattern. Multiple patterns split by a space are also possible.
    > !stats *DiceType* - Will report stats on given dice type
    > 
    > *DiceType* can be d or w followed by number of sides. Examples: d6, w20
    > *DicePattern* can be a number, followed by a *DiceType*, optionally followed (or preceded) by a positive or negative modificator, including just + or - sign. If any modifier is given, the dice results are summed up, including the modifier. Examples: 3w20, 1d6+4, 12+w6, 7d6+
    '''

if __name__ == '__main__':
    bot = commands.Bot(command_prefix='!',
     description='Wuerfelbecher is a simple dice rolling bot for pen&paper roleplaying',
     help_command=None)
    
    @bot.event
    async def on_ready():
        print('{0.user} online and ready to roll'.format(bot))

    # TODO: consider to replace with auto-generated help command
    @bot.command()
    async def help(ctx):
        await ctx.send(help_message())

    @bot.command()
    async def stats(ctx, *args):
        await ctx.send(wuerfelbecher.commands.stats(' '.join(args)))

    @bot.command()
    async def roll(ctx, *args):
        await ctx.send(ctx.author.name + ': ' + wuerfelbecher.commands.roll(' '.join(args)))

    @bot.command()
    async def r(ctx, *args):
        await ctx.send(ctx.author.name + ': ' + wuerfelbecher.commands.roll(' '.join(args)))

    bot.run(os.getenv('DISCORD_BOT_TOKEN'))