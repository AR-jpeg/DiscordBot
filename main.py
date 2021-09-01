from discord.ext import commands
from dotenv import load
import os

load()

# Load environment secrets
TOKEN = os.getenv('TOKEN')
PREFIX = os.getenv('PREFIX')

with open('badwords') as f:
    badWords = f.read()


bot = commands.Bot(command_prefix=PREFIX)


@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! Bot Latency: {round (bot.latency * 1000)} ms')


print("Bot Is Running!")

bot.run(TOKEN)
