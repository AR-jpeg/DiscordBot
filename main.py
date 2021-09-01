from discord.ext import commands
# import dotenv
import os

# dotenv.load()

# Load environment secrets
TOKEN = os.getenv('TOKEN')
PREFIX = os.getenv('PREFIX')
BADWORDS = os.getenv('BADWORDS')

BADWORDS = BADWORDS.split(',')

bot = commands.Bot(command_prefix=PREFIX)


@bot.event
async def on_ready():
    print('Logged in as {0.user}'.format(bot))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    else:
        await message.channel.send(message.content)

@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! Bot Latency: {round (bot.latency * 1000)} ms')


bot.run(TOKEN)
