import discord

from nhentai import *

client = discord.Client()

@client.event
async def on_read():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startwith('--oof'):
        await message.channel.send(':eggplant:')

client.run('NzMwOTY1ODQwMjQ1MjkzMTA5.Xwkskw.RLP7fMwUTy-sxjfq9N7h5oHfHSU')
