from typing import Final 
import os 
from dotenv import load_dotenv
from discord.ext import commands
from discord import Intents, Client, Message, Embed, Member
import asyncio 
import math
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
async def Calculator(ctx): 
  embed = Embed(
    title="Calculator", 
    description="Let x and y represent two numbers you will input into the calculator.\n\n!Testmath - Run this command if you don't understand the format.\n!Add x y\n!Subtract x y\n!Multiply x y\n!Divide x y\n!Exp x y\n!Sin x\n!Cos x\n!Tan x")
  await ctx.send(embed=embed)

# Each operation as a particular command. 
@bot.command()
async def Testmath(ctx):
  await ctx.send("!Add 4 4")
  addition = lambda x, y: x + y
  await ctx.send(addition(4,4))

@bot.command()
async def Add(ctx, x:float,y:float):
  addition = lambda x, y: x + y
  await ctx.send(addition(x, y))  

@bot.command()
async def Subtract(ctx, x:float, y:float):
  subtraction = lambda x, y: x - y
  await ctx.send(subtraction(x, y))

@bot.command()
async def Multiply(ctx, x:float, y:float):
  multiplication = lambda x, y: x*y
  await ctx.send(multiplication(x, y))

@bot.command()
async def Divide(ctx, x:float, y:float):
  division = lambda x, y: x/y
  await ctx.send(division(x, y))

@bot.command()
async def Exp(ctx, x:float, y:float):
  exponential = lambda x, y: x**y
  await ctx.send(exponential(x, y))

@bot.command()
async def Sin(ctx, x:float):
  sin = lambda x: math.sin(math.radians(x)) 
  await ctx.send(sin(x))

@bot.command()
async def Cos(ctx, x:float):
  cos = lambda x: math.cos(math.radians(x))
  await ctx.send(cos(x))
  
@bot.command()
async def Tan(ctx, x:float):
  tan = lambda x: math.tan(math.radians(x))
  await ctx.send(tan(x))



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