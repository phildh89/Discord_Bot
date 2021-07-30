import discord
from discord.ext import commands
from dotenv import load_dotenv
import os


bot = commands.Bot(command_prefix = '!')
load_dotenv('.env')

@bot.command()
async def load (ctx, extension):
    bot.load_extension(f'cogs.{extension}')

@bot.command()
async def unload (ctx, extension):
    bot.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')


bot.run(os.getenv('BOT_TOKEN'))
