import discord
from discord.ext import commands

class Commands(commands.Cog):
    
    def __init__(self,client):
        self.client = client
    
    #Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is ready.')

    #Commands
    @commands.command()
    async def ping(self, ctx):
        await ctx.send('Example Message')


    @commands.command()
    async def clear(self, ctx, amount=5):
        if amount > 0 and amount < 11:
            await ctx.channel.purge(limit=amount)
        else:
            await ctx.send("I can only delete 1 to 10 messages at a time!")


def setup(client):
    client.add_cog(Commands(client))

