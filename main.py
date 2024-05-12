from typing import Final 
import os 
from dotenv import load_dotenv
from discord.ext import commands
from discord import Intents, Client, Message, Member
import asyncio 
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
    if "Anindit" in message.content:
        await channel.send("Anindit? more like :nerd:")
    if "Chris" in message.content:
        await channel.send("By definition, Chris is by definition an intellectual")
    if "Uzair" in message.content:
        await channel.send("Uzair? Bro is the most clutch up man on this earth")
    if "Mohamed" in message.content:
        await channel.send("Mohamed, a man who enjoys the slumber of night")
    await bot.process_commands(message)


@bot.command()
async def Pingloop(ctx, member: Member = None):
  if member == None:
    member = ctx.author
  try: 
    await ctx.send("How many times do you want to ping this person? ")
    num_Ping = await bot.wait_for("message", timeout=15, check=lambda message: message.author == ctx.author and message.channel == ctx.channel)
  except asyncio.TimeoutError():
    await ctx.send("You unfortunately ran out of time. ")
  try: 
    loop_Counter = int(num_Ping.content)
  except: 
    await ctx.send("This is not a real number")
  if loop_Counter < 0:
    await ctx.send("Negative number is invalid")
  elif loop_Counter > 20:
     await ctx.send("The amount of pings is capped at 20!")
  else: 
    loop_Start = 0
    while (loop_Start < loop_Counter):
      await ctx.send(member.mention)
      loop_Start = loop_Start + 1  


bot.run(TOKEN)