import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run('NzMwOTY1ODQwMjQ1MjkzMTA5.XwfK_Q.Y0oSOxR6ZeNQuFcL7q489MO9wK0')