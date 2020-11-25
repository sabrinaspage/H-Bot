import discord
from discord.ext import commands

from nhentai import *

bot = commands.Bot(command_prefix='!')

@bot.command()
async def nhentai(ctx):
    e = discord.Embed()
    e.set_image(url="https://t.nhentai.net/galleries/772164/cover.jpg")
    await ctx.send("Hiiiiii",embed=e)

@bot.command()
async def nhentai_search(ctx,*args):
    doujins = retrieveSearch(args[0])
    for i in range(5):
        await ctx.send(str(i+1) + ". " + doujins[i]['title'] + "\n")

@bot.event()
async on_command_completion(ctx):
    pass

@bot.event
async def on_reaction_add(reaction,user):
    pass

"""
@bot.event
async def on_message(message):
    if message.author == bot.user:
        pass

    if message.content.startswith('bruh'):
        await message.channel.send('bruh')
"""
bot.run('NzMxNTcxNzk4Mzk0NTM2MDI4.XwoACw.Z0awqU20kSNrmtBw0YUC6fJo9ds')
