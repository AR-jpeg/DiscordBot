from dotenv import load
import discord
import os

load()

# Load environment secrets
TOKEN = os.getenv('TOKEN')
PREFIX = os.getenv('PREFIX')


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

        if message.content == PREFIX + "ping":
            await message.channel.send(f'Pong! Bot Latency: {round (client.latency * 1000)} ms')

        # if message.author != self.user:
        #     await message.channel.send('YOOOOO')


# running the client
client = MyClient()
client.run(TOKEN)
