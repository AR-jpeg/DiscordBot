from discord.ext import commands
import os


# Load environment secrets
TOKEN = os.getenv('TOKEN')
PREFIX = os.getenv('PREFIX')
BADWORDS = os.getenv('BADWORDS').split(',')
hello = ['Hi', 'hi', 'Yo', 'yo','HI', 'Hello']


bot = commands.Bot(command_prefix='?')


@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! Bot Latency: {round (bot.latency * 1000)} ms')

@bot.command()
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount=0):
    await ctx.channel.purge(limit=amount+1)
   

@bot.event
async def on_member_join(member):
    print(f' {member} has joined the server')
  

@bot.event
async def on_ready():
    print('Logged in as {0.user}'.format(bot))


@bot.event
async def on_message(message):
    print(str(message.author) + ": " +message.content)
    words = message.content.split(' ')


    for word in words:
        if word in hello:
            await message.add_reaction('👋') 

        if word in BADWORDS:
            await message.author.send(f'Hey <@{str(message.author.id)}>! Swearing in the server is not allowed! Please do not continue with this behavior or else you may get banned!')
            
            await message.delete()

    await bot.process_commands(message)


bot.run(TOKEN)
