from wuerfelbecher import bot as wuerfelbecher_bot

if __name__ == "__main__":
    bot = wuerfelbecher_bot.setup_bot()
    bot.run(wuerfelbecher_bot.get_bot_token("/run/secrets/discord_bot_token", "DISCORD_BOT_TOKEN"))
