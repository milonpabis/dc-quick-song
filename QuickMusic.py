import discord
import os

#os.environ["DISCORD_TOKEN"] = "..."  -> set the environment variable DISCORD_TOKEN to your bot token
INTENTS = discord.Intents.default()
INTENTS.message_content = True


class QuickMusic(discord.Client):
    
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')

    async def on_message(self, message):
        print(f'{message.channel}: {message.author}: {message.author.name}: {message.content}')

    
