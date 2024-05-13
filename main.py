from typing import Final 
import os 
from dotenv import load_dotenv
from discord.ext import commands
from discord import Intents, Client, Message, Embed, Member
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

@bot.command()
async def Name(ctx, member: Member = None):
   if member == None:
      member = ctx.author
   try: 
    await ctx.send(f"{member.name}? What about him?")
    msg = await bot.wait_for("message", timeout=15, check=lambda message: message.author == ctx.author and message.channel == ctx.channel)
   except asyncio.TimeoutError():
      await ctx.send("Next time say something instead of staying quiet")
   await ctx.send(f"{member.mention} {str(msg.content)}")

@bot.command()
async def About(ctx):
   embed = Embed(
      title="About",
      description="Hello, I am the **UofT Engineer** and I will be your personal assistant in your server!",
      color=800080
   )
   embed.set_image(url="https://utcsp.utoronto.ca/wp-content/uploads/2023/04/cropped-utcsp-icon-1.png")
   await ctx.send(embed=embed)



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


@bot.event
async def on_member_join(member):
   await member.send("Welcome to the server!")
   await bot.process_commands(member)

@bot.event
async def on_member_leave(member):
   await member.send("We hope you enjoyed the server!")
   await bot.process_commands(member)

@bot.event
async def on_message(message):
    channel = message.channel
    if message.author == bot.user:
       return None; 
    await bot.process_commands(message)


bot.run(TOKEN)