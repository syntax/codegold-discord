import discord
from discord.ext import commands

client = discord.Client()
client = commands.Bot(command_prefix='.')


submissions = {}

@client.event
async def on_ready():
    print ("online")

@client.command()
async def submit(ctx):
    submitee = ctx.message.author
    submission = ctx.message.content
    submissions[f'{submitee}'] = f'{submission}'
    await client.get_channel(728561287570915378).send(f'{submitee.mention} just submitted their submission :eyes: ')

@client.command()
async def show():
    if submissions != {}:
        for value in submissions:
            await client.get_channel(728561287570915378).send(f'{value} submitted:\n{len(str(submissions[value])[8:])} chars\n\n```py\n{str(submissions[value])[8:]}```')
    else:
        await client.get_channel(728561287570915378).send('no submissions rn :slight_frown:')
@client.command()
async def clear(ctx):
    submissions.clear()
    await ctx.message.channel.send('cleared')

client.run('')
