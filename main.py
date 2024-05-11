from typing import Final 
import os 
from dotenv import load_dotenv
from discord.ext import commands
from discord import Intents, Client, Message

# Load our individual token
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')
print(TOKEN)


# Setup our bot 
intents = Intents.all()
bot = Client(intents=intents)
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_read():
    print(f"Logged in as {bot.user}")

@bot.command()
async def Test(ctx):
    await ctx.send("Hello, I am the UofT Engineer")

@bot.event
async def on_message(message):
    channel = message.channel
    if message.author == bot.user:
        return 
    if "Zaeem" in message.content:
        await channel.send("Zaeem eats lots of fish")
    await bot.process_commands(message)



bot.run(TOKEN)