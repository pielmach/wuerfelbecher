import discord
import os
import wuerfelbecher

def removeprefix(command: str, prefix: str) -> str:
    if command.startswith(prefix):
        return command[len(prefix):]
    return

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

        if message.content.startswith('!stats'):
            await message.channel.send(wuerfelbecher.commands.stats(removeprefix(message.content, '!stats')))

    client.run(os.getenv('DISCORD_BOT_TOKEN'))