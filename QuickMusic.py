import discord
import requests
import os

INTENTS = discord.Intents.default()
INTENTS.message_content = True

ENDPOINT = "https://api.genius.com/search/"
HEADERS = {
    "Authorization": "Bearer " + os.getenv("GENIUS_ACCESS")
}


class QuickMusic(discord.Client):
    
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')

    async def on_message(self, message):
        print(f'{message.channel}: {message.author}: {message.author.name}: {message.content}')
        channel = message.channel
        if message.content.startswith("?:find"):
            title = " ".join(message.content.split(" ")[1:])
            await channel.send(f"Searching for ''{title}''...")
            response = requests.get(ENDPOINT, headers=HEADERS, params={"q": title})
            if response.status_code == 200:
                data = response.json()
                song1 = data["response"]["hits"][0]["result"]["full_title"]
                song2 = data["response"]["hits"][1]["result"]["full_title"]
                song3 = data["response"]["hits"][2]["result"]["full_title"]
                await channel.send(f"1. {song1}\n2. {song2}\n3. {song3}")
            else:
                print("ERROR:", response.status_code)

    
