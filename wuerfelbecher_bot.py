import discord
import os
import wuerfelbecher

def removeprefix(command: str, prefix: str) -> str:
    if command.startswith(prefix):
        return command[len(prefix):]
    return

def help() -> str:
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
    client = discord.Client()

    @client.event
    async def on_ready():
        print('{0.user} online and ready to roll'.format(client))

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if message.content.startswith('!roll'):
            await message.channel.send(message.author.name + ': ' + wuerfelbecher.commands.roll(removeprefix(message.content, '!roll')))
        elif message.content.startswith('!r'):
            await message.channel.send(message.author.name + ': ' + wuerfelbecher.commands.roll(removeprefix(message.content, '!r')))
        elif message.content.startswith('!stats'):
            await message.channel.send(wuerfelbecher.commands.stats(removeprefix(message.content, '!stats')))
        elif message.content.startswith('!help'):
            await message.channel.send(help())

    client.run(os.getenv('DISCORD_BOT_TOKEN'))