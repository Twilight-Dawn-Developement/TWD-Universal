from discord.ext import commands
import discord
import os
from dotenv import load_dotenv

load_dotenv()


bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"), intents=discord.Intents.all())
bot.remove_command("help")


@bot.event
async def on_ready():
    print(f"Bot connected to Discord\n"
          f"User: {bot.user.name}#{bot.user.discriminator}\n"
          f"ID: {bot.user.id}\n"
          f"------------------------------")


cogfiles = [
    f"cogs.{filename[:-3]}" for filename in os.listdir("./cogs/") if filename.endswith(".py")
]

for cogfile in cogfiles:
    try:
        bot.load_extension(cogfile)
    except Exception as err:
        print(err)

bot.run(os.getenv("TOKEN"))