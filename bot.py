import discord
from discord.ext import commands
from dotenv import load_dotenv
import os


bot = commands.Bot(command_prefix = '!')
load_dotenv('.env')

@bot.event
async def on_ready():
    print('Bot is ready.')

@bot.command()
async def ping(ctx):
    await ctx.send('Example Message')


@bot.command()
async def clear(ctx, amount=5):
    if amount > 0 and amount < 11:
        await ctx.channel.purge(limit=amount)
    else:
        await ctx.send("I can only delete 1 to 10 messages at a time!")

bot.run(os.getenv('BOT_TOKEN'))
