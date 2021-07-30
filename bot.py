import discord
from discord.ext import commands
from dotenv import load_dotenv
import os


client = commands.Bot(command_prefix = '!')
load_dotenv('.env')

@client.command()
async def load (ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload (ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


client.run(os.getenv('BOT_TOKEN'))
