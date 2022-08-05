import asyncio, discord, random, time, json
from discord.ext import commands

bot = commands.Bot(command_prefix="*", self_bot=True) # Change prefix here

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name=f"STREAM NAME HERE", url="FAKE LINK HERE"))
    print(f"streaming on {bot.user} | {bot.user.id}")

bot.run('TOKEN HERE', bot=False) # insert you discord token here